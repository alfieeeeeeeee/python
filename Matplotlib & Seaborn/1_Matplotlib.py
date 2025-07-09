import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import lineStyles

"""
Python中有很多第三方数据可视化工具包，如Matplotlib、Seaborn等就是其中的佼佼者。
它们的出现，大大降低了人们对数据分析的理解难度。
在本章中，我们将主要介绍Matplotlib和Seaborn的基本用法。
本章要点（对于已掌握的内容，请在对应的方框中打钩）
□掌握Matplotlib绘图工具的使用方法
□掌握Seaborn的使用方法
□了解可视化在特征选择中的作用

Matplotlib是一款功能强大的数据可视化工具。它与NumPy的无缝集成，使得Python拥有与MATLAB、R等语言“叫板”的实力。
通过使用plot()、bar()、hist()和pie()等函数，Matplotlib可以很方便地绘制散点图、条形图、直方图及饼图等专业图形。
但客观来讲，Matplotlib也有不足。比如说，它绘制的图形还不够细腻，或者说比较底层，如果你想绘制一个相对高级的图形，需要花费较大的精力进行微调和美化。
有需求，自然就会有开发的动力。于是，人们对Matplotlib进行了二次封装，开发出了更为高阶的Seaborn绘图库，使绘制的图形更加细腻，也显得更加“高大上”。
在某些场合，可用Seaborn来替代Matplotlib绘制更为惊艳的图形。
"""
# TODO 1.示例
# 生成正弦曲线
# nbSample = 256 # nbSample 控制着你绘制正弦曲线时使用的数据点数量。 数值越大，曲线越平滑； 数值越小，曲线越粗糙（看起来像折线）。
# xRange = (-math.pi,math.pi)  # X轴的取值区间[-π，π]
# x,y = [],[]
#
# for i in range(nbSample):
#     radio = (i+0.5)/nbSample
#     x.append(xRange[0] + (xRange[1] - xRange[0]) * radio)
#     y.append(math.sin(x[-1]))   # 将列表x中最后一个数据作为sin()函数的值，求出y
#
# plt.plot(x,y)
# plt.show()

"""
第01行导入了math模块，这是因为我们要用到该模块中的sin()函数。
第02行导入了Matplotlib绘图库，并取别名为plt。
第07行创建了两个空列表x和y，
第09～12行的for循环通过追加（append）模式来填充列表x和y，它们分别作为X轴和Y轴的数据。
列表x、y的构造很费劲。需要先算出每个元素在整个数据集合中的比例系数ratio（第10行），
然后根据这个比例系数算出该元素在+π和-π之间的相对位置（第11行），这里的π用math.pi表示。
最后，将列表x中最后一个数据（即最新的数据）作为sin()函数的参数值，求出对应的sin(x)值，并逐个将它们追加到x和y列表中。
实际上，绘图的代码只有一行（第15行），即plt.plot(x,y)。
这是一个通用命令，在理论上，该命令可接受任意数量的参数。其中x为数据点的横坐标，y为数据点的纵坐标。
x和y可以是列表，也可以是数组，但二者的长度要保持一致，否则难以搭配形成绘图坐标。
当然，只有第15行代码也是不够的，图片绘制成功后，如果我们想在屏幕上看到它，还需要通过plt.show()函数来显示绘制的图形（第16行）。
"""

"""
如前所述，对充当X轴和Y轴数据集的两个列表x和y，其构造过程太过于低效。好在“他山之石，可以攻玉”，
在前面的章节中，我们已经学习过高效的数值计算包NumPy。
因此，完全可用NumPy来高效构造所需数据。下面我们结合NumPy对范例进行局部修改。
"""


# nbSample = 256
# x = np.linspace(-math.pi, math.pi, num=256)
# y = np.sin(x)
#
# plt.plot(x, y)
# plt.show()

