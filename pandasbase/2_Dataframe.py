<<<<<<< HEAD
import pandas as pd
import numpy as np
from numpy.random import randint

"""
如果我们把Series看作Excel表中的一列，那么DataFrame就是Excel中的一张表。
从数据结构的角度来看，Series好比一个带标签的一维数组，而DataFrame就是一个带标签的二维数组，
它可以由若干个一维数组（Series）构成。
"""
# TODO 1.构建Dataframe
"""
为了方便访问数据，DataFrame中不仅有行索引（好比Excel表中最左侧的索引编号），
还有列索引（好比Excel表中各个列的列名）。我们可以通过字典、Series等基本数据结构来构建DataFrame。
最常用的方法之一是，先构建一个由列表或NumPy数组组成的字典，然后再将字典作为DataFrame中的参数。
"""
df1 = pd.DataFrame({'sentence': ['alfie', 'ada', 'john']})
# print(df1)
"""
  sentence
0    alfie
1      ada
2     john

"""

"""
DataFrame是一种表格型数据结构，它含有一组有序的列，每列的值可以不同。
充当DataFrame数据源的字典中有两部分：key和value。其角色各不相同，
字典的key（如sentences）变成了DataFrame的列名称，而字典的value是一个列表，
列表的长度就是行数。为每一行打一个标签，得到的就是索引，位于DataFrame对象的最左侧。
从上面的输出可以看出，与Series类似的是，在默认情况下，DataFrame的索引也是从0开始的自然数序列。
如果充当数据源的字典中有多个key/value对，那么每个key都对应一列。
"""
data1 = {'one': [1, 2, 3], 'two': [4, 5, 6], 'three': [7, 8, 9]}  # 构建字典
df2 = pd.DataFrame(data1)  # 通过字典构造DataFrame
# print(df2)
"""
   one  two  three
0    1    4      7
1    2    5      8
2    3    6      9
"""

"""
除了可以将字典当作构造DataFrame的数据源，我们也可以将NumPy中的二维数组转化为DataFrame对象。
二维数组比较“纯粹”，只能提供必要的数据，DataFrame的索引名称和列名称均无法从数组对象中获取。
因此，通过二维数组创建的DataFrame列名及行名都是默认的自然数序列。
"""
data2 = np.random.randint(1, 10, 9).reshape(3, 3)
df3 = pd.DataFrame(data2)
# print(df3)

# 当然，我们也可以在创建时显式指定列名及index行名.
df4 = pd.DataFrame(data2, columns=['one', 'two', 'three'], index=['a', 'b', 'c'])
# print(df4)
"""
   0  1  2
0  7  3  6
1  6  9  8
2  6  9  1

   one  two  three
a    2    6      8
b    6    2      7
c    1    4      2
"""

"""
本质上，一个DataFrame可以视为由若干个Series构成的。也就是说Series是构成DataFrame的天然数据源。
下面，我们再来看看如何使用Series来创建DataFrame。
"""
row1 = pd.Series(np.arange(3), index=['one', 'two', 'three'])
row2 = pd.Series(np.arange(3), index=['a', 'b', 'c'])
row1.name = 'Series1'
row2.name = 'Series2'
df5 = pd.DataFrame([row1, row2])  # 通过多个series创建dataframe
# print(df5)

"""
         one  two  three    a    b    c
Series1  0.0  1.0    2.0  NaN  NaN  NaN
Series2  NaN  NaN    NaN  0.0  1.0  2.0

原来Series中的index变成了DataFrame中的列索引，而name变成了DataFrame中的行索引，
数据缺失的位置自动用NaN表示。
"""

"""
如同NumPy中的二维数组一样，我们也可以对DataFrame进行“转置”处理。转置的英文为transpose（简写为T），
因此用“DataFrame对象．T”的形式即可完成相应的转置操作，此处“.T”是DataFrame对象的一个属性。
"""
# print(df5.T)  # df5.T 等价于 df5.transpose()
"""
       Series1  Series2
one        0.0      NaN
two        1.0      NaN
three      2.0      NaN
a          NaN      0.0
b          NaN      1.0
c          NaN      2.0

或许有读者会问，连续两次转置，难道不是将df3变回原始模样吗？
为什么两次输出的结果都是df3的转置呢？
其实原因并不复杂，不论是DataFrame的属性“T”，还是transpose()方法，
它们返回的都是原始DataFrame视图的转置，
原始DataFrame对象在转置过程中始终稳若泰山，纹丝未动，自然输出结果是一样的。
"""

# TODO 2.访问DataFrame中的列与行
# 访问DataFrame中的列很方便，因为DataFrame提供了特殊属性——columns，通过具体的列名称，我们就可以轻松获取一列或多列数据。
# print(df5.columns)  # Index(['one', 'two', 'three', 'a', 'b', 'c'], dtype='object')
# print(df5.columns.values)  # ['one' 'two' 'three' 'a' 'b' 'c']
# print(df5.columns.values[0])  # one
# print(df5['one'])
# print(df5.one)  # 和上方等价

"""
Series1    0.0
Series2    NaN
Name: one, dtype: float64

但有一点需要注意，如果列名的字符串包含空格，或存在其他不符合Python变量命名规范的情况，
则不能通过访问对象属性的方式来访问某个特定的列。
也就是说，df2.one这种“对象名．属性名”来访问某个列的方式虽然很优雅，但适用范围有限。
相比而言，df2['one']这类访问方式适用范围更广，因为方括号内的字符串由于被引号引起来，
因此无须受制于Python变量命名规则。
"""

# 此外，上述方法仅仅对单个列是有效的。如果想要同时访问多个列，还是得“规规矩矩”地将多个列的名称打包进一个列表之中，
# print(df5[['one', 'two']])

"""
         one  two
Series1  0.0  1.0
Series2  NaN  NaN
"""

