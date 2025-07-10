import numpy as np
import matplotlib.pyplot as plt
from pyparsing import alphas

"""
在数据可视化中，条形图（bar，又称柱状图）常用来展示和对比可测量数据。
bar()和barh()函数都可用于绘制一般的条形图。
其区别在于，bar()用于绘制垂直条形图，而barh中的“h”是英文“horizontal”（水平的）的简写，
因此，barh()函数只用于绘制水平条形图。
"""
# # TODO 1.垂直条形图
# objects = ['Python','Java','Scala','C','C++']
# y_ops = np.arange(len(objects))
# performance = [10,8,7,3,4]
#
# try:
#     plt.rcParams['font.sans-serif'] = ['SimHei']      # 设置Matplotlib使用支持中文的字体 黑体是常用的中文字体
#     plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示为方块的问题
# except:
#     plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimSun', 'FangSong']  # 如果SimHei不可用，尝试其他备选字体
#
# plt.bar(y_ops,performance,align='center',alpha=0.5)
# plt.xticks(y_ops,objects)
# plt.ylabel('用户量')
# plt.title('大数据开发语言使用情况')
# plt.show()

"""
绘制垂直条形图的核心方法是bar()，其原型如下所示。
left：X轴的位置序列，一般采用arange()函数产生一个序列。
height：Y轴的数值序列，也就是条形图的高度，一般就是我们需要显示的数据。
width：条形图的宽度，取值范围为0～1，默认为0.8（相对缩小）。
bottom：条形图的起始位置，也是Y轴的起始坐标。默认值为None（即以X轴作为起点），如果为叠状条形图，该值通常为次一级条形图的高度。
alpha：透明度，其取值范围为0～1。0为全透明，1为不透明。本例取值0.5，读者可根据情况自行调整。
color或facecolor：条形图填充的颜色。取值可以为rbg#123465等，默认为b。这里的b表示blue（蓝色）。如果是黑色的话，简写为k。
edgecolor：图形边缘的颜色。
Linewidth、linewidths或lw：图形边缘线的宽度。
tick_labe：设置每个刻度处的标签。
在本例中，一方面可以在bar参数中设置tick_label=objects。
另一方面，也可以单独设置，如本例第09行的plt.xticks(y_pos,objects)。二者功能相同。
label：标签，当有多个条形图并列时，可以区分不同条形图代表的含义。
"""

# TODO 2.水平条形图
# objects = ['Python','Java','Scala','C','C++']
# y_ops = np.arange(len(objects))
# performance = [10,8,7,3,4]
#
# try:
#     plt.rcParams['font.sans-serif'] = ['SimHei']      # 设置Matplotlib使用支持中文的字体 黑体是常用的中文字体
#     plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示为方块的问题
# except:
#     plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimSun', 'FangSong']  # 如果SimHei不可用，尝试其他备选字体
#
# plt.barh(y_ops,performance,align='center',alpha=0.5,color='k',tick_label=objects)
# plt.xlabel('用户量')
# plt.title('大数据开发语言使用情况')
# plt.show()

# TODO 3.并列条形图
# # 设置中文字体，以便正常显示中文标签
# plt.rcParams['font.sans-serif'] = ['SimHei']
#
# n_groups = 4  # 定义组数，即课程的数量
# means_frank = (90, 55, 40, 65)  # 张三在各课程上的分数
# means_guido = (85, 62, 54, 20)  # 李四在各课程上的分数
#
# # 创建图形和坐标轴对象
# fig, ax = plt.subplots()
# index = np.arange(n_groups)  # 生成一个从0到n_groups-1的数组，作为条形图的x轴位置
# bar_width = 0.35  # 条形图的宽度
# opacity = 0.8  # 条形图的透明度
#
# # 绘制第一个条形图（张三的分数）
# rects1 = plt.bar(index,  # 定义第一个条形图的X轴坐标信息
#                  means_frank,  # 定义第一个条形图的Y轴坐标信息，即张三的分数
#                  bar_width,  # 定义图形的宽度
#                  alpha=opacity,  # 定义图形的透明度
#                  color='b',  # 定义图形颜色为蓝色
#                  label='张三')  # 定义图形的标签信息，用于图例
#
# # 绘制第二个条形图（李四的分数）
# rects2 = plt.bar(index + bar_width,  # 与第一个条形图在X轴上无缝“肩并肩”，通过偏移实现
#                  means_guido,  # 定义第二个条形图的Y轴坐标信息，即李四的分数
#                  bar_width,  # 定义图形的宽度
#                  alpha=opacity,  # 定义图形的透明度
#                  color='g',  # 定义第二个图形颜色为绿色
#                  label='李四')  # 定义第二个图形的标签信息，用于图例
#
# # 设置图形的标签和标题
# plt.xlabel('课程')  # 设置x轴标签
# plt.ylabel('分数')  # 设置y轴标签
# plt.title('分数对比图')  # 设置图形标题
# plt.xticks(index + bar_width, ('A', 'B', 'C', 'D'))  # 将x轴刻度设置为课程名称，并居中显示
# plt.legend()  # 显示图形的标签信息，即图例
# plt.show()  # 展示绘制好的图形