"""
可以看到，使用NumPy后，数据构造变得十分简单。
代码第07行使用了NumPy的内置方法linspace(linspace(start, stop, num=50)，它能批量生成指定区间[start, stop)内的数量为num的均匀间隔的数组向量x。
默认情况下，上限stop是无法取到的。不过linspace提供了第三个参数endpoint，这是一个布尔变量，如果它取值为True，则可以取到stop，如果为False，则无法取到stop。
第08行使用了NumPy中的方法sin()。对于NumPy而言，它有一个重要的属性，那就是“向量进，向量出”。
由于第07行构造的x为一个向量（你可以理解为具有相同数据类型的一批数据），所以sin(x)会批量产出一个相同维度的向量数组y，两个向量中的元素一一对应。
这种“向量进，向量出”的编程模式，就是向量化编程。
向量化编程是一种能够消除代码中for循环的编程艺术，它在机器学习（如神经网络训练）领域被广泛应用。
由以上分析可知，如果我们能得心应手地利用NumPy，就能大大提高代码编写效率。上面我们只是简单说明如何使用plot()函数来绘制一条简单的曲线。
事实上，我们也可以在plot()函数中指定线条的属性，通过color、linewidth、linestyle参数来指定线条颜色、宽度、形状，
还可以选择通过marker、markerfacecolor、markersize参数对标记点的形状、颜色、大小进行指定。
"""

# 修改图形中线条的属性（curve_attrs.py）
# nbSample1 = 128
# x = np.linspace(-np.pi, np.pi, nbSample1)
# y1 = np.sin(x)
# y2 = np.cos(x)
#
# plt.plot(x, y1, color='g', linewidth=4, linestyle='--')
# plt.plot(x, y2, markersize=8, markerfacecolor='r', markeredgecolor='k')
# plt.show()

"""
首先，我们在一个画布中画出了两条曲线。其实现过程并不复杂，只需配置不同的数据源，然后两次调用plot()函数即可。
为了区分，还需要指定不同的颜色、线条样式等。
比如，在第09行代码中，我们将正弦函数曲线的线条颜色（color）修改成绿色（参数g是green的简写），
将线条宽度（linewidth）设置为4，将线条样式（linestyle）由原来的实线改成了虚线。
一个字母可表示常用颜色，单字母表示的常用颜色。
同时，我们还修改了标记点（marker）的大小（markersize）、填充色（markerfacecolor）和边线颜色（markeredgecolor）。
plot()中的linestyle参数可以简化一系列由字符串构成的标识，
对于'[color][marker] [linestyle]'而言，'g^-'就等价于color='g', marker='^', ls='-'。
第10行代码所示的plt.plot(x,y2, '*')用到了部分简化模式。
当我们不指定color、linestyle时，plot()函数会为我们自动匹配。
"""

# TODO 2. pyplot的高级功能
"""
在某些情况下，我们需要将不同曲线放置在同一个坐标系下，以方便对照。
为区分不同曲线代表的含义，增强图形的可读性，就需要给不同的曲线设置不同的标记、颜色、宽度等，并添加图例（Legend）来区分它们，
"""
# nbSample2 = 128
# x = np.linspace(-np.pi,np.pi,nbSample2)
# y1 = np.sin(x)
# y2 = np.cos(x)
# plt.plot(x,y1,color= 'g',linewidth=4,linestyle='--',label=r'$y=sin(x)$')
# plt.plot(x,y2,linestyle='-.',markersize=8,markerfacecolor='r',markeredgecolor='k',label='$y=cos(x)$')
# plt.legend(loc='best')
# plt.show()

"""
本例仅在基础上做了简单的修改。
首先，在第09和第11行为曲线添加了标签属性，
然后在第16行，通过设置plt.legend(loc='best')使图例能够在画布的“最佳”位置显示，
这里的“最佳”是由系统自动判别的，通常哪里留白较多，系统就将图例放到哪里，
loc参数是location（位置）的简写，表示图例所在位置，通常默认为最佳位置。
当然，我们也可以自行指定图例位置，可供选择的参数有upper right（右上）、upper left（左上）、lower left（左下）、
lower right（右下）、right（右边）、center left（左中）、center right（右中）、lower center（中下）、upper center（中上）、center（中）等。
值得注意的是，Matplotlib在绘图的过程中，可以为各个轴的标题（Label）、图像的标题（Title）、图形的图例（Legend）等元素添加LaTeX风格的公式。
添加公式并不复杂，只要在LaTeX公式的文本前后各增加一个$符号，Matplotlib就可以自动进行解析。
如代码第9行和第11行所示，公式前面通常添加字母r，它是raw（原始的）的首字母，表示后面的字符串（即LaTeX公式）以原始字符形式存在，不需要进行转义解析。
例如，字符串r'\n'就表示两个字符，一个是“\”另一个是“n”。如果去掉字符串前面的标识r，'\n'就被解析为一个字符，即换行符。
"""