# 倘若想获取DataFrame中一行或多行数据，最简单的方法莫过于使用切片技术，
# DataFrame的切片方法和列表及NumPy是类似的。
# print(df5[:1])
"""
         one  two  three   a   b   c
Series1  0.0  1.0    2.0 NaN NaN NaN
"""

"""
当然，我们也可以利用iloc方法返回DataFrame的多行数据。
如果这些行数据是连续的，可以用行索引的切片操作来获取。
如果这些行数据是不连续的，可以把这些间断的行索引编号汇集起来，赋值给一个列表，
然后将这个列表当作iloc方法的参数.
"""
# print(df5.iloc[0:2])  # 连续行用切片
# print(df5.iloc[[0, 1]])  # 间断行用列表

"""
         one  two  three    a    b    c
Series1  0.0  1.0    2.0  NaN  NaN  NaN
Series2  NaN  NaN    NaN  0.0  1.0  2.0

         one  two  three    a    b    c
Series1  0.0  1.0    2.0  NaN  NaN  NaN
Series2  NaN  NaN    NaN  0.0  1.0  2.0
"""

# print(df5.iloc[1, 1])  # 表示获取第2行第1列的数据（从0开始计数）
# print(df5.iloc[0:2, 1:])  # 表示获取第0行到第1行，第1列至最后1列的数据
"""
iloc方法的优势并不体现在对行粒度的访问上，而是体现在它精确的区域定位上，
方括号内每增加一个逗号，就增加一个维度的控制权。
例如，iloc[2,2]表示获取第2行第2列的数据，实际上就是获取一个确定的单元格数值。

nan

         two  three    a    b    c
Series1  1.0    2.0  NaN  NaN  NaN
Series2  NaN    NaN  0.0  1.0  2.0

获取前两行（即第0行和第1行）与所有列交叉区域的数据。由于行维度的读取是从0开始的，
所以冒号前面的0是可以省略的。它等价于df2.iloc[:2,1:]。
"""

# TODO 3.DataFrame中的删除操作
"""
有了行或列的索引，我们就可以对DataFrame中的数据进行修改。
类似于Series，在DataFrame中同样可以使用drop()方法删除一行或者一列。
"""
column1 = df5['three']
# print(type(column1))  # <class 'pandas.core.series.Series'>
# print(df5.drop('three', axis='columns'))  # 删除列时，轴值还可以设置为axis=1，这与axis='columns'是等价的。
# print(df5)

# 类似地，如果我们把drop()函数的删除轴方向设置为行方向（axis=0），这样就可达到删除行的目的。
# print(df5.drop('Series1', axis=0))  # 行索引,在行方向上删除第0行

"""
         one  two    a    b    c
Series1  0.0  1.0  NaN  NaN  NaN
Series2  NaN  NaN  0.0  1.0  2.0

         one  two  three    a    b    c
Series1  0.0  1.0    2.0  NaN  NaN  NaN
Series2  NaN  NaN    NaN  0.0  1.0  2.0

         one  two  three    a    b    c
Series2  NaN  NaN    NaN  0.0  1.0  2.0
"""

"""
删除DataFrame原始数据的第二种方法，就是要借助drop()中的另外一个参数inplace（本地），其默认值为False，此时我们将其设置为True。
"""
# print(df5.drop('three', axis='columns', inplace=True))  # None

"""
使用`inplace=True`参数时，`drop`方法会直接修改原DataFrame，并且返回None。
因此，当我们执行`print(df5.drop('three', axis='columns', inplace=True))`时，
实际上打印的是`drop`方法的返回值，即None。
"""

# 事实上，我们还可以利用全局内置函数del，在原始DataFrame对象中删除某一列
# del df5['two']
# print(df5)

"""
         one    a    b    c
Series1  0.0  NaN  NaN  NaN
Series2  NaN  0.0  1.0  2.0
"""

# TODO 4.DataFrame中的“轴”方向
"""
DataFrame是一种表格型数据结构，它含有一组有序的列，每一列中的值可以不同。
所以，DataFrame既有行索引，也有列索引。
为了区分这两个索引，并且更方便地操作数据，DataFrame中引入了“轴”（axis）的概念。
但DataFrame轴方向的参数配置非常具有迷惑性，很多用户对此一头雾水，所以有必要在此单列一节说明。
首先需要说明的是，Pandas数值处理的基础是NumPy，所以对于数字轴方向的解释，和NumPy是保持一致的。
例如，axis=1表示水平方向的操作，axis=0表示垂直方向的操作。

但偏偏Pandas设计者给出的所谓可读性强的文字参数，让人很困惑。
例如，axis=1与axis='columns'是等价的。axis=0与axis='index'是等价的。

实际上，应该这么理解：对于axis='columns'，
Pandas设计者想表达的意思是column-wise（跨越不同列的方向），这样它就和axis=1（水平方向）是等价的了。
类似地，axis='index'表示的是row-wise（跨越不同行的方向），这样它就和axis=0（垂直方向）是等价的了。

可以这样记：axis=1 等价于axis = 'column',指的是水平方向 -> 行
          axis=0 等价于axis = 'index', 指的是垂直方向 -> 列
"""
df6 = pd.DataFrame(np.random.randint(10, size=(3, 2)), columns=list('AB'))
# print(df6)
# print(df6.max(axis=1))  # 求水平方向上的最大值
# print(df6.max(axis=0))  # 求垂直方向上的最大值

"""
   A  B
0  2  6
1  2  2
2  0  0

0    6
1    2
2    0
dtype: int32

A    2
B    6
dtype: int32
"""

# TODO 5.DataFrame中的添加操作
# 在DataFrame中，添加一个新行并不复杂。我们需要先创建一个空DataFrame对象，然后利用for循环逐个添加新的行。
df7 = pd.DataFrame(columns=['feature1', 'feature2', 'feature3'])
# print(df7)

"""
在DataFrame中，使用loc(index)方法就可以添加一个新行，这里的index就是一个DataFrame对象中原先没有的行索引。
为一个先前没有的行索引赋值，实质上，就是添加一个新行。
"""
for index in range(5):
    df7.loc[index] = ['name' + str(index)] + list(randint(10, size=2))