"""
在本质上，垂直并列条形图就是在X轴上分别画两组并列的条形图，但二者在X轴的位置上有先后关系。
举例来说，第一个条形图。请注意，实际上代码是一行语句，不过是为了注释方便，将不同的参数放置于不同的行罢了。
第二个条形图。值得注意的是，在细节处理上，它的X轴坐标的向右偏移量正好等于第一个条形图的宽度，
通过X轴上的偏移操作index+bar_width，第二个条形图能与第一个条形图在X轴上无缝“肩并肩”。
为了区分两组条形图，用label属性来区分不同图形的标签。
我们知道，即使不同的条形图使用了不同颜色加以区分，但有时效果也欠佳。
这是因为，在彩色的电子显示设备中，这些多彩图形清晰可分，但当黑白打印时，颜色往往难以区分。
因此，在科技论文写作中，常常使用不同纹理而非不同颜色来区分不同的条形图。
这时，就需要使用条形图的hatch（填充）参数了。
"""

# TODO 4.垂直并列条形图
# 用于绘制图形的数据
# n_groups = 4
# means_frank = (90, 55, 40, 65)
# means_guido = (85, 62, 54, 20)
#
# fig, ax = plt.subplots()  # 创建图形
# index = np.arange(n_groups) # 定义条形图在横坐标上的分类位置
# bar_width = 0.35
# opacity = 0.8
#
# # 绘制第一个条形图
# rects1 = plt.bar(index,                # 定义第一个条形图的 X 轴坐标信息
#                  means_frank,          # 定义第一个条形图的 Y 轴坐标信息
#                  bar_width,            # 定义条形图的宽度
#                  alpha=opacity,        # 定义图形的透明度
#                  color="w", edgecolor="k",
#                  hatch='.....',
#                  label='张三')         # 定义第一个条形图的标签信息
#
# # 绘制第二个条形图
# rects2 = plt.bar(index + bar_width,
#                  means_guido,
#                  bar_width,
#                  alpha=opacity,
#                  color="w", edgecolor="k",
#                  hatch='\\\\\\',
#                  label='李四')         # 定义第二个图形的标签信息
# plt.xlabel('课程')
# plt.ylabel('分数')
# plt.title('分数对比图')
# plt.xticks(index + bar_width,('A','B','C','D')) # 设置x刻度位置和标签
# plt.legend()
# plt.show()

"""
本例的绘图关键在于，首先要将图形的填充色设置为白色：color="w"。同时把图形的边界颜色设置为黑色：edgecolor="k"。
最后我们再设置图形的纹理。参数hatch可用来设置填充的纹理类型，其可取值为/、\、|、-、+、x、o、O、.、*。
这些符号表示图形中填充的符号，大多都能“见号知意”。
这里有一个小技巧，即你使用的填充单一符号越多，图形中对应的纹理就越密集，
例如，通过hatch='.....'绘制的图形就比通过hatch='..'绘制的图形纹理更密集，这个填充符号表示图形里面填充的都是点（.）。
同理，第32行的hatch='\\\\'，就比hatch='\\'纹理密集，这里表示填充的是反斜线。
最后需要说明的是，注意转义字符的干扰。如果我们在第32行的字符串前添加一个字符r，即变为hatch=r'\\\\'
"""