"""
在机器学习中，在图上显示出点的坐标也是十分重要的，例如在k均值聚类算法中，将聚类中心点的坐标显示出来更有利于对数据进行分析。
下面，我们举一个简单的例子来说明如何显示坐标点，
"""
# x = np.arange(1,10,1)   # 构造x轴坐标向量
# y = x * 2               # 构造y轴坐标向量
#
# for a,b in zip(x,y):
#     plt.text(a,b,(a,b),ha = 'center',va = 'bottom',fontsize = 10)
#
# plt.plot(x,y,'bo-')
# plt.show()

"""
在本例中，我们使用plt.text()函数给图形添加了文本注释，借此把点的坐标逐个标注到了图形当中。
在第08行代码中，plt.text(a,b,(a,b),ha='center', va='bottom', fontsize=10)的
前两个参数表示要标注的X轴和Y轴的坐标位置。第三个参数表示标注的文本内容，我们在这里打算显示的是坐标点。
我们可以看到，坐标点文本压在所绘制的曲线上，如果想优化显示文本的位置，我们可以调整前两个参数的位置。
例如，plt.text(a- 0.5,b,(a,b))就表示把文本的X坐标左移0.5个单位。
ha、va分别是horizontal alignment（水平对齐）、vertical alignment（垂直对齐）的简写。
ha可选的参数有'center'、'right'、'left'，
va可选的参数有'center'、'top'、'bottom'、'baseline'、'center_baseline'。
可根据自己的需要，选择合适的参数。
"""

"""
在某些情况下，我们需要给图形设置一个标题，修改坐标轴的刻度值，或关闭坐标轴显示等。
这时，我们可以使用plt.title()函数来给图形设置标题，
使用plt.xticks()函数设置X轴的刻度值，使用plt.yticks()函数设置Y轴刻度值，
使用plt.xlim()函数、plt.ylim()函数分别设置X轴和Y轴的区间范围，
使用plt.xlabel()函数、plt.ylabel()函数设置X轴和Y轴的名称。
"""

# x = np.arange(-5, 5, 0.05) # 生成 x 轴数据：从 -5 到 5，步长为 0.05
# y1 = np.sin(x)  # 计算 y1 值：y1 = sin(x)
# y2 = np.cos(x) # 计算 y2 值：y2 = cos(x)
#
# plt.rcParams['font.sans-serif'] = ['SimHei'] # 设置中文字体为黑体（SimHei），避免中文显示乱码
# plt.title('双曲线') # 设置图像标题为“双曲线”
#
# plt.ylim(-1.2, 1.2)  # 设置 y 轴的显示范围为 [-1.2, 1.2]
# plt.xlim(-6, 6) # 设置 x 轴的显示范围为 [-6, 6]
#
# # 设置 x 轴刻度的位置和标签：
# # 刻度位置从 -1.5π 到 2π，每隔 0.5π 一个刻度
# # 标签使用 LaTeX 风格的数学符号表示 π 的倍数
# plt.xticks(
#     ticks=np.arange(-1.5 * np.pi, 2 * np.pi, 0.5 * np.pi),
#     labels=[
#         '$-\\frac{3}{2}\pi$',  # -3/2 π
#         '$-\pi$',              # -π
#         '$-\\frac{1}{2}\pi$',  # -1/2 π
#         '0',                   # 0
#         '$\\frac{1}{2}\pi$',   # 1/2 π
#         '$\pi$',               # π
#         '$\\frac{3}{2}\pi$'    # 3/2 π
#     ]
# )
# plt.yticks(ticks=[-1, 0, 1])  # 设置 y 轴刻度
#
# plt.xlabel('我是$X$轴') # 设置 x 轴标签为“我是 X 轴”，并用 LaTeX 显示变量 X
# plt.ylabel('我是$Y$轴') # 设置 y 轴标签为“我是 Y 轴”，并用 LaTeX 显示变量 Y
#
# plt.plot(x, y1, 'r-', label='$y_1=\sin(x)$') # 绘制第一条曲线：红色实线，表示 y1 = sin(x)，图例为 y1=sin(x)
# plt.plot(x, y2, 'b:', label='$y_2=\cos(x)$') # 绘制第二条曲线：蓝色点线，表示 y2 = cos(x)，图例为 y2=cos(x)
#
# plt.legend(loc='best') # 显示图例（legend），loc='best' 表示自动选择最佳位置
# plt.show() # 显示图像