# print(df7)

# 也可以按照下面的方式添加新行
df7.loc['new_row'] = 3
# print(df7)

df7.loc['new_row2'] = ['name5', 11, 22]  # 添加一个新行
# print(df7)

"""
Empty DataFrame
Columns: [feature1, feature2, feature3]
Index: []

  feature1  feature2  feature3
0    name0         4         7
1    name1         7         8
2    name2         1         7
3    name3         9         2
4    name4         7         5

        feature1  feature2  feature3
0          name0         0         2
1          name1         5         2
2          name2         6         0
3          name3         1         9
4          name4         7         7
new_row        3         3         3

         feature1  feature2  feature3
0           name0         9         3
1           name1         1         3
2           name2         4         4
3           name3         3         6
4           name4         8         4
new_row         3         3         3
new_row2    name5        11        22
"""

# append方式
df8 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
df9 = pd.DataFrame({'a': [7, 8, 9], 'b': [10, 11, 12]})
# print(df8._append(df9))
# print(df8._append(df9, ignore_index=True))

"""
   a   b
0  1   4
1  2   5
2  3   6
0  7  10
1  8  11
2  9  12

   a   b
0  1   4
1  2   5
2  3   6
3  7  10
4  8  11
5  9  12
"""
df10 = pd.DataFrame({'a': [7, 8, 9], 'b': [10, 11, 12], 'c': [13, 14, 18]})
df11 = pd.DataFrame({'a': [7, 8, 9], 'b': [10, 11, 12]})
# print(df10._append(df11, ignore_index=True))

"""
   a   b     c
0  7  10  13.0
1  8  11  14.0
2  9  12  18.0
3  7  10   NaN
4  8  11   NaN
5  9  12   NaN

从上面的输出可以看到，两个不同列数的DataFrame对象也可以在垂直方向堆叠。
合并后的DataFrame对象列，是合并前两个DataFrame对象列的并集。
其中具有相同列索引的那些列，自动合并为一列，并以“就大不就小”的原则实施合并，
对于不具有相同列索引的DataFrame对象，缺失部分用NaN（空值）来填充。
"""

# 添加列
df11['new_col_1'] = 3
print(df11)

"""
   a   b  new_col_1
0  7  10          3
1  8  11          3
2  9  12          3

DataFrame对象添加一列的语法更加“优雅”：df['column_name']=values，
这里，df为DataFrame的对象名，方括号之内的column_name就是新添加的列名称，values就是我们要添加的数据。
"""

# TODO 6.DataFrame中的apply和transform函数
"""
apply:
可以应用于DataFrame的行或列，也可以应用于整个 DataFrame。常用于执行自定义函数、聚合操作等。
对于 Series：应用一个函数到每个元素。
对于 DataFrame：可以指定 `axis=0`（按列）或 `axis=1`（按行）来应用函数。
"""
# 创建示例DataFrame
df_apply = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]})

# 应用到每一列
result = df_apply.apply(lambda x: x.max() - x.min())
print(result)
# 应用到每一行
result = df_apply.apply(lambda x: x.max() - x.min(), axis=1)
print(result)

"""
A    2
B    2
dtype: int64

0    3
1    3
2    3
dtype: int64
"""



"""
apply的高级用法
核心特性：灵活处理整个分组（返回任意形状），适合复杂逻辑。
"""
df = pd.DataFrame({
    'Group': ['A', 'A', 'B', 'B', 'B', 'C', 'C'],
    'Value': [10, 20, 30, 40, 50, 60, 70],
    'Flag': [True, False, True, True, False, True, False]
})
# 场景1：返回多行/多列（重塑数据）
# 目标：为每个组生成标准化后的新DataFrame
def standardize(group):
    """组内标准化函数"""
    # 计算标准化值：(值 - 均值) / 标准差
    group['Value_Std'] = (group['Value'] - group['Value'].mean()) / group['Value'].std()
    return group  # 返回整个修改后的分组


# 应用标准化函数并重置索引
normalized_df = df.groupby('Group').apply(standardize).reset_index(drop=True)
print("apply 场景1: 数据重塑")
print("说明：为每个组添加标准化列，返回新DataFrame")
print(normalized_df[['Group', 'Value', 'Value_Std']])
print("\n" + "-" * 50 + "\n")

# 场景2：组内排序/过滤
# 目标：筛选每个组内 Value 最大的前2条记录
top2_df = df.groupby('Group').apply(lambda x: x.nlargest(2, 'Value')  # 获取每组Value最大的2条记录
).reset_index(drop=True)  # 重置索引
print("apply 场景2: 组内排序过滤")
print("说明：获取每个组中Value最大的两条记录")
print(top2_df[['Group', 'Value']])
print("\n" + "-" * 50 + "\n")


# 场景3：自定义聚合（返回多指标）
# 目标：为每个组计算多个统计量
def custom_stats(group):
    """自定义统计量函数"""
    return pd.Series({  # 返回包含多个统计量的Series
        'Range': group['Value'].max() - group['Value'].min(),  # 极差
        'Mean': group['Value'].mean(),  # 均值
        'Positive_Count': (group['Value'] > 30).sum()  # 大于30的计数
    })


# 应用自定义统计函数
stats_df = df.groupby('Group').apply(custom_stats).reset_index()
print("apply 场景3: 自定义聚合")
print("说明：计算每个组的极差、均值和大于30的计数")
print(stats_df)
print("\n" + "-" * 50 + "\n")

# 场景4：时间序列处理（组内滚动计算）
# 目标：每组内计算滚动平均（避免组间数据混合）
# 创建时间序列示例数据
dates = pd.date_range('2023-01-01', periods=7)
ts_df = pd.DataFrame({
    'Group': ['A', 'A', 'B', 'B', 'B', 'C', 'C'],
    'Value': [10, 20, 30, 40, 50, 60, 70],
    'Date': dates
    }).set_index('Date')

