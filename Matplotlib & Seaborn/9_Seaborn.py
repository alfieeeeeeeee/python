import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

"""
Seaborn是基于Matplotlib的数据可视化库。它在Matplotlib的基础上，进行了更高级的API封装，从而使得作图更加容易，不需要经过大量的调整，就能使图形变得精致。
有了Seaborn的加持，加之使用Pandas能方便地导入数据，我们能够更加高效地对数据进行可视化分析。
但需要说明的是，我们应该把Seaborn视为Matplotlib的补充，而不是替代物。
这就好比，Seaborn是“锦上添花”中的“花”，而Matplotlib才是“锦”。有了“花”，可以让“锦”更好看，但如果没有“锦”，“花”之不存。
Seaborn不仅可以配合Matplotlib来绘制更好的图形，事实上，它还可以与Pandas高效对接。
Seaborn所处理的数据类型大多基于Pandas中的数据结构—DataFrame。
这里我们只介绍几个常见的图形类型，如pairplot（对图）、heatmap（热力图）、boxplot（箱形图）、vilolinplot（小提琴图）、密度图和直方图。
"""

# TODO 1.pairplot（对图）
"""
pairplot（对图，亦有文献译作“矩阵图”）用于呈现数据集中不同特征数据两两成对比较（包括自己和自己对比）的结果。
对图是数据探索性分析中的常用工具，可用于呈现所有可能的数值变量对之间的关系。它基本是双变量分析的必备工具。
"""

# # 读取CSV数据文件
# iris = pd.read_csv('Iris-data.csv', header=None)    # 注意：header=None表示数据文件没有列标题
# iris.columns = ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']  # 为数据集添加列名
#
# # ====== 数据预处理开始 ======
# # 1. 指定需要转换为数值类型的列
# num_cols = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
#
# # 2. 将数值列转换为float类型
# #   - pd.to_numeric：将列转换为数值类型
# #   - errors='coerce'：将无法转换的值设为NaN（而不是抛出错误）
# iris[num_cols] = iris[num_cols].apply(pd.to_numeric, errors='coerce')
#
# # 3. 检查并处理缺失值
# #   - 打印每列缺失值数量，帮助诊断数据问题
# print("缺失值统计:")
# print(iris[num_cols].isnull().sum())
# #   - 删除包含缺失值的行
# iris.dropna(subset=num_cols, inplace=True)  # subset=num_cols：只检查数值列中的缺失值 inplace=True：直接在原数据框上修改
# # ====== 数据预处理结束 ======
#
# sns.set(style='ticks')  # 设置Seaborn绘图风格
#
# # 创建配对图(pair plot)
# g = sns.pairplot(
#     data=iris,          #   - data：使用的数据集
#     hue='Species',      #   - hue：按'Species'列分组着色
#     vars=num_cols,      #   - vars：指定要使用的数值变量列
#     diag_kind='kde',    #   - diag_kind='kde'：对角线显示核密度估计图
#     palette='muted'     #   - palette='muted'：使用柔和的调色板
# )
#
# plt.show()

# g.savefig('iris_pairplot.png', dpi=300, bbox_inches='tight')  # 可选：保存图形到文件（解决libpng警告）

"""
通过Seaborn，我们仅使用十行左右的代码就能绘制出非常美观的图形，
代码sns.set_style("ticks")用于设置图片的风格，与plt.style.use()作用相同。
Seaborn中预设好了五种主题风格：darkgrid、whitegrid、dark、white、ticks。
pairplot()函数内有很多参数，
我们挑选比较重要的介绍一下。第一个参数就是data，它表示绘制图形的数据源。
这里，我们利用Pandas读取数据，需要注意的是，读取的数据如果没有列名就要主动设置列名，
因为后面使用pairplot()函数时会以某一列为分类标准，从而给不同类别的图形上色。
第二个参数是hue，它用于从data中指定某个属性，据此区分不同的类别标签，从而对不同类别的图形上色。
在鸢尾花这个例子中，我们通过hue参数指定species为类别标签。
参数diag_kind用于指定对角线上图形的类别。因为在主对角线上，对于某一属性自身而言，自然无法画出如散点图之类的图形。
于是，我们有两种类型可选：频率分布直方图；核密度估计图。
另外一个参数是palette（调色板，即配色方案），我们可以选择不同的调色板来给图形上色。
通常，选择预设好的调色板就能满足我们的一般需求，预设好的调色板包括husl、pastel、muted、bright、deep、
colorblind、dark、hls、Paired、Set1、Set2、Blues、Greens、Reds、Purples、BuGn_r、GnBu_d、cubehelix等。
除了使用预设好的调色板，我们也可以自己制作调色板，详细的制作方法可以查阅Seaborn的官方文档。
"""

# TODO 2.heatmap(热力图)
"""
heatmap也就是热力图，主要用于描绘数据之间的相关程度。
下面，我们使用红酒等级数据集来说明热力图在特征选择中的作用。
我们知道，影响红酒等级的因素（即特征）非常多，给定数据集至少给出了13种影响红酒等级的因素，
如固定酸度、挥发酸度、柠檬酸、残糖、密度、pH值等。
在分类时，哪些特征对分类有明显影响呢？这时，热力图可为特征选择提供一臂之力。
"""
# plt.figure(figsize=(20,10), dpi=150)    # 设置绘图窗口的大小为20x10英寸，分辨率（dpi）为150，以确保图像清晰。
# wine = pd.read_csv('wine.csv')          # 使用pandas的read_csv函数读取名为'wine.csv'的CSV文件，并将数据存储在变量wine中。
# wine_corr = wine.corr()                 # 计算wine数据框中各列之间的相关系数矩阵，并将结果存储在wine_corr变量中。
# plt.figure(figsize=(20,10))             # 再次设置绘图窗口的大小为20x10英寸，这里可能是因为需要调整或确认绘图区域的尺寸。
#
# # 使用seaborn的heatmap函数绘制wine_corr的相关系数热力图。
# sns.heatmap(wine_corr,
#             annot=True,     # 参数annot=True表示在每个单元格中显示数值；
#             square=True,    # square=True确保每个单元格是正方形；
#             fmt='.2f'       # fmt='.2f'指定数值格式为保留两位小数的浮点数。
#             )
#
# plt.show()


"""
相关系数，其绝对值越大（要么正相关大，要么负相关大），两个变量之间的相关性越强，找到相关性，便容易进行预测，而预测是数据分析的核心本质。
反过来，相关系数的绝对值越接近于0，说明两个变量之间的相关性越小。
比如说，我们观察class（红酒等级）这一列，就会发现，class与Ash这个特征之间相关系数最小，仅为-0.05。
通过查看数据也发现，不同种类的红酒的Ash值并无太大变化。
这说明什么呢？在对红酒进行评级时，我们大可不必将Ash作为特征值。
此外，当特征比较多时，热力图体现了颜色的深度，我们一眼就可以看出，颜色越深，特征彼此间就越相关。
绘制热力图时，我们首先需要计算出数据集的相关系数矩阵，
通过Pandas中DataFrame对象自带的corr()方法很容易求出，
见第07行代码wine_corr=wine.corr()。
sns.heatmap()函数用来绘制热力图，annot是布尔类型参数，它是“annotate”（注释）的简写，默认为False。
当annot为True时，热力图中的每个方格内都会写入注释数据（即相关系数）。
square也是布尔类型参数，表示是否将输出的图形转化为正方形，默认输出长方形。
"""