"""
Matplotlib功能很强大，但对中文支持不够友好。如果不指定具体的中文字体，凡是涉及中文文本的地方，都可能出现乱码。
在Windows平台下，我们可以在每次编写代码时设置如下参数，正确显示中文.
在中文字体设置中，'SimHei'表示简体（Simple）黑体（Hei），当然你也可以设置其他中文字体，但前提是Matplotlib能找到你所指定的字体。
如果想一劳永逸解决这个问题，就要修改Matplotlib的配置文件，请参考本章后面的思考与提高部分。
然后，在代码第12行，我们使用plt.xlim()设置X轴的坐标范围为(-6, 6)。这里xlim表示X轴的限度（limit）。
类似地，ylim表示Y轴的限度（limit）。代码第13行使用plt.ylim()设置Y坐标轴范围为(-1.2, 1.2)。
接着，使用plt.xlabel()设置X坐标轴名称'我是X轴'，使用plt.ylabel设置Y坐标轴名称'我是Y轴'。
我们使用plt.xticks()（代码第14行～16行）设置X轴的刻度，使用plt.yticks()（代码17行）设置Y轴的刻度。
xticks()、yticks()函数分别用于设置X轴和Y轴的刻度与标签。这两个函数都有相同的参数ticks和labels。
其中ticks用于设置坐标轴的刻度值，labels用于设置坐标轴的标签值，标签中可以添加LaTeX公式。
"""

"""
在范例中，我们调用了两次plot()方法，从而实现了在一张画布中绘制两条曲线的目的。
实际上，只要给足绘图所需的信息，调用一次plot()即可绘制多条曲线
"""
# data = np.arange(0,4,0.2)

# plt.plot(data,data,'r-.',data,data**2,'bs',data,data**3,'g^')

# 有时候，为了便于比较，我们可能需要利用图形中的网格线来辅助定位图像的大致坐标位置，这时就需要利用grid()方法。添加一行代码即可添加网格线.
# plt.grid(True)

"""
grid()方法的参数解释如下。
b：布尔类型变量，取值为[True | False]，表示是否为图形添加网格，默认为False，即不添加。 matplotlib3.1时已更新，不需要b参数，直接写True即可。
which：取值为['major' | 'minor' | 'both']，表示使用大网格（'major'）或小网格（'minor'），或大网格里套小网格（'both'），默认为'major'。
axis：取值为['both' | 'x' | 'y']，表示在哪个轴添加网格线，可以是X轴、Y轴，或X轴和Y轴均添加，默认为'both'，即X轴和Y轴均添加网格线。
"""
# plt.savefig('mult_lines.png',dpi=600)



"""
在本例中有两个小技巧值得借鉴。第一个小技巧就是前面所说的，
我们可以一次性地绘制多条曲线，如代码第08代码按照顺序先后提供了三条线段的X轴数据、Y轴数据和线条样式，实际上实现了y=x、y=x2和y=x3这三条曲线的绘制。
为了区分这三条曲线，要让它们在样式上有所不同，例如第一条曲线的参数是“r-.”，其中“r”表示红色（red），“-.”是非常形象的点画线。
显而易见的是，“--”表现虚线，读者可自行测试一下。
第二条曲线的样式是“bs”，其中“b”表示的是颜色blue（蓝色），“s”表示图形为方形（square）。
第三条曲线的原始设置是“g^”，其中“g”表示的是颜色green（绿色），第二个字符“^”表示图形是“三角形”，看这个字符“^”外形，是不是也很形象？
其实，Matplotlib的标记远不止这些，更多详情可以访问官方文档。

第二个值得关注的小技巧是，如果我们不想在屏幕显示图形，而是想将显示结果另存为一张图片以备后用，就可以使用savefig()方法。
在该方法中填写对应的存储路径和文件名（包括扩展名）即可。这个方法神奇的地方在于，它会根据文件名的扩展名不同，自动识别图片并将其存储为对应的格式。
例如，如果你利用LaTeX撰写学术论文，可能会对eps格式的这类矢量图情有独钟，这时你可以把第09行代码修改如下。
当然，你也可以根据需要将图片保存为jpg、pdf、svg等格式。
在第09行代码中，参数dpi=600并不是必需的。
只有当你觉得生成图片的分辨率“惨不目睹”时，设置这个参数才有必要，可以提高分辨率。
这里dpi表示的含义是Dots Per Inch（每英寸点数，简称DPI），它是一个量度单位，用于衡量生成图片的每英寸像素数量。
通常，DPI越大，图片的清晰度也就越高，但占据的比特数也越高，不利于网络传输，所以有时候我们为了网络传输质量和传输速度，会对DPI的大小做一个合理的权衡。
"""