# 组内滚动计算
ts_df['Rolling_Mean'] = (
    ts_df.groupby('Group')['Value']  # 按Group分组
    .apply(lambda x: x.rolling(window=2).mean())  # 组内计算窗口为2的滚动均值
)
print("apply 场景4: 组内时间序列处理")
print("说明：按组计算滚动平均值（窗口大小=2）")
print(ts_df[['Group', 'Value', 'Rolling_Mean']])
print("\n" + "-" * 50 + "\n")



"""
transform
- 主要用于返回与输入形状相同的转换结果。
- 常见应用场景包括标准化、分组变换等。
- 必须返回与输入相同形状的结果，否则会报错。
- 在进行分组操作时特别有用，可以对每个分组应用函数，并将结果广播回原DataFrame的对应位置。
"""
# 创建示例DataFrame
df_transform = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [10, 20, 30, 40]})

# 使用transform标准化数据
df_transform['normalized_A'] = df_transform.groupby('B')['A'].transform(lambda x: (x - x.mean()) / x.std())
print(df_transform)

"""
   A   B  normalized_A
0  1  10          -1.0
1  2  20          -1.0
2  3  30          -1.0
3  4  40          -1.0
"""

"""
transform的高级用法
核心特性：返回与原始分组相同长度的结果（广播到每个元素），支持多列操作。
"""
# 场景1：条件过滤 + 分组计算
# 目标：计算每个组内 Flag=True 的 Value 均值（未满足条件返回NaN）
df['Mean_Flag'] = (
    df.groupby('Group')  # 按Group分组
    .transform(lambda x: x['Value'][x['Flag']].mean()  # 筛选Flag=True的值计算均值
               if any(x['Flag'])  # 检查组内是否有True值
               else np.nan  # 没有True值返回NaN
    )
)

print("transform 场景1: 条件过滤计算")
print("说明：计算每个组内 Flag=True 的 Value 均值")
print(df[['Group', 'Value', 'Flag', 'Mean_Flag']])
print("\n" + "-"*50 + "\n")

# 场景2：多列联合计算
# 目标：计算每个组内 Value 与组中位数的差异
df['Deviation'] = df.groupby('Group').transform(
    lambda x: x['Value'] - x['Value'].median()  # 计算每个值与组中位数的差值
)
print("transform 场景2: 多列联合计算")
print("说明：计算每个值与其组中位数的偏差")
print(df[['Group', 'Value', 'Deviation']])
print("\n" + "-"*50 + "\n")

# 场景3：使用命名聚合返回多列结果
# 目标：为每个组添加最小值和最大值列
# 注意：需要返回与原始组相同长度的DataFrame
df[['Min', 'Max']] = df.groupby('Group').transform(
    lambda x: pd.DataFrame({  # 创建包含最小最大值的DataFrame
        'Min': [x['Value'].min()] * len(x),  # 最小值重复组长度次数
        'Max': [x['Value'].max()] * len(x)   # 最大值重复组长度次数
    }, index=x.index)  # 保持原始索引
)
print("transform 场景3: 命名聚合返回多列")
print("说明：为每条记录添加所属组的最小值和最大值")
print(df[['Group', 'Value', 'Min', 'Max']])
print("\n" + "-"*50 + "\n")


"""
比较 `apply` 和 `transform`

| 特性       | `apply`                               | `transform`                 |
| 返回值形状  | 不要求与输入形状一致，适用于聚合等操作        | 必须返回与输入形状一致的结果      |
| 分组操作支持 | 支持，但返回结果可能需要额外处理以匹配原始索引 | 自动处理分组并将结果广播到正确位置  |
| 性能       | 通常较慢，因为它提供了更大的灵活性           | 针对特定类型的转换进行了优化      |

实际应用中选择哪个？
如果你需要对数据进行聚合或者不需要保持原始形状的操作，应该选择 `apply`。
如果你希望对数据进行某种形式的变换，并且结果需要与原始数据对齐，则 `transform` 更合适
，尤其是在分组操作中。例如，标准化、填充缺失值等场景下 `transform` 尤其有用。

关键区别总结
| 特性          | `transform`                      | `apply`                          |
|--------------|----------------------------------|----------------------------------|
| 输出长度       | 必须与输入相同长度                   | 任意长度（可改变行数）             |
| 返回类型*      | Series/DataFrame（与输入同结构）     | 任意（标量/Series/DataFrame）    |
| 典型用途       | 组内广播计算、创建新列                | 复杂聚合、数据筛选、返回新结构       |
| 多列操作       | 直接支持（函数可访问多列）             | 需在函数中处理多列                |
| 性能          | 通常更快（优化内部实现）               | 较慢（通用性强）                  |

何时选择哪个？
需要维持原始行数（如创建新列）         → 选 `transform`
需要返回聚合值（如组统计量）           → 选 `agg` 或 `apply`
需要改变数据结构（如排序/过滤/复杂转换） → 选 `apply`
需要高性能广播计算（如标准化）         → 优先 `transform`

"""

# 综合对比,目标：计算每个组的分位数，并标记异常值
# 使用transform广播分位数
df['Q1'] = df.groupby('Group')['Value'].transform(
    lambda x: x.quantile(0.25)  # 计算每个组的25%分位数
)
df['Outlier'] = (df['Value'] > df['Q1'] * 1.5)  # 标记异常值

# 使用apply返回异常值明细
outliers = df.groupby('Group').apply(
    lambda x: x[x['Value'] > x['Value'].quantile(0.75) * 1.5]  # 筛选异常值
).reset_index(drop=True)

print("综合对比: transform vs apply")
print("transform结果: 为每条记录添加分位数和异常标记")
print(df[['Group', 'Value', 'Q1', 'Outlier']])
print("\napply结果: 返回异常值明细")
print(outliers[['Group', 'Value', 'Q1']])
=======
import pandas as pd
import numpy as np
from numpy.random import randint