# TODO 4.叠加条形图
# 用于绘制图形的数据
# n_groups = 4
# means_frank = (90, 55, 40, 65)
# means_guido = (85, 62, 54, 20)
#
# fig, ax = plt.subplots()    # 创建图形
# index = np.arange(n_groups) # 定义条形图在横坐标上的分类位置
# bar_width = 0.35
# opacity = 0.8
#
# # 绘制第一个条形图
# rects1 = plt.bar(index,                # 定义第一个条形图的 X 轴坐标信息
#                  means_frank,          # 定义第一个条形图的 Y 轴坐标信息
#                  bar_width,            # 定义图形的宽度
#                  alpha=opacity,        # 定义图形的透明度
#                  color="w", edgecolor="k",
#                  hatch='.....',
#                  label='张三')
# # 绘制第二个条形图
# rects2 = plt.bar(index,
#                  means_guido,
#                  bar_width,
#                  bottom = means_frank,  # 设置条形的底部位置，这里将张三的分数数据作为底部，实现堆叠效果
#                  alpha = opacity,
#                  color="w", edgecolor="k",
#                  hatch=r'\\\\',
#                  label = '李四')
#
# plt.xlabel('课程')
# plt.ylabel('分数')
# plt.title('分数对比图')
# plt.xticks(index, ('A', 'B', 'C', 'D'))
# plt.legend()
# plt.show()

"""
在本例中，成功绘图的关键有两点：
首先，第一个条形图和第二个条形图的X轴坐标是一样的；
其次，第二个条形图的Y轴坐标是站在第一个肩膀上的，第31行代码的含义是说，第二个条形图是以第一个为底（bottom）的。于是，顺理成章地，如果我们还有第三个条形图需要叠加的话，它的起点是第二个条形图的顶点，以此类推。
"""

# TODO 5.直方图
"""
如前所述，条形图一般用来描述顺序数据，其中的各个长条形之间留有空隙，以区分不同的类别，
不同的类别之间没有必然的先后关系，调整彼此的顺序，并不会影响数据的可视化表达。
对比而言，直方图（Histogram）则像一种统计报告图。在外观上，它也由一个个的长条形构成，
但直方图在宽度（即X轴）方向将样本的取值范围从小到大划分为若干个间隔（bin），这个间隔越大，表明涵盖的属性值跨度就越大（换句话说，间隔并不必须是等分的）
。在高度（即Y轴）方向，直方图可表示特定间隔区间样本出现的次数（即频数），长条形越高，表明此间隔内的样本越多。
换句话说，直方图的宽度和高度均有意义，特别是在宽度方向，“尊卑有序”，不可随意调整顺序。
“Histogram”一词源自希腊语，前缀histos表示“竖立”（如船的桅杆），词根gramma则表示“描绘”。
该术语由英国统计学家卡尔·皮尔逊（Karl Pearson）于1895年发明并提出。
为了构建直方图，第一步是将样本在某个特定属性的取值范围内进行分段，形成一系列间隔，
然后计算每个间隔中有多少个样本。
"""
# mu = 100
# sigma = 15
# x = mu+sigma * np.random.randn(200)
# num_bins = 25
# plt.figure(figsize=(9,6),dpi=100)
#
# # 绘制直方图
# # 使用 plt.hist 函数绘制直方图，返回三个对象：n（每个柱的频数）、bins（柱的边界值）、patches（柱的图形对象）
# n, bins, patches = plt.hist(x, num_bins,
#                             color="w",  # 设置柱的填充颜色为白色
#                             edgecolor="k",  # 设置柱的边框颜色为黑色
#                             hatch=r'ooo',  # 设置柱的纹理为'ooo'
#                             density=1,  # 将直方图归一化，使其表示概率密度（面积和为1）
#                             label='频率')  # 设置直方图的标签，用于图例显示
#
# # 计算正态分布的概率密度函数值
# # 根据正态分布公式：f(x) = (1 / (σ * √(2π))) * exp(-0.5 * ((x - μ) / σ) ** 2)
# # 这里使用给定的均值 mu 和标准差 sigma，以及直方图的柱边界值 bins 来计算概率密度
# y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
#
# plt.plot(bins, y, '--', label='概率密度函数') # 绘制概率密度函数曲线 使用 plt.plot 函数绘制曲线，线条样式为虚线，并设置标签用于图例显示
# plt.xlabel('聪明度') # 设置 x 轴标签为“聪明度”
# plt.ylabel('概率密度') # 设置 y 轴标签为“概率密度”
# plt.title('IQ 直方图:$\mu=100$,$\sigma=15$')   # 设置图形标题，显示均值和标准差
#
# plt.legend()    # 显示图例，根据之前设置的 label 参数显示对应的标签
# plt.show()