"""
在前面的讨论中，每次我们都绘制一张图片，实际上，有时候我们需要将多个子图绘制在一起进行比较。
这时需要利用绘制子图的方法subplot()，其函数原型大致如下。
上述方法的功能为，绘制nrows行ncols列第plot_number个子图。显然，在这种布局下，我们一共有nrows×ncols个子图，参数plot_number指明是第几个子图。
例如subplot(2, 1, 1)表示两行一列（共上下结构两个子图）第一个子图。
如果以上参数的值都小于10，则可以连写在一起。例如前面的写法可简化为subplot(211)。
"""

# def f(t):
#     return np.exp(-t) * np.cos(2 * np.pi * t)  # 这是一个数学函数，表示阻尼振荡器的输出，即随着时间衰减的余弦波：
#
# t1 = np.arange(0.0,5.0,0.1)
# t2 = np.arange(0.0,5.0,0.02)
#
# # 创建一个包含 2 行 1 列 子图的画布  axes: 包含两个 Axes 对象的数组，分别对应两个子图。
# fig, axes = plt.subplots(2, 1, figsize=(8, 6))  # 指定整个画布（包含所有子图的窗口）的大小为宽8英寸、高6英寸。
#
# # 第一个子图
# axes[0].plot(t1, f(t1), 'bo', t2, f(t2), 'k')  # 用蓝色圆圈 'bo' 画出稀疏的采样点。 用黑色实线 'k' 画出更平滑的曲线。
# axes[0].set_title('Damped Oscillation')
# axes[0].grid(True)
#
# # 第二个子图
# axes[1].plot(t2, np.cos(2 * np.pi * t2), 'r--')
# axes[1].set_title('Cosine Wave')
# axes[1].grid(True)
#
# # 自动调整子图间距
# plt.tight_layout()
# # 显示图形
# plt.show()

"""
Axes与Subplot的区别
Figure、Axes、axis的区别首先要说明的是，在绘图时，Figure（画布）最大，它有点像绘制实体画所用的画板，例如代码fig=plt.figure()的意思就是创建一个空画布。
在画布里，我们可以创建各种子图。子图主要有两类：一类是规规矩矩、排列整齐的子图，叫作Subplot；
另一类是可以不那么规则摆放的子图，叫作Axes。
如果你不能很好地理解，这里有个比喻：把Figure想象成Windows操作系统的桌面，
在桌面上会有各种图标（icon），如果图标是自动对齐到网格的，就称之为Subplot；
如果图标是自由摆放的，甚至可以相互重叠的那种，就称之为Axes。
但不管怎么摆放，Subplot和Axex本质上都是Figure内的子图。

但在本质上，Axes更加底层。事实上，Subplot内部也是调用Axes来实现的，不过是子图排列得更加规范罢了。
因为，Subplot在某种程度上是Axes的特例。但让我们比较困惑的是，在绘图时axis会出来捣乱。其实axis是地地道道的坐标轴。
每个子图都有坐标轴。为了获得更好的可读性，每个坐标轴都可以配上标签（label）。
例如，X轴有xlabel这个属性，Y轴有ylabel属性等。
可能Matplotlib的设计者认为，任何一个子图都要通过多个轴（axis）来呈现（二维图有两个轴，三维图有三个轴），众轴成图，所以就用“axis”的复数形式“Axes”表示子图。
但切不可认为Axes是多个轴（axis）的意思，而应该在整体上把它视为一个在画布中可任意摆放的子图。
正如“无木不成林”，如果没有子图，光有一个画布，是无法构成一个图形显示对象的。但是，如果我们有意识地添加子图，哪怕是一个空子图，它也构成了可显示的图形对象。

区别
层次结构: Axes 是更基本的概念，表示的是实际绘图的区域；而 Subplot 是一种特殊的 Axes 布局方式，用来在一张图中放置多个 Axes。
使用场景: 如果你需要绘制一个独立的图表，可以直接使用 Axes；如果你想要在一张图中同时展示多个相关联的图表，那么你会用到 Subplot 来组织这些 Axes。
灵活性: Axes 提供了对单个图表的最大控制权，而 Subplot 则简化了多图布局的过程，但可能在某些高级定制方面不如直接操作 Axes 灵活。
"""



