"""
如果我们把Series看作Excel表中的一列，那么DataFrame就是Excel中的一张表。
从数据结构的角度来看，Series好比一个带标签的一维数组，而DataFrame就是一个带标签的二维数组，
它可以由若干个一维数组（Series）构成。
"""
# TODO 1.构建Dataframe
"""
为了方便访问数据，DataFrame中不仅有行索引（好比Excel表中最左侧的索引编号），
还有列索引（好比Excel表中各个列的列名）。我们可以通过字典、Series等基本数据结构来构建DataFrame。
最常用的方法之一是，先构建一个由列表或NumPy数组组成的字典，然后再将字典作为DataFrame中的参数。
"""
df1 = pd.DataFrame({'sentence': ['alfie', 'ada', 'john']})
# print(df1)
"""
  sentence
0    alfie
1      ada
2     john

"""

"""
DataFrame是一种表格型数据结构，它含有一组有序的列，每列的值可以不同。
充当DataFrame数据源的字典中有两部分：key和value。其角色各不相同，
字典的key（如sentences）变成了DataFrame的列名称，而字典的value是一个列表，
列表的长度就是行数。为每一行打一个标签，得到的就是索引，位于DataFrame对象的最左侧。
从上面的输出可以看出，与Series类似的是，在默认情况下，DataFrame的索引也是从0开始的自然数序列。
如果充当数据源的字典中有多个key/value对，那么每个key都对应一列。
"""
data1 = {'one': [1, 2, 3], 'two': [4, 5, 6], 'three': [7, 8, 9]}  # 构建字典
df2 = pd.DataFrame(data1)  # 通过字典构造DataFrame
# print(df2)
"""
   one  two  three
0    1    4      7
1    2    5      8
2    3    6      9
"""

"""
除了可以将字典当作构造DataFrame的数据源，我们也可以将NumPy中的二维数组转化为DataFrame对象。
二维数组比较“纯粹”，只能提供必要的数据，DataFrame的索引名称和列名称均无法从数组对象中获取。
因此，通过二维数组创建的DataFrame列名及行名都是默认的自然数序列。
"""
data2 = np.random.randint(1, 10, 9).reshape(3, 3)
df3 = pd.DataFrame(data2)
# print(df3)

# 当然，我们也可以在创建时显式指定列名及index行名.
df4 = pd.DataFrame(data2, columns=['one', 'two', 'three'], index=['a', 'b', 'c'])
# print(df4)
"""
   0  1  2
0  7  3  6
1  6  9  8
2  6  9  1

   one  two  three
a    2    6      8
b    6    2      7
c    1    4      2
"""

"""
本质上，一个DataFrame可以视为由若干个Series构成的。也就是说Series是构成DataFrame的天然数据源。
下面，我们再来看看如何使用Series来创建DataFrame。
"""
row1 = pd.Series(np.arange(3), index=['one', 'two', 'three'])
row2 = pd.Series(np.arange(3), index=['a', 'b', 'c'])
row1.name = 'Series1'
row2.name = 'Series2'
df5 = pd.DataFrame([row1, row2])  # 通过多个series创建dataframe
# print(df5)

"""
         one  two  three    a    b    c
Series1  0.0  1.0    2.0  NaN  NaN  NaN
Series2  NaN  NaN    NaN  0.0  1.0  2.0

原来Series中的index变成了DataFrame中的列索引，而name变成了DataFrame中的行索引，
数据缺失的位置自动用NaN表示。
"""

"""
如同NumPy中的二维数组一样，我们也可以对DataFrame进行“转置”处理。转置的英文为transpose（简写为T），
因此用“DataFrame对象．T”的形式即可完成相应的转置操作，此处“.T”是DataFrame对象的一个属性。
"""
# print(df5.T)  # df5.T 等价于 df5.transpose()
"""
       Series1  Series2
one        0.0      NaN
two        1.0      NaN
three      2.0      NaN
a          NaN      0.0
b          NaN      1.0
c          NaN      2.0

或许有读者会问，连续两次转置，难道不是将df3变回原始模样吗？
为什么两次输出的结果都是df3的转置呢？
其实原因并不复杂，不论是DataFrame的属性“T”，还是transpose()方法，
它们返回的都是原始DataFrame视图的转置，
原始DataFrame对象在转置过程中始终稳若泰山，纹丝未动，自然输出结果是一样的。
"""

# TODO 2.访问DataFrame中的列与行
# 访问DataFrame中的列很方便，因为DataFrame提供了特殊属性——columns，通过具体的列名称，我们就可以轻松获取一列或多列数据。
# print(df5.columns)  # Index(['one', 'two', 'three', 'a', 'b', 'c'], dtype='object')
# print(df5.columns.values)  # ['one' 'two' 'three' 'a' 'b' 'c']
# print(df5.columns.values[0])  # one
# print(df5['one'])
# print(df5.one)  # 和上方等价

"""
Series1    0.0
Series2    NaN
Name: one, dtype: float64

但有一点需要注意，如果列名的字符串包含空格，或存在其他不符合Python变量命名规范的情况，
则不能通过访问对象属性的方式来访问某个特定的列。
也就是说，df2.one这种“对象名．属性名”来访问某个列的方式虽然很优雅，但适用范围有限。
相比而言，df2['one']这类访问方式适用范围更广，因为方括号内的字符串由于被引号引起来，
因此无须受制于Python变量命名规则。
"""

# 此外，上述方法仅仅对单个列是有效的。如果想要同时访问多个列，还是得“规规矩矩”地将多个列的名称打包进一个列表之中，
# print(df5[['one', 'two']])

"""
         one  two
Series1  0.0  1.0
Series2  NaN  NaN
"""

# 倘若想获取DataFrame中一行或多行数据，最简单的方法莫过于使用切片技术，
# DataFrame的切片方法和列表及NumPy是类似的。
# print(df5[:1])
"""
         one  two  three   a   b   c
Series1  0.0  1.0    2.0 NaN NaN NaN
"""

