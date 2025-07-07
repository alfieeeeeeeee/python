import pandas as pd
import numpy as np

"""
Pandas吸纳了NumPy中的很多精华，然在数据分析方面“青出于蓝而胜于蓝”。
二者最大的不同在于，Pandas在设计之初就是倾向于支持图表和混杂数据运算的，
相比之下，NumPy显得“纯洁”很多，它是基于数组构建的，
NumPy中的数组一旦被设置为某种数据类型（如整型或浮点型），就会从一而终，不得改变。

Pandas是基于NumPy构建的数据分析包，但它含有比ndarray更为高级的数据结构和操作工具，
如Series类型、DataFrame类型等。有了这些高级数据的辅佐，使得通过Pandas进行数据分析变得更加便捷与高效。
Pandas除了可以通过管理索引来快速访问数据、执行分析和转换运算，还可用于高效绘图，只需寥寥几行代码，
一个栩栩如生的数据可视化图便可“扑面而来”（当然，它用了Matplotlib作为后端支持）。
此外，Pandas还是数据读取“小能手”，支持从多种数据存储文件（如CSV、TXT、Excel、HDF5等）中读取数据，
支持从数据库（如SQL）中读取数据，还支持从Web（如JSON、HTML等）中读取数据。

Pandas的使用便捷，离不开高效的底层数据结构的支持。
Pandas主要有三种数据结构：Series（类似于一维数组）、DataFrame（类似于二维数组）
和Panel（类似于三维数组）。由于Panel并不常用，
因此，新版本的Pandas已经将其列为过时（Deprecated）的数据结构。
"""
# TODO 1.Series的生成

"""
Series是一种类似于一维数组的数据结构，是由一组数据及与之对应的标签（即索引）构成的。
创建Series的语法非常简单。

pd.Series(data,index = index)
在上述构造方法的参数中，data就是数据源，其类型可以是一系列的整数、字符串，也可是浮点数或某类Python对象。
默认索引就是数据的标签（label）

Series的数据源可以用列表来填充。series和list有相似之处，它们内部都包括一系列的数据。
不同之处在于，列表内的元素可以是相同类型的，也可以是不同类型的，也就是说列表中的元素是“大杂烩”。
而Series则不同，它依赖于NumPy中的N维数组（ndarray）而构建，
因此，其内部的数据要整齐划一，数据类型必须相同。
"""
# series1 = pd.Series([1, 4, 5, -1])
# print(series1)
"""
0    1
1    4
2    5
3   -1
dtype: int64
"""

"""
此外，Series增加对应的标签（label）作为索引。如果没有显式添加索引，
Python会自动添加一个0～n-1内的索引值（n为Series对象内含元素的个数）。
通常的视图是索引在左，数值在右。
我们可以把Series理解为Excel表格中的一列。
不过，这个列自带旁边的编号（即索引）
"""
# 通过Series的index和values属性，分别获取索引和数组元素值。
# print(series1.values)
# print(series1.index)
"""
[ 1  4  5 -1]
RangeIndex(start=0, stop=4, step=1)

start=0：索引起始值是 0
stop=4：索引到 4，但不包括 4（即 [0, 1, 2, 3]）
step=1：索引步长是 1
"""

"""
当然，在创建Series对象时，其标签并不必然是0～n-1内的数字，
它也可以被显式指定为其他类型，甚至可在创建索引后被二次修改.
"""
# np.random.randn是NumPy中用于生成服从标准正态分布（均值为 0，标准差为 1）的随机数的函数
# series2 = pd.Series(np.random.randn(6))
# print(series2.values)
# print(series2.index)
# series2.index = ['a', 'b', 'c', 'd', 'e', 'f']
# print(series2)
"""
[-0.36954017  0.35228776 -0.1115395  -1.4079176   0.98616195 -0.02102312]

RangeIndex(start=0, stop=6, step=1)

a    0.839009
b    1.927729
c    0.095861
d    0.229308
e   -1.093406
f    0.808392
dtype: float64

乍一看，Series与Python中的字典颇有相似之处。
的确如此，Series中的index可对应字典中的key，Series中的value与字典中的value相同。
因此，Series也可以由现有的字典数据类型通过“打包”来创建.
"""
# dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# series3 = pd.Series(dic)
# print(series3)
"""
a    1
b    2
c    3
d    4
dtype: int64

由于字典中的key可以“对标”Series中的index，两者都起到快速定位数据的作用，
所以无须单独设置Series所需的index参数。
"""

