 # -*- coding: utf-8 -*-
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

# TODO 3.boxplot（箱形图）
"""
箱形图的绘制方法在前面的范例中已经涉及，这里我们想利用Seaborn再次绘制箱形图，让各位读者从中感知Seaborn的优势。
下面我们依然以经典的Iris（鸢尾花）数据集为例，说明如何利用Seaborn绘制箱形图。
"""
# sns.set(style='ticks')
# iris = pd.read_csv("Iris-data.csv",header=None)
# iris.columns = ['Id','SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm','Species']
# sns.boxplot(x=iris["SepalLengthCm"],data=iris)
# plt.show()

"""
本例使用了Seaborn内置的方法boxplot()来绘制箱形图。
该方法的原型如下所示。该方法中的参数较多，我们挑选几个相对常用的给予简单介绍。
x：指定X轴的数据，若不设置，默认为None。
y：指定Y轴的数据，若不设置，默认为None。
hue：字符串类型，它是DataFrame中某个代表类别的列名，boxplot()方法会将这个列中包含的不同属性值作为分类依据，不同分类对应不同颜色的箱体，以示区分。
data：设置输入的数据集，可以是DataFrame对象，也可以是数组、数组列表等，是可选项。
palette：调色板，控制图形的色调。
order、hue_order：控制箱体的顺序。
orient：取值为v、h，用于控制图像是水平（horizontal）显示，还是垂直（vertical）显示。
"""
# plt.rcParams['font.sans-serif'] = ['SimHei']    # 设置中文显示
#
# # 读取 CSV 文件
# df = pd.read_csv("Iris-data.csv", header=None)
# df.columns = ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']
#
#
# df['SepalLengthCm'] = pd.to_numeric(df['SepalLengthCm'], errors='coerce')   # 强制转换 SepalLengthCm 为数值类型
# df = df.dropna(subset=['SepalLengthCm'])    # 删除无效行
# df['Species'] = df['Species'].astype('category')    # 确保 Species 是分类类型（可选）
#
# ax = sns.boxplot(x="Species", y="SepalLengthCm", data=df)   # 绘制箱线图
# medians = df.pivot_table(index="Species", values="SepalLengthCm", aggfunc="median").values  # 计算每组的中位数
#
# # 统计每个物种的数量
# nobs = df['Species'].value_counts().values
# nobs = [str(x) for x in nobs.tolist()]
# nobs = ["数量: " + i for i in nobs]
#
# pos = range(len(nobs))  # 设置标注位置
#
# # 在中位数线上方添加样本数量标注
# for tick, label in zip(pos, ax.get_xticklabels()):
#     ax.text(
#         pos[tick],  # x 坐标
#         medians[tick] + 0.03,  # y 坐标（中位数上方偏移 0.03）
#         nobs[tick],  # 显示的文本
#         horizontalalignment='center',
#         size='x-small',
#         color='w',
#         weight='semibold'
#     )
#
# # 显示图形
# plt.show()

"""
从数据导入的方式可以看出，Seaborn和Pandas做了很好的集成，例如代码直接返回了一个DataFrame对象。
我们可以按照操作DataFrame对象的方式来操作它。
在功能上，第10行代码和如下代码（即利用分组聚合方式）是等价的，选择哪一种方式，
就看你更喜欢哪种方式，但明显可以看出，利用透视表（pivot_table）能使代码更加具有可读性。
如果仅仅关注于把鸢尾花三个种类的箱形图绘制出来，那么代码到第07行就可以结束了。
第08行以后的代码，主要是为在中位数（50%处）横线上方显示每个子类的数量。
碰巧的是，在这个鸢尾花数据集里，每个子类的数量都是50，在其他数据集中自然不会是这个数值。
"""

# TODO 4.violin plot（小提琴图）
"""
小提琴图和箱形图有点类似，它也可以显示四分位数（quartile）。
不同于箱形图是通过长方形呈现的，以及绘图组件都对应实际的数据点，
小提琴图集合了箱形图和密度图的特征，主要用来显示数据的分布状态，它能很好地表征了连续变量数据的分布情况。
在外形上，因为所绘制的图形像一把把小提琴，故名“小提琴图”。
小提琴图是用于观察多个数据分布情况的有效媒介，相比于箱形图，它在视觉上更令人愉悦。
下面我们还是以熟悉的鸢尾花数据集为例，来说明小提琴图的绘制方法。
"""
# iris = pd.read_csv("Iris-data.csv")
# iris.columns = ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']
# print("数据集的列名：", iris.columns.tolist())
#
# # 强制转换 SepalLengthCm 为数值类型，并删除无效行
# iris['SepalLengthCm'] = pd.to_numeric(iris['SepalLengthCm'], errors='coerce')
# iris = iris.dropna(subset=['SepalLengthCm'])
#
# plt.figure(dpi=200)
#
# # 绘制小提琴图
# # 确保 x 参数与数据集中的列名一致（注意大小写）
# sns.violinplot(
#     x='Species',  # 如果数据集中的列名是 "Species"，则使用大写 S
#     y='SepalLengthCm',  # 列名应与数据集中的列名一致
#     data=iris,
#     scale='width',
#     inner='quartile'
# )
#
# # 设置标题并显示图形
# plt.title('Violin Plot', fontsize=12)
# plt.show()