"""
当然，我们也可以利用iloc方法返回DataFrame的多行数据。
如果这些行数据是连续的，可以用行索引的切片操作来获取。
如果这些行数据是不连续的，可以把这些间断的行索引编号汇集起来，赋值给一个列表，
然后将这个列表当作iloc方法的参数.
"""
# print(df5.iloc[0:2])  # 连续行用切片
# print(df5.iloc[[0, 1]])  # 间断行用列表

"""
         one  two  three    a    b    c
Series1  0.0  1.0    2.0  NaN  NaN  NaN
Series2  NaN  NaN    NaN  0.0  1.0  2.0

         one  two  three    a    b    c
Series1  0.0  1.0    2.0  NaN  NaN  NaN
Series2  NaN  NaN    NaN  0.0  1.0  2.0
"""

# print(df5.iloc[1, 1])  # 表示获取第2行第1列的数据（从0开始计数）
# print(df5.iloc[0:2, 1:])  # 表示获取第0行到第1行，第1列至最后1列的数据
"""
iloc方法的优势并不体现在对行粒度的访问上，而是体现在它精确的区域定位上，
方括号内每增加一个逗号，就增加一个维度的控制权。
例如，iloc[2,2]表示获取第2行第2列的数据，实际上就是获取一个确定的单元格数值。

nan

         two  three    a    b    c
Series1  1.0    2.0  NaN  NaN  NaN
Series2  NaN    NaN  0.0  1.0  2.0

获取前两行（即第0行和第1行）与所有列交叉区域的数据。由于行维度的读取是从0开始的，
所以冒号前面的0是可以省略的。它等价于df2.iloc[:2,1:]。
"""

# TODO 3.DataFrame中的删除操作
"""
有了行或列的索引，我们就可以对DataFrame中的数据进行修改。
类似于Series，在DataFrame中同样可以使用drop()方法删除一行或者一列。
"""
column1 = df5['three']
# print(type(column1))  # <class 'pandas.core.series.Series'>
# print(df5.drop('three', axis='columns'))  # 删除列时，轴值还可以设置为axis=1，这与axis='columns'是等价的。
# print(df5)

# 类似地，如果我们把drop()函数的删除轴方向设置为行方向（axis=0），这样就可达到删除行的目的。
# print(df5.drop('Series1', axis=0))  # 行索引,在行方向上删除第0行

"""
         one  two    a    b    c
Series1  0.0  1.0  NaN  NaN  NaN
Series2  NaN  NaN  0.0  1.0  2.0

         one  two  three    a    b    c
Series1  0.0  1.0    2.0  NaN  NaN  NaN
Series2  NaN  NaN    NaN  0.0  1.0  2.0

         one  two  three    a    b    c
Series2  NaN  NaN    NaN  0.0  1.0  2.0
"""

"""
删除DataFrame原始数据的第二种方法，就是要借助drop()中的另外一个参数inplace（本地），其默认值为False，此时我们将其设置为True。
"""
# print(df5.drop('three', axis='columns', inplace=True))  # None

"""
使用`inplace=True`参数时，`drop`方法会直接修改原DataFrame，并且返回None。
因此，当我们执行`print(df5.drop('three', axis='columns', inplace=True))`时，
实际上打印的是`drop`方法的返回值，即None。
"""

# 事实上，我们还可以利用全局内置函数del，在原始DataFrame对象中删除某一列
# del df5['two']
# print(df5)

"""
         one    a    b    c
Series1  0.0  NaN  NaN  NaN
Series2  NaN  0.0  1.0  2.0
"""

# TODO 4.DataFrame中的“轴”方向
"""
DataFrame是一种表格型数据结构，它含有一组有序的列，每一列中的值可以不同。
所以，DataFrame既有行索引，也有列索引。
为了区分这两个索引，并且更方便地操作数据，DataFrame中引入了“轴”（axis）的概念。
但DataFrame轴方向的参数配置非常具有迷惑性，很多用户对此一头雾水，所以有必要在此单列一节说明。
首先需要说明的是，Pandas数值处理的基础是NumPy，所以对于数字轴方向的解释，和NumPy是保持一致的。
例如，axis=1表示水平方向的操作，axis=0表示垂直方向的操作。

但偏偏Pandas设计者给出的所谓可读性强的文字参数，让人很困惑。
例如，axis=1与axis='columns'是等价的。axis=0与axis='index'是等价的。

实际上，应该这么理解：对于axis='columns'，
Pandas设计者想表达的意思是column-wise（跨越不同列的方向），这样它就和axis=1（水平方向）是等价的了。
类似地，axis='index'表示的是row-wise（跨越不同行的方向），这样它就和axis=0（垂直方向）是等价的了。

可以这样记：axis=1 等价于axis = 'column',指的是水平方向 -> 行
          axis=0 等价于axis = 'index', 指的是垂直方向 -> 列
"""
df6 = pd.DataFrame(np.random.randint(10, size=(3, 2)), columns=list('AB'))
# print(df6)
# print(df6.max(axis=1))  # 求水平方向上的最大值
# print(df6.max(axis=0))  # 求垂直方向上的最大值

"""
   A  B
0  2  6
1  2  2
2  0  0

0    6
1    2
2    0
dtype: int32

A    2
B    6
dtype: int32
"""

# TODO 5.DataFrame中的添加操作
# 在DataFrame中，添加一个新行并不复杂。我们需要先创建一个空DataFrame对象，然后利用for循环逐个添加新的行。
df7 = pd.DataFrame(columns=['feature1', 'feature2', 'feature3'])
# print(df7)

"""
在DataFrame中，使用loc(index)方法就可以添加一个新行，这里的index就是一个DataFrame对象中原先没有的行索引。
为一个先前没有的行索引赋值，实质上，就是添加一个新行。
"""
for index in range(5):
    df7.loc[index] = ['name' + str(index)] + list(randint(10, size=2))