"""
x：指定要在X轴上绘制直方图所需的数据；在形式上，它可以是一个数组，也可以是数组序列。如果是数组序列，数组的长度不需要相同。
bins：指定直方图条形的个数。如果此处的值为整数，就会产生bins+1个分割边界，此时该方法就等价于numpy.histogram，默认值为10，即将属性值10等分。
如果该值是一个序列，则可构建一个非分等的间隔序列，如取值为[1, 3, 4, 6]，表示第一个间隔区间是[1,3)，
请注意此时区间范围为左闭右开，即第一个分割区间不包括上界3。
类似地，第二个间隔区间是[3,4)。但是最后一个间隔由于没有下一个间隔来“接盘”，所以是完全的闭区间，即[4,6]。
range：设置直方图数据的显示上、下界，边界之外的数据将被舍弃。默认为None，即不设置边界，包含所有数据。
density：可选项，是一个布尔值，用于设置是否进行归一化处理。如果为True，返回元组的第一个元素并将把计数标准化为一个概率密度，也就是说，直方图下的面积（或积分）总和为1。
weights：为每一个数据点设置权重。
cumulative：表明是否需要计算累计频数或频率。
bottom：为直方图的每个条形添加基准线，默认为0。
histtype：指明直方图的类型，可选bar、barstacked、step、stepfilled中的一种，默认为bar，即条形图。
align：设置条形边界的对齐方式，默认为mid，除此之外还有left和right。
normed：表明是否将得到的直方图向量归一化，布尔类型，默认为False。
orientation：指明直方图中条形的呈现方向，要么水平，要么垂直。因此可选值为horizontal、vertical，默认值为垂直方向（horizontal）。
rwidth：设置直方图各条形宽度的百分比，默认是0。
log：指明是否需要对绘图数据进行对数（log）变换。
color：设置直方图的填充色。
label：设置直方图的标签，可展示图例。
stacked：指明当有多个数据时，是否需要将直方图呈堆叠摆放，默认设置是水平摆放。
normed：指明是否将直方图的频数转换成频率（已弃用，被density替代）。

下面我们再来看一下hist()函数的返回值，分别如下。
n：直方图每个间隔内的样本数量，数据形式为数组或数组列表。
bins：返回直方图中各个条形（分组）的区间范围，数据形式为数组。
patches：返回直方图中各个间隔的相关信息（如颜色、透明度、高度、角度等），数据形式为列表或列表的列表（即嵌套列表，相当于多维数组）。
"""

x = np.random.normal(0, 1, 5000)  # 生成符合正态分布的5000个随机样本
plt.figure(figsize=(14, 7))  # 设置图片大小为14×7英寸
plt.style.use('seaborn-whitegrid')  # 设置绘图风格为seaborn-whitegrid

n,bins,patches = plt.hist(x,bins=90,facecolor='#2ab0ff',edgecolor='#169acf',linewidth=0.5)  # 绘制直方图，设置柱的填充颜色、边框颜色和线宽
n = n.astype('int')  # 将频数n转换为整型，因为返回值n必须是整型

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为SimHei（黑体），以支持中文显示
plt.rcParams['axes.unicode_minus'] = False  # 显示负号'-'，解决坐标轴负号显示问题

# 为每个条形设置颜色
for i in range(len(patches)):
    patches[i].set_facecolor(plt.cm.viridis(n[i] / max(n)))  # 根据频数的相对大小，使用viridis颜色映射设置条形颜色

# 对某个特定条形（如第49个）做特别说明
patches[49].set_fc('red')  # 设置第49个条形的颜色为红色
patches[49].set_alpha(1)  # 设置第49个条形的透明度为不透明

# 添加注释
plt.annotate('这是一个重要条形！', xy=(0.6, 155), xytext=(1.5, 130),
             fontsize=15, arrowprops={'width': 0.4, 'headwidth': 5, 'color': '#333333'})  # 在图形上添加注释，指定注释位置、文本位置、字体大小和箭头属性

# 设置X轴和Y轴的标题、字体
plt.title('正态分布', fontsize=12)  # 设置图形标题为“正态分布”，字体大小为12
plt.xlabel('不同的间隔（bins）', fontsize=10)  # 设置x轴标签为“不同的间隔（bins）”，字体大小为10
plt.ylabel('频度大小', fontsize=10)  # 设置y轴标签为“频度大小”，字体大小为10

plt.show()  # 显示绘制好的图形

"""
在本例中，我们利用NumPy生成了5000个服从正态分布的随机样本点（第03行），然后通过直方图来可视化它们的分布。
第06行除了绘制普通的直方图，更重要的是返回了是三个参数。
本例中的关键之处在于，不同的patch参数代表不同间隔（bin）的构造信息，
第13～14行为每个patch设置了不同的前置色。
第16～17行为特定的patch设置了填充色和透明度。
第19行是一个绘图小技巧，即利用annotate()方法在图形上给数据添加文本注解，以方便我们在合适的位置添加描述信息。
"""