"""
在小提琴图中，由于横线的宽度代表密度（就是这个值出现的频率），所以，我们可以很容易地观察到某个特征主要的密集分布区域。
形象点来说，横向越“胖”，这个值就出现得越频繁。
绘制小提琴图的方法是violinplot()，其原型如下。
该方法参数众多，大多都能见名知意。这里，我们挑选几个重要的参数介绍如下。
scale：可选参数，取值为area、count、width其中之一，主要用于调整小提琴图的缩放。
area表示每个小提琴图拥有相同的面域，count根据样本数量来调节宽度，width表示每个小提琴图拥有相同的宽度。
inner：可选参数，取值为box、quartile、point、stick、None其中之一，用于控制小提琴图内部数据点的形态。
box表示绘制微型小提琴图，quartiles表示显示四分位分布，point、stick表示绘制点或小竖条，None表示绘制朴素的小提琴图。
split：可选参数，布尔值，取值为True或False，表示是否将小提琴图从中间分开。
"""



# TODO 5.Density Plot（密度图）
"""
数据分析的重要目的之一在于，了解数据的基本性质，为后续的模型选择和模型训练提供依据。
了解特征的分布，通常是机器学习的第一步，同时也是相当关键的一步。
通常，我们会用核密度估计来掌握数据的基本分布情况。
类似于小提琴图，基于核密度估计的密度图（Density Plot），是一种常用的可视化图形。
这种密度图是将连续型随机变量分布情况可视化的利器。
在密度图中，分布曲线上的每一个点都表示概率密度，分布曲线下的每一块面积都是特定变量区间发生的概率。
下面，我们还是以鸢尾花数据集为例，说明三种不同品类鸢尾花的花瓣长度的概率密度分布。
"""
plt.rcParams['font.sans-serif'] = ['SimHei']

iris = pd.read_csv("Iris-data.csv")
iris.columns = ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']

# 强制转换 SepalLengthCm 为数值类型，并删除无效行
iris['SepalLengthCm'] = pd.to_numeric(iris['SepalLengthCm'], errors='coerce')
iris = iris.dropna(subset=['SepalLengthCm'])

# 绘制 Iris-versicolor 的花萼长度密度图
sns.kdeplot(iris.loc[iris['Species'] == 'Iris-versicolor', 'SepalLengthCm'],    # 筛选出物种为 Iris-versicolor 的花萼长度数据
            shade=True,                 # shade=True 表示填充密度曲线下的区域
            color="g",                  # color="g" 表示曲线和填充颜色为绿色
            label="Iris-versicolor",    # label="Iris-versicolor" 设置图例标签
            alpha=0.7                   # alpha=0.7 设置透明度为 0.7
            )
# 绘制 Iris-virginica 的花萼长度密度图
sns.kdeplot(iris.loc[iris['Species'] == 'Iris-virginica', 'SepalLengthCm'],
            shade=True,
            color="deeppink",
            label="Iris-virginica",
            alpha=0.7
            )
# 绘制 Iris-setosa 的花萼长度密度图
sns.kdeplot(iris.loc[iris['Species'] == 'Iris-setosa', 'SepalLengthCm'],
            shade=True,
            color="dodgerblue",
            label="Iris-setosa",
            alpha=0.7
            )

plt.title('鸢尾花花萼长度的密度图', fontsize=16)
plt.legend()    # 图例
plt.show()

"""
若要绘制密度图，需要用到Seaborn提供的一个专门方法kdeplot()，
和其他Seaborn提供的绘图方法类似，它有很多好用的参数，其方法的原型如下。

kdeplot(
    data,                # 输入的数据集（DataFrame 或类似数组的对象）
    data2=None,          # 可选的第二个数据集，用于绘制双变量核密度估计（如果需要）
    shade=False,         # 是否填充密度曲线下的区域（默认为 False，不填充）
    vertical=False,      # 是否垂直显示密度图（默认为 False，水平显示）
    kernel='gau',        # 核密度估计使用的核函数类型，'gau' 表示高斯核
    bw='scott',          # 带宽选择方法，'scott' 是 Scott's Rule 的带宽估计方法
    gridsize=100,        # 用于绘制密度图的网格点数（默认为 100）
    cut=3,               # 密度曲线绘制的截断参数，表示带宽的倍数（默认为 3）
    clip=None,           # 可选的元组，用于指定密度估计的裁剪范围
    legend=True,         # 是否显示图例（默认为 True）
    cumulative=False,    # 是否绘制累积分布函数（CDF，默认为 False）
    shade_lowest=True,   # 对于双变量图，是否填充最低密度区域（默认为 True）
    cbar=False,          # 是否显示颜色条（仅适用于双变量图，默认为 False）
    cbar_ax=None,        # 颜色条的子图位置（如果需要自定义）
    cbar_kws=None,       # 传递给颜色条的关键字参数（字典形式）
    ax=None,             # 指定的子图对象（如果需要在特定子图上绘制）
    **kwargs             # 其他传递给底层绘图函数的关键字参数
)

下面我们简单介绍几个常用的参数。
data、data2：这两个参数都用于指定绘图的数据源。如果除了X轴的数据，我们还想指定Y轴的数据，那么就要启用data2。
shade：指明密度曲线内是否填充阴影。对于本例的第11～13行，如果这个参数设置为False，即不需要填充阴影，那么运行结果将如图8-53所示。
vertical：布尔值，指定密度图的方向，默认为False（即非垂直显示）如果此值设置为True。
垂直显示的密度图很显然，不论是基础款的Matplotlib，还是进阶版的Seaborn，它们所能绘制的可视化图，远远不是一本小书所能覆盖的。
好在网络上有很多资源可供参考，这里推荐学有余力的读者参考《Matplotlib可视化最有价值的50个图表》，其中介绍的很多图形都非常美观。
"""
