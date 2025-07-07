import pandas as pd

train_df = pd.read_csv('train.csv')

# 查看数据分布
print(train_df.head(10))
print(train_df.shape)
print(train_df.info())  # 查看数据类型
print(train_df.describe())
print(train_df.isnull().sum())  # 查看整个数据集的缺失值个数 需要注意的是，在Python中，是可以对布尔值实施加法操作的，True被当作1，而False被当作0，

"""
测试集和训练集的差别在于，测试集把标签（即第二列的Survived）删掉了，因为它刻画的是某个乘客“是否为幸存者”，这是留给训练好的模型来预测的。
换句话说，train.csv比test.csv多一列。即使如此，我们还是可以利用concat()把这两个数据集堆叠在一起。
"""
test_df = pd.read_csv('test.csv')
print(test_df.head(10))

"""
Pandas在处理多个数据对象时，往往会用到数据连接操作，这时就可以使用concat()方法（类似于NumPy中的concatenate()方法）。
该方法中有很多参数可供调整，可将两组数据堆叠成你想要的形态。

concat(objs,axis=0,join='outer',join_axes=None,ignore_index=False
,keys=None,levels=None,names=None,verify_integrity=False,opy=True)

参数objs是需要连接的数据对象，当多个数据对象连接时，就需要把它们同时放到一个列表里，
[train_df, test_df]就是两个需要连接的DataFrame对象，它们被放置在一个列表里。

参数axis的默认值为0（axis=0），表示在垂直方向进行连接，即行变多了。
如果设置axis=1，就表示在水平方向进行连接，即列变多了。

参数join是数据集的连接方式。其默认值为outer（join=outer），表示外连接，即所有参与连接的索引全部都保留。
若某数据源中没有另外一个数据源的索引，则在连接时，缺失部分用NaN代替。若join=inner，则表示内连接，
在这种模式下，只取多个数据集中index交集部分的行或列，其余部分删除。
"""
full_df = pd.concat([train_df, test_df], ignore_index=True, sort=False)

"""
关于Seaborn和Matplotlib：
Seaborn在Matplotlib的基础上进行了更高级的API封装，从而使得作图更加容易。
在大多数情况下，使用Seaborn，只需寥寥几行代码就能做出很具吸引力的图。
如果是通过Anaconda安装Python的，那么Seaborn是默认安装好的，我们只需要按照正常流程加载它即可。


"""
# import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']    # 正常显示中文标签
# sns.heatmap(full_df.isnull(),cbar = False).set_title(r"缺失值热力图")

"""
对缺失值实施填充需要用到fillna()方法
fillna(self,value=None,method=None,axis=None,inplace=False,limit=None,downcast=None,**kwargs)[source]

其中，参数value指明有缺失值时该填充什么值，默认值为None，相当于不设置填充值。如果不设置填充值，还能填充什么呢？

这时，就可以用method()方法来指导填充行为。如果某一行或某一列不全为缺失值，那说明它总会找到合法的有效值。
而这个有效值就用来填充空位。这时需要设置填充策略，
如果method='backfill'或method='bfill'，则表示在填充时会按照指定的轴方向，向回（back）找到上一个合法有效值，然后把这个有效值填充到当前空缺处。
反之，如果method='ffill'或method='pad'，则表明按照指定的轴方向，向前（front）找到一个有效值来填充。

参数axis表示的是填充缺失值所沿的轴方向。取值为0或'index'时，表示按行填充，取值为1或'columns'时，表示按列填充。
如果我们希望在原始DataFrame中（而非DataFrame的副本中）填充数据，则需要把参数inplace设置为True。
设置为False时，Pandas会创建一个副本，填充的结果对原有的数据集没有任何影响。这时，我们需要用一个新DataFrame对象来接收fillna()方法的执行结果。

缺失值的填充策略有很多。除了在fillna()方法中利用method()方法来指导填充，我们还可以自定义一些填充策略。
比如，对于数值型空缺，我们可以使用众数、均值、中位数填充。

比如，对于数值型空缺，我们可以使用众数、均值、中位数填充。
对于具备时间序列特征的空缺，我们可以使用插值（interpolation）方式来填充。
插值是一种离散函数逼近的重要方法，它可通过拟合函数在有限个点处的取值状况，估算出函数在其他点（缺失值）处的近似值。
如果是分类数据（即标签）缺失，一种填充策略就是用最常见的类别来填充空缺处，这类似于众数填充。
当然，如果在特征参数很完备的情况下，还可以用模型来预测缺失值，然后填充。

"""
full_df['Embarked'].isnull().sum()  # 填充前缺失值的数量
full_df['Embarked'].fillna(full_df['Embarked'].mode()[0],inplace=True)
full_df['Embarked'].isnull().sum()  # 填充后缺失值的数量

"""
首先来说full_df['Embarked']，它返回的是一个Series对象，它相当于DataFrame中的一列，
然后我们求这个Series对象的众数，这里用到了mode()方法。
需要注意的是，通过前面的介绍可知，一个数据集中的众数可能不止一个，为了稳妥起见，mode()方法返回的是一个列表，以便存储多个并列的众数。
对于一个列表而言，我们想取这个列表中的第一个元素，就可以用下标[0]获得。
"""