"""
如果Pandas中的Series与Python中的字典完全一样，那么Series就没有存在的必要了。
言外之意就是，它与字典还是有不同之处的。
我们知道，字典是一种无序的数据类型，而Series却是有序的，并且Series的index和value之间是相互独立的。
此外，两者的索引也是有区别的，Series的index是可变的，而字典的key是不可变的。

Series还提供了简单的统计方法（如describe()）供我们使用。
describe()方法为以列为单位进行统计分析.
"""
# print(series3.describe())
"""
count    4.000000
mean     2.500000
std      1.290994
min      1.000000
25%      1.750000
50%      2.500000
75%      3.250000
max      4.000000
dtype: float64

count：一列数据的个数。mean：一列数据的均值。std：一列数据的均方差。
min：一列数据中的最小值。max：一列数据中的最大值。
25%：一列数据中前25%的数据的分位数。
50%：一列数据中前50%的数据的分位数。
75%：一列数据中前75%的数据的分位数。
"""

# TODO 2.Series的数据访问
"""
一旦指定Series的索引，就可以通过特定索引值，访问、修改索引位置对应的数值。
我们知道，Series对象在本质上就是一个带有标签的NumPy数组，
因此，NumPy中的一些概念和操作手法，可直接用于Series对象。
首先，像NumPy数组一样，我们也可通过下标存取Series对象内部的元素.
"""
# figure = {'Alfie': 20, 'Ada': 19, 'Author': 22, 'Thomas': 21}
# series4 = pd.Series(figure, name='age')  # name='age' 是为这个 Series 对象本身起的一个名字（类似列名）
# print(series4)
# print(series4[0])  不安全
# print(series4['Thomas'])
# print(series4[['Thomas', 'Ada', 'Alfie']])
"""
Alfie     20
Ada       19
Author    22
Thomas    21
Name: age, dtype: int64

20
21

Thomas    21
Ada       19
Alfie     20
Name: age, dtype: int64
"""

# 两个Series对象还可以通过append()方法实施叠加操作，以达到Series对象合并的目的
# series6 = pd.Series([1, 2, 3])
# series7 = pd.Series([4, 5, 6])
# print(series6._append(series7))
# print(series6._append(series7, ignore_index=True))
"""
0    1
1    2
2    3
0    4
1    5
2    6
dtype: int64

可以在append()方法中采用ignore_index=True，
这样原始Series对象中的索引都会被忽略，而由Pandas统一给数值添加索引.

0    1
1    2
2    3
3    4
4    5
5    6
dtype: int64
"""

# TODO 3.Series的向量化操作与布尔索引
"""
类似于NumPy，Pandas中的数据结构也支持广播操作。
比如说，某个向量乘以某个标量，那么这个标量会自我复制，并拉伸至维度尺寸与向量相同，
然后即可进行逐元素（element-wise）操作
"""

# print(series6 * 3)
"""
0    3
1    6
2    9
dtype: int64
"""

"""
在代码层面，向量化通常是消除代码中显式for循环语句的“艺术”。
在底层实现上，Pandas的很多操作都是基于NumPy实现的，
而在NumPy中，向量化操作通常意味着并行处理。
"""
# print(series6 + series7)
"""
0    5
1    7
2    9
dtype: int64

需要注意的是，前面在Series之上的操作，其实并没有破坏原有Series中的数值，
而是临时生成了一个新的Series对象来存储处理的结果。
例如，将Series数组中的所有元素都乘以3，此时Pandas会创建一个匿名的Series对象来接收这个处理结果，
但原有的Series对象apts的值并没有受到任何影响。
"""

# 同样，类似于NumPy，Series也支持利用布尔表达式提取符合条件的数值。
# print(series6 > series6.median())  # 判断series6中的元素是否大于所有数据的中位数
"""
0    False
1    False
2     True
dtype: bool
"""

"""
逻辑判断会产生一个与apts对象维度相同的布尔矩阵，
而这个布尔矩阵本身又可以作为Series对象的下标，
用于获取值为True的位置对应的数值，从而达到抽取特定样本的目的。
"""
# print(series6[series6 > series6.median()])
"""
2    3
dtype: int64
"""

"""
另外，Series对象也可以作为NumPy函数的一个参数。
顾名思义，在本质上，Series就是“一系列”的数据，类似数组向量。
这样一来，它就可以在NumPy函数的操作下，达到“向量进，向量出”的目的，
而不像C或Java等编程语言一样使用for循环来完成类似的操作。
"""
# series8 = pd.Series(np.random.randn(5), index=[1, 2, 3, 4, 5])
# print(series8)
# series9 = np.square(series8)
# print(series9)
# series10 = np.abs(series8)
# print(series10)

"""
1   -0.474483
2    0.149088
3   -1.981861
4    0.079473
5    0.384618
dtype: float64

1    0.225134
2    0.022227
3    3.927773
4    0.006316
5    0.147931
dtype: float64

1    0.474483
2    0.149088
3    1.981861
4    0.079473
5    0.384618
dtype: float64
"""

# TODO 4.Series中的切片操作
# 类似于NumPy，我们可以通过索引切片选取或处理Series中的一个或多个值，其返回的结果依然是Series类型的对象。
# series11 = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
# print(series11[1:3])
"""
b   -1.103973
c    0.377403
dtype: float64
"""

