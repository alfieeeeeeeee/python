import numpy as np

# TODO 8. 数组的堆叠操作
"""
有时，我们需要将不同的NumPy数组，通过堆叠（stack）操作，拼接为一个新的较大的数组。
堆叠方式大致分为水平方向堆叠（horizontal stack）、垂直方向堆叠（vertical stack）、深度方向堆叠（depth-wise stack）等。

假设我们想把两本书摆在一起，一共有几种方式？
在同一个平面上，我们可以将这两本书水平左右排列（数组的水平方向堆叠），垂直上下排列（数组的垂直方向堆叠），
借助三维空间（类似于书架），我们还可以让这两本书竖着叠放起来（数组的深度方向堆叠）
"""
# TODO 8.1 水平方向堆叠hstack() horizontal
"""
需要注意的是，该函数的参数是一个元组，而元组的标志之一就是用圆括号将元素括起来，
这样看起来，函数hstack()的参数好像被两层圆括号包围起来一样。
元组内被堆叠的数据对象可以是列表，也可以是NumPy数组，返回结果为NumPy数组。
"""
array5 = np.zeros(shape=(2, 2), dtype=np.intp)  # NumPy 使用 intp 类型是为了确保你在数组索引、内存指针相关场景中，使用的整数总是够用的、兼容平台的。
print(array5)
array6 = np.zeros(shape=(2, 3), dtype=np.intp)
print(array6)
print(np.hstack((array5, array6)))
"""
[[0 0 0 0 0]
 [0 0 0 0 0]]
"""
# TODO 8.2 垂直方向堆叠vstack() vertical
array7 = np.zeros(shape=(2, 2), dtype=np.intp)  # NumPy 使用 intp 类型是为了确保你在数组索引、内存指针相关场景中，使用的整数 总是够用的、兼容平台的。
print(array7)
array8 = np.zeros(shape=(3, 2), dtype=np.intp)
print(array8)
print(np.vstack((array7, array8)))
"""
[[0 0]
 [0 0]
 [0 0]
 [0 0]
 [0 0]]
"""

# concatenate()函数
# 利用concatenate()函数，并设置水平轴方向（axis=1）,默认轴方向是axis=0，实现水平和垂直的数组堆叠
print(np.concatenate((array5, array6), axis=1))
print(np.concatenate((array7, array8)))

# TODO 8.3 深度方向堆叠hstack()
"""
除了水平和垂直方向的堆叠，还有深度方向堆叠（depth-wise stacking），它对应的方法为dstack()。
它可以把一系列数组在第三维度进行堆叠。例如我们可以把图像数据在不同通道上（如RGB）进行叠加.
"""
# 一维
array_red = np.linspace(1, 5, 5)
array_green = np.linspace(6, 10, 5)
array_blue = np.linspace(11, 15, 5)
print(array_red)
print(array_green)
print(array_blue)
print(np.dstack((array_red, array_green, array_blue)))
"""
[1. 2. 3. 4. 5.]
[ 6.  7.  8.  9. 10.]
[11. 12. 13. 14. 15.]

[[[ 1.  6. 11.]
  [ 2.  7. 12.]
  [ 3.  8. 13.]
  [ 4.  9. 14.]
  [ 5. 10. 15.]]]
"""

# 多维
array_R = np.linspace(1, 9, 9).reshape(3, 3)
array_G = np.linspace(10, 18, 9).reshape(3, 3)
array_B = np.linspace(19, 27, 9).reshape(3, 3)
print(array_R)
print(array_G)
print(array_B)
print(np.dstack((array_R, array_G, array_B)))
"""
[[1. 2. 3.]
 [4. 5. 6.]
 [7. 8. 9.]]

[[10. 11. 12.]
 [13. 14. 15.]
 [16. 17. 18.]]

[[19. 20. 21.]
 [22. 23. 24.]
 [25. 26. 27.]]

对于前面的三个数组，如果不考虑深度方向，其输出结果从宏观看来还是3×3的二维数组，
有所不同的是，原来的每一个点，由一个元素在深度方向扩展变成了三个元素，

 [[[ 1. 10. 19.]
  [ 2. 11. 20.]
  [ 3. 12. 21.]]

 [[ 4. 13. 22.]
  [ 5. 14. 23.]
  [ 6. 15. 24.]]

 [[ 7. 16. 25.]
  [ 8. 17. 26.]
  [ 9. 18. 27.]]]
"""
# TODO 8.4 列堆叠与行堆叠
"""
除前面几节介绍的数组堆叠方式之外，我们还可以通过column_stack()方法实现一维数组按列方向（column-wise）堆叠
"""
one = np.arange(0, 3)
two = one * 2
print(np.column_stack((one, two)))
print(np.row_stack((one, two)))
"""
[[0 0]
 [1 2]
 [2 4]]

 [[0 1 2]
 [0 2 4]]
"""
