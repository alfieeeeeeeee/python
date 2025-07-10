import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Iris-data.csv',parse_dates=True,index_col=[0])
# print(df.head())
# SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm      Species
"""
是的，就一行代码！一行代码就完成了数据的加载、日期的转换和索引的设置。
其中，parse_dates设置为True时，它就会尝试把“疑似”日期的字符串列转换为日期类型。
然后，我们对参数index_col进行赋值，把索引设置为第0列。
可以看到，我们是利用列表对index_col赋值的。
也就是说，如果想把多列设置为索引，把对应的列编号放到列表中即可。
例如，index_col=[0,1]就表示把第0和第1列都设置为索引，形成一个双重索引。
"""
# df.plot()                         # 所有字段画图
# df['SepalLengthCm'].plot()        # 支持单个字段画图

# # 支持两个字段放在一起画图
# df.SepalLengthCm.plot()             # 支持单个字段画图
# df.SepalWidthCm.plot()              # 支持单个字段画图

temp_df = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm']]  # 从数据框df中选择三列数据，并将其存储在新的数据框temp_df中

styles = ['bs-', 'ro-', 'y^-']  # 定义一个列表styles，包含三种不同的曲线风格：蓝色方形点线、红色圆形点线、黄色三角形点线
linewidths = [2, 1, 1]  # 定义一个列表linewidths，包含三条曲线的线宽：第一条线宽为2，后两条线宽为1
labels = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm']  # 定义一个列表labels，包含三条曲线的标签

fig, ax = plt.subplots()  # 创建一个新的图形和一个子图区域，fig代表整个图形，ax代表子图区域

for col, style, lw, label in zip(temp_df.columns, styles, linewidths, labels):  # 使用zip函数将temp_df的列名、曲线风格、线宽和标签一一对应
    temp_df[col].plot(style=style, lw=lw, ax=ax, label=label)  # 对每一列数据进行绘图，使用指定的曲线风格、线宽，并在子图区域ax上绘制，同时设置标签

plt.legend(loc='best')  # 在图形上添加图例，位置自动选择最佳位置
plt.show()  # 显示绘制的图形

"""
Pandas具有强大的数据分析能力，我们可以利用Pandas的布尔矩阵表达形式有选择地绘制某些图形，从而过滤掉不想要的数据。

到目前为止，我们通过Pandas绘制的图形都是一个整体图，那能不能绘制子图呢？
事实上，这并不难。在上述数据环境下，同样通过一行代码就能绘制多个子图。
df[a].plot(subplot = True,figsize = (15,60))
上述代码的含义很简单，结合前面的分析可知，a实际上是一个布尔列表，用以提取符合条件的州（即首字母为M的州）的数据，否则子图太多将难以显示。
参数subplots=True表示要绘制子图，而不是将多个不同的列绘制在同一个画布上，
figsize=(15,60)用来设置每个子图的大小，我们可以根据自己的需要来调整元组中的参数（heigh、width​。
"""