# print(df7)

# 也可以按照下面的方式添加新行
df7.loc['new_row'] = 3
# print(df7)

df7.loc['new_row2'] = ['name5', 11, 22]  # 添加一个新行
# print(df7)

"""
Empty DataFrame
Columns: [feature1, feature2, feature3]
Index: []

  feature1  feature2  feature3
0    name0         4         7
1    name1         7         8
2    name2         1         7
3    name3         9         2
4    name4         7         5

        feature1  feature2  feature3
0          name0         0         2
1          name1         5         2
2          name2         6         0
3          name3         1         9
4          name4         7         7
new_row        3         3         3

         feature1  feature2  feature3
0           name0         9         3
1           name1         1         3
2           name2         4         4
3           name3         3         6
4           name4         8         4
new_row         3         3         3
new_row2    name5        11        22
"""

# append方式
df8 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
df9 = pd.DataFrame({'a': [7, 8, 9], 'b': [10, 11, 12]})
# print(df8._append(df9))
# print(df8._append(df9, ignore_index=True))

"""
   a   b
0  1   4
1  2   5
2  3   6
0  7  10
1  8  11
2  9  12

   a   b
0  1   4
1  2   5
2  3   6
3  7  10
4  8  11
5  9  12
"""
df10 = pd.DataFrame({'a': [7, 8, 9], 'b': [10, 11, 12], 'c': [13, 14, 18]})
df11 = pd.DataFrame({'a': [7, 8, 9], 'b': [10, 11, 12]})
# print(df10._append(df11, ignore_index=True))

"""
   a   b     c
0  7  10  13.0
1  8  11  14.0
2  9  12  18.0
3  7  10   NaN
4  8  11   NaN
5  9  12   NaN

从上面的输出可以看到，两个不同列数的DataFrame对象也可以在垂直方向堆叠。
合并后的DataFrame对象列，是合并前两个DataFrame对象列的并集。
其中具有相同列索引的那些列，自动合并为一列，并以“就大不就小”的原则实施合并，
对于不具有相同列索引的DataFrame对象，缺失部分用NaN（空值）来填充。
"""

# 添加列
df11['new_col_1'] = 3
print(df11)

"""
   a   b  new_col_1
0  7  10          3
1  8  11          3
2  9  12          3

DataFrame对象添加一列的语法更加“优雅”：df['column_name']=values，
这里，df为DataFrame的对象名，方括号之内的column_name就是新添加的列名称，values就是我们要添加的数据。
"""

# TODO 6.DataFrame中的apply和transform函数
"""
apply:
可以应用于DataFrame的行或列，也可以应用于整个 DataFrame。常用于执行自定义函数、聚合操作等。
对于 Series：应用一个函数到每个元素。
对于 DataFrame：可以指定 `axis=0`（按列）或 `axis=1`（按行）来应用函数。
"""
# 创建示例DataFrame
df_apply = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]})

# 应用到每一列
result = df_apply.apply(lambda x: x.max() - x.min())
print(result)
# 应用到每一行
result = df_apply.apply(lambda x: x.max() - x.min(), axis=1)
print(result)

"""
A    2
B    2
dtype: int64

0    3
1    3
2    3
dtype: int64
"""



"""
apply的高级用法
核心特性：灵活处理整个分组（返回任意形状），适合复杂逻辑。
"""
df = pd.DataFrame({
    'Group': ['A', 'A', 'B', 'B', 'B', 'C', 'C'],
    'Value': [10, 20, 30, 40, 50, 60, 70],
    'Flag': [True, False, True, True, False, True, False]
})
# 场景1：返回多行/多列（重塑数据）
# 目标：为每个组生成标准化后的新DataFrame
def standardize(group):
    """组内标准化函数"""
    # 计算标准化值：(值 - 均值) / 标准差
    group['Value_Std'] = (group['Value'] - group['Value'].mean()) / group['Value'].std()
    return group  # 返回整个修改后的分组


# 应用标准化函数并重置索引
normalized_df = df.groupby('Group').apply(standardize).reset_index(drop=True)
print("apply 场景1: 数据重塑")
print("说明：为每个组添加标准化列，返回新DataFrame")
print(normalized_df[['Group', 'Value', 'Value_Std']])
print("\n" + "-" * 50 + "\n")

# 场景2：组内排序/过滤
# 目标：筛选每个组内 Value 最大的前2条记录
top2_df = df.groupby('Group').apply(lambda x: x.nlargest(2, 'Value')  # 获取每组Value最大的2条记录
).reset_index(drop=True)  # 重置索引
print("apply 场景2: 组内排序过滤")
print("说明：获取每个组中Value最大的两条记录")
print(top2_df[['Group', 'Value']])
print("\n" + "-" * 50 + "\n")


# 场景3：自定义聚合（返回多指标）
# 目标：为每个组计算多个统计量
def custom_stats(group):
    """自定义统计量函数"""
    return pd.Series({  # 返回包含多个统计量的Series
        'Range': group['Value'].max() - group['Value'].min(),  # 极差
        'Mean': group['Value'].mean(),  # 均值
        'Positive_Count': (group['Value'] > 30).sum()  # 大于30的计数
    })


# 应用自定义统计函数
stats_df = df.groupby('Group').apply(custom_stats).reset_index()
print("apply 场景3: 自定义聚合")
print("说明：计算每个组的极差、均值和大于30的计数")
print(stats_df)
print("\n" + "-" * 50 + "\n")

# 场景4：时间序列处理（组内滚动计算）
# 目标：每组内计算滚动平均（避免组间数据混合）
# 创建时间序列示例数据
dates = pd.date_range('2023-01-01', periods=7)
ts_df = pd.DataFrame({
    'Group': ['A', 'A', 'B', 'B', 'B', 'C', 'C'],
    'Value': [10, 20, 30, 40, 50, 60, 70],
    'Date': dates
    }).set_index('Date')

