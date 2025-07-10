import numpy as np
import matplotlib.pyplot as plt

"""
在可视化图形应用中，散点图的应用范围也很广泛。
例如，如果某一个点或某几个点偏离大多数点，成为孤立点（Outlier），通过散点图就可以一目了然。
在机器学习中，散点图常常用在分类、聚类当中，以便显示不同类别。
在Matplotlib中，绘制散点图的方法与使用plt.plot()绘制图形的方法类似。
"""
# nbPointers = 50  # 设置要生成的样本点数量为50
# x = np.random.standard_normal(nbPointers)  # 生成50个服从标准正态分布的x坐标值
# y = np.random.standard_normal(nbPointers)  # 生成50个服从标准正态分布的y坐标值
#
# np.random.seed(999827)  # 固定随机数种子以便结果可复现
# colors = np.random.rand(nbPointers)  # 生成每个点的颜色值，范围在[0, 1)
# area = (30 * np.random.rand(nbPointers)) ** 2  # 生成每个点的面积大小，范围是[0, 900)
#
# plt.scatter(x, y, s=area, c=colors, alpha=0.5)  # 绘制散点图，使用上面定义的x, y坐标，颜色和大小，并设置透明度
# plt.show()  # 显示绘制好的散点图

"""
plt.scatter()与plt.plot()的使用方法大致相同。
但相比而言，plt.scatter()只能绘制点状图，且不支持将点与点连成线。
scatter()函数的参数s就是plot()函数中的markersize。
在本例中，它的值是一个随机大小的圆，这些随机大小的圆由第11行代码产生。
参数c表示点的颜色；
alpha表示透明度，其大小不超过1，数值越大越不透明。
"""

"""
下面，我们再来看看散点图在机器学习中的一些具体应用。使用的是经典的Iris（鸢尾花）数据集。
该数据集中包含了150个样本，都属于鸢尾属下的三个亚属，分别是山鸢尾、变色鸢尾和维吉尼亚鸢尾。
数据集中共有四个特征，分别是花萼长度、花萼宽度、花瓣长度、花瓣宽度。
由于pyplot模块只能画出二维图形，则这四个特征两两组合，可以构成6副二维散点图。
"""
# 读取文本数据
data = []  # 创建一个空列表用于存储数据
with open('Iris-data.csv', 'r') as file:  # 以只读模式打开CSV文件
    lines = file.readlines()  # 读取文件的所有行

    for line in lines[1:]:  # 跳过第一行（标题行），遍历其余行
        temp = line.split(',')  # 将每行按逗号分割成列表
        data.append(temp)  # 将分割后的数据添加到data列表中

data_np = np.array(data)  # 将列表转化为numpy数组，方便后续处理

# 处理数据：不读取最后一列（通常是分类标签），并将数值部分转换为浮点数
# 注意：这里假设最后一列是分类标签，前几列是数值特征
data_np = np.array(data_np[:, :-1]).astype(float)

feature_name = ['花萼长度', '花萼宽度', '花瓣长度', '花瓣宽度']  # 使用中文名称更直观  # 设置特征名称（对应数据集中的四个特征）

# 创建3行2列的子图画布，大小为20x15英寸
# 这样安排是因为4个特征两两组合有6种可能，需要6个子图
fig, axes = plt.subplots(3, 2, figsize=(25, 20))

# 解决中文显示问题
try:
    # 设置Matplotlib使用支持中文的字体
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体是常用的中文字体
    # 解决负号显示为方块的问题
    plt.rcParams['axes.unicode_minus'] = False
except:
    # 如果SimHei不可用，尝试其他备选字体
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimSun', 'FangSong']

fig.suptitle('鸢尾花数据集特征散点图矩阵', fontsize=25)  # 设置整个图形的总标题

# 生成所有可能的特征组合（4个特征两两组合）
# 使用列表推导式生成所有组合：[(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)]
feature_pairs = [(i, j) for i in range(4) for j in range(i + 1, 4)]

# 为每个特征组合绘制散点图
for idx, (x_idx, y_idx) in enumerate(feature_pairs):
    # 计算当前子图在3x2网格中的位置
    row = idx // 2  # 行索引 (0, 1, 2) - 整数除法确定行
    col = idx % 2  # 列索引 (0, 1) - 取模确定列
    ax = axes[row, col]  # 获取当前子图的坐标轴对象

    # 提取不同鸢尾花类别的数据点
    # 假设数据集前50条是setosa类别
    X_setosa = data_np[:50, x_idx]  # 当前特征组合的x坐标（setosa）
    Y_setosa = data_np[:50, y_idx]  # 当前特征组合的y坐标（setosa）

    # 中间50条是versicolor类别
    X_versicolor = data_np[50:100, x_idx]  # x坐标（versicolor）
    Y_versicolor = data_np[50:100, y_idx]  # y坐标（versicolor）

    # 最后50条是virginica类别
    X_virginica = data_np[100:, x_idx]  # x坐标（virginica）
    Y_virginica = data_np[100:, y_idx]  # y坐标（virginica）

    # 绘制散点图 - 使用不同的标记和颜色区分三类鸢尾花
    ax.scatter(X_setosa, Y_setosa, marker='x', c='b', label='山鸢尾(setosa)')  # setosa类别：蓝色叉号标记
    ax.scatter(X_versicolor, Y_versicolor, marker='o', c='r', label='变色鸢尾(versicolor)')  # versicolor类别：红色圆圈标记
    ax.scatter(X_virginica, Y_virginica, marker='*', c='g', label='维吉尼亚鸢尾(virginica)')  # virginica类别：绿色星号标记

    # 设置坐标轴标签
    ax.set_xlabel(feature_name[x_idx], fontsize=12)  # x轴标签为当前x特征名称
    ax.set_ylabel(feature_name[y_idx], fontsize=12)  # y轴标签为当前y特征名称

    ax.set_title(f'{feature_name[x_idx]} vs {feature_name[y_idx]}', fontsize=14)  # 设置子图标题，显示当前比较的两个特征
    ax.legend(loc='best')  # 添加图例，自动选择最佳位置
    ax.grid(True, linestyle='--', alpha=0.7)  # 添加网格线，使用虚线并设置透明度

# 调整子图布局，确保所有元素都能正确显示
# rect参数指定布局的矩形区域：[左, 下, 右, 上]（0-1之间），这里为总标题留出空间
plt.tight_layout(rect=[0, 0, 1, 0.96])

plt.show()
