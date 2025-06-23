import numpy as np

# TODO 9. 数组的分割操作
"""
有矛，就有盾。有堆叠，就有分割。NumPy也提供了数组的分割操作。
和堆叠类似，分割也包括水平方向分割、垂直方向分割和深度方向分割，
分别用hsplit()、vsplit()和dsplit()实现。

类似于concatenate()方法可通过设置轴方向，既实现水平方向堆叠，又实现垂直方向堆叠，
split()也可以通过设置分割方向，分别实现hsplit()、vsplit()和dsplit()的功能。

hsplit(ary,indices_or_sections)
其中，ary表示要分割的数组，indices如果只有一个数值，表示水平等分数组（所以要保证数组能被等分，否则会报错），
如果分割的位置不止一个，则用sections来表达。
sections可以是一个数组，也可是一个列表，其中的整数元素依次代表分割的位置。示例代码如下。
"""
array9 = np.arange(16).reshape(4, 4)
print(np.hsplit(array9, 2))
"""
[array([[ 0,  1],
       [ 4,  5],
       [ 8,  9],
       [12, 13]]), 
array([[ 2,  3],
       [ 6,  7],
       [10, 11],
       [14, 15]])]
"""
# 我们知道，分割数组不是目的，分割后拿来用才有意义。这时，就需要知道hsplit()返回的是什么类型的数据
# hsplit()返回的是包含子数组的列表。因此，我们可以用访问列表元素的方式（即方括号加索引）来访问这些子数组。
# hsplit()的效果等价于设置轴方向（axis=1）的split()方法
array9_hsplit = np.hsplit(array9, 2)
print(type(array9_hsplit))  # <class 'list'>
print(len(array9_hsplit))  # 2
print(array9_hsplit[0])
print(array9_hsplit[1])
"""
[[ 0  1]
 [ 4  5]
 [ 8  9]
 [12 13]]

[[ 2  3]
 [ 6  7]
 [10 11]
 [14 15]]
"""
# 分成多个部分
array10 = np.arange(16).reshape(2, 8)
"""
array10就是待分割的数组，[2,4,6]是一个列表，提供了三个分割位置，即第2列、第4列和第6列。
如同切西瓜一样，3刀下去分4瓣，array10这个数组就在列的方向被分成四个子数组，它们一起构成一个列表，
"""
array10_hsplit_mul = np.hsplit(array10, (2, 4, 6))
print(array10_hsplit_mul)
"""
[array([[0, 1],
       [8, 9]]), 
array([[ 2,  3],
       [10, 11]]),
array([[ 4,  5],
       [12, 13]]), 
array([[ 6,  7],
       [14, 15]])]
"""
# 类似地，vsplit()表示垂直方向（或者说行方向）上的分割
# 深度方向的分割（depth-wise splitting），它用的方法是dsplit()
"""
方法中的参数意义与vsplit()和hsplit()一致，其功能是沿第三轴（深度）方向将数组拆分为多个子数组。
当方法split()中设置axis=2时，那么它和dsplit()是等价的。
如果数组维度大于或等于3，则dsplit()方法始终沿第三轴进行拆分.

"""
array11 = np.arange(16).reshape(2, 2, 4)
print(array11)
print(np.dsplit(array11, 2))  # 将数组在深度方向上等分为两部分
"""
[[[ 0  1  2  3]
  [ 4  5  6  7]]

 [[ 8  9 10 11]
  [12 13 14 15]]]

对于深度方向的分割，读者们可能会产生困惑，
原因在于，大家对三维（或高于三维）数组的尺寸布局可能有认知偏差。
array3的尺寸为(2, 2, 4)，它的布局应该理解为2个2×4的二维数组，而不是2×2的二维数组有4个。
如果我们能正确理解这一点，那么理解深度方向的分割就容易多了.

[array([[[ 0,  1],
        [ 4,  5]],

       [[ 8,  9],
        [12, 13]]]), 

array([[[ 2,  3],
        [ 6,  7]],

       [[10, 11],
        [14, 15]]])]

"""