"""
Series对象是一个有标签属性的数组，这个标签也可以用来作为切片的依据, 
特别需要注意的是，与基于数字的切片不同，基于标签的切片访问，其访问区间是左闭右也闭的，
也就是说访问是“指哪打哪”的，不留余地。
"""
# print(series11['a':'c'])
"""
a    0.457724
b   -1.103973
c    0.377403
dtype: float64
"""

# TODO 5.Series中的缺失值
"""
在处理数据时，我们经常会遇到一些缺失值，Pandas对缺失值的处理十分友好。
我们可以使用NumPy中的numpy.nan来创建一个缺失值，在Pandas中，缺失值用NaN（Not a Number，非数字）来表示。
我们可以使用Pandas中的isnull()和notnull()两个方法来检测数据中是否含有缺失值。
"""
# array1 = np.array([1, 2, 3, np.nan])
# series12 = pd.Series(array1, index=['a', 'b', 'c', 'd'])
# print(series12)
# print(series12.isnull())
"""
a    1.0
b    2.0
c    3.0
d    NaN
dtype: float64

a    False
b    False
c    False
d     True
dtype: bool

使用isnull()方法返回的是与原始Series维度相同的布尔Series对象，
其中，True表示该位置处的数据为缺失值。notnull()方法的功能与isnull()方法正好相反，
它将逐个判断Series中的元素是否不为空值。isnull()还可以把Series对象作为参数。
"""

"""
当处理的数据量非常庞大时，缺失值可能“混迹”于茫茫的正常数据之中，我们很难看出哪些数据是缺失值。
这时，可以用布尔表达式的形式，把这样的数据筛选出来。
"""
# print(series12[series12.isnull() == True])
"""
d   NaN
dtype: float64
"""

# TODO 6.Series中的删除与添加操作
# 当我们想要删除Series中的一条或者多条数据时，可以使用Pandas提供的drop()方法。
"""
如前所述，对Series进行删除操作并不会“惊扰”原有Series中的数值。
虽然使用drop()方法删掉了索引值为0的数据，但原有Series中的数据依然安然无恙。
这是因为，drop()操作的流程是这样的：先将原始的Series数据复制到一个新的内存空间（即所谓的深拷贝），
再在新的Series对象基础上，删除指定索引值，
这时，新旧两个Series分处不同的内存空间，自然操作起来互不干涉“内政”。
你可以理解为，drop()操作仅仅返回原有Series对象的一个视图而已。
"""
# series13 = pd.Series([1, 10, -2343, 433])
# print(series13)
# series13.drop(2)  # 去除索引为2的数据
# print(series13.drop(2))
# print(series13)
"""
0       1
1      10
2   -2343
3     433
dtype: int64

0      1
1     10
3    433
dtype: int64

0       1
1      10
2   -2343
3     433
dtype: int64
"""

# 如果我们想一次性删除多个索引值对应的数据，就需要把这多个索引值打包为一个列表，
# series13.drop([0, 3])  # 去除索引为2的数据
# print(series13.drop([0, 3]))
"""
1      10
2   -2343
dtype: int64
"""

"""
在某些情况下，如果我们的确想删除原始Series对象中的数据，该怎么办呢？办法还是有的。
我们可以在drop()方法中多启用一个参数inplace，它是一个布尔类型变量，默认值为False，
如果设置为True，drop()操作就会在“本地”完成，最终的删除效果便会体现在原始Series对象上。
"""
# series14 = pd.Series([199, 1, -2311, 354])
# series14.drop([0, 3], inplace=True)
# print(series14)

"""
1       1
2   -2311
dtype: int64
"""

"""
我们可以删除Series中的数据，自然也可以为其添加新的数据。
为了添加数据，我们需要使用append()方法或者concat()方法，它能把一个Series对象整体追加到前一个Series对象后面。
pd.concat(series15,series16,ignore_index=True)
"""
series15 = pd.Series([199, 1888, -777, 999])
series16 = pd.Series(np.random.randint(1, 10, 4))
print(series15)
print(series16)
print(series15._append(series16))
print(series15._append(series16, ignore_index=True))

"""
0     199
1    1888
2    -777
3     999
dtype: int64

0    7
1    5
2    6
3    4
dtype: int32

0     199
1    1888
2    -777
3     999
0       7
1       8
2       9
3       5
dtype: int64

0     199
1    1888
2    -777
3     999
4       3
5       1
6       8
7       5
dtype: int64
"""

# TODO 7.Series中的name属性
"""
name可以理解为数值列的名称。如果把index也理解为一个特殊索引列的话，那么index.name就是这个索引列的名称。
name属性多用在Pandas另外一个常见的数据结构DataFrame中，DataFrame可视为多个Series对象的组合。
默认情况下，name与index.name都被设置为None。在特定场合下，我们也可以通过如下代码进行修改。
"""
series17 = pd.Series([1.75, 2.10, 1.99])
series17.name = 'height'
series17.index.name = 'No'
print(series17)
"""
No
0    1.75
1    2.10
2    1.99
Name: height, dtype: float64
"""