# 组内滚动计算
ts_df['Rolling_Mean'] = (
    ts_df.groupby('Group')['Value']  # 按Group分组
    .apply(lambda x: x.rolling(window=2).mean())  # 组内计算窗口为2的滚动均值
)
print("apply 场景4: 组内时间序列处理")
print("说明：按组计算滚动平均值（窗口大小=2）")
print(ts_df[['Group', 'Value', 'Rolling_Mean']])
print("\n" + "-" * 50 + "\n")



"""
transform
- 主要用于返回与输入形状相同的转换结果。
- 常见应用场景包括标准化、分组变换等。
- 必须返回与输入相同形状的结果，否则会报错。
- 在进行分组操作时特别有用，可以对每个分组应用函数，并将结果广播回原DataFrame的对应位置。
"""
# 创建示例DataFrame
df_transform = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [10, 20, 30, 40]})

# 使用transform标准化数据
df_transform['normalized_A'] = df_transform.groupby('B')['A'].transform(lambda x: (x - x.mean()) / x.std())
print(df_transform)

"""
   A   B  normalized_A
0  1  10          -1.0
1  2  20          -1.0
2  3  30          -1.0
3  4  40          -1.0
"""

"""
transform的高级用法
核心特性：返回与原始分组相同长度的结果（广播到每个元素），支持多列操作。
"""
# 场景1：条件过滤 + 分组计算
# 目标：计算每个组内 Flag=True 的 Value 均值（未满足条件返回NaN）
df['Mean_Flag'] = (
    df.groupby('Group')  # 按Group分组
    .transform(lambda x: x['Value'][x['Flag']].mean()  # 筛选Flag=True的值计算均值
               if any(x['Flag'])  # 检查组内是否有True值
               else np.nan  # 没有True值返回NaN
    )
)

print("transform 场景1: 条件过滤计算")
print("说明：计算每个组内 Flag=True 的 Value 均值")
print(df[['Group', 'Value', 'Flag', 'Mean_Flag']])
print("\n" + "-"*50 + "\n")

# 场景2：多列联合计算
# 目标：计算每个组内 Value 与组中位数的差异
df['Deviation'] = df.groupby('Group').transform(
    lambda x: x['Value'] - x['Value'].median()  # 计算每个值与组中位数的差值
)
print("transform 场景2: 多列联合计算")
print("说明：计算每个值与其组中位数的偏差")
print(df[['Group', 'Value', 'Deviation']])
print("\n" + "-"*50 + "\n")

# 场景3：使用命名聚合返回多列结果
# 目标：为每个组添加最小值和最大值列
# 注意：需要返回与原始组相同长度的DataFrame
df[['Min', 'Max']] = df.groupby('Group').transform(
    lambda x: pd.DataFrame({  # 创建包含最小最大值的DataFrame
        'Min': [x['Value'].min()] * len(x),  # 最小值重复组长度次数
        'Max': [x['Value'].max()] * len(x)   # 最大值重复组长度次数
    }, index=x.index)  # 保持原始索引
)
print("transform 场景3: 命名聚合返回多列")
print("说明：为每条记录添加所属组的最小值和最大值")
print(df[['Group', 'Value', 'Min', 'Max']])
print("\n" + "-"*50 + "\n")


"""
比较 `apply` 和 `transform`

| 特性       | `apply`                               | `transform`                 |
| 返回值形状  | 不要求与输入形状一致，适用于聚合等操作        | 必须返回与输入形状一致的结果      |
| 分组操作支持 | 支持，但返回结果可能需要额外处理以匹配原始索引 | 自动处理分组并将结果广播到正确位置  |
| 性能       | 通常较慢，因为它提供了更大的灵活性           | 针对特定类型的转换进行了优化      |

实际应用中选择哪个？
如果你需要对数据进行聚合或者不需要保持原始形状的操作，应该选择 `apply`。
如果你希望对数据进行某种形式的变换，并且结果需要与原始数据对齐，则 `transform` 更合适
，尤其是在分组操作中。例如，标准化、填充缺失值等场景下 `transform` 尤其有用。

关键区别总结
| 特性          | `transform`                      | `apply`                          |
|--------------|----------------------------------|----------------------------------|
| 输出长度       | 必须与输入相同长度                   | 任意长度（可改变行数）             |
| 返回类型*      | Series/DataFrame（与输入同结构）     | 任意（标量/Series/DataFrame）    |
| 典型用途       | 组内广播计算、创建新列                | 复杂聚合、数据筛选、返回新结构       |
| 多列操作       | 直接支持（函数可访问多列）             | 需在函数中处理多列                |
| 性能          | 通常更快（优化内部实现）               | 较慢（通用性强）                  |

何时选择哪个？
需要维持原始行数（如创建新列）         → 选 `transform`
需要返回聚合值（如组统计量）           → 选 `agg` 或 `apply`
需要改变数据结构（如排序/过滤/复杂转换） → 选 `apply`
需要高性能广播计算（如标准化）         → 优先 `transform`

"""

# 综合对比,目标：计算每个组的分位数，并标记异常值
# 使用transform广播分位数
df['Q1'] = df.groupby('Group')['Value'].transform(
    lambda x: x.quantile(0.25)  # 计算每个组的25%分位数
)
df['Outlier'] = (df['Value'] > df['Q1'] * 1.5)  # 标记异常值

# 使用apply返回异常值明细
outliers = df.groupby('Group').apply(
    lambda x: x[x['Value'] > x['Value'].quantile(0.75) * 1.5]  # 筛选异常值
).reset_index(drop=True)

print("综合对比: transform vs apply")
print("transform结果: 为每条记录添加分位数和异常标记")
print(df[['Group', 'Value', 'Q1', 'Outlier']])
print("\napply结果: 返回异常值明细")
print(outliers[['Group', 'Value', 'Q1']])
>>>>>>> 1ee27c175f430901a0371b8efc021416cc340850
