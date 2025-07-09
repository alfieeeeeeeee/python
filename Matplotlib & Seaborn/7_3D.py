import numpy as np
import matplotlib.pyplot as plt
"""
在前面章节中，我们介绍了Matplotlib中大部分常用的二维图形绘制方法，
其实Matplotlib还支持三维绘图，不过需要额外导入mpl_toolkits.mplot3d.axes3d模块。
我们需要在实例化子图类型时指定projection为3D，接下来不论是绘制散点图、曲线图，还是给图形添加文字注释，方法都与绘制二维图形相同，区别仅是多出了一个维度。
"""
fig = plt.figure(figsize=(20, 10))  # 创建一个大小为 20x10 英寸的图形对象

ax1 = fig.add_subplot(221, projection='3d') # 在图形中添加一个子图，221 表示 2x2 网格中的第一个子图，projection='3d' 表示创建三维坐标轴
theta = np.linspace(-4 * np.pi, 4 * np.pi, 500) # 生成在 -4π 到 4π 之间均匀分布的 500 个点，作为角度值

z = np.linspace(-2, 2, 500)  # 生成在 -2 到 2 之间均匀分布的 500 个点，作为 z 轴数据
r = z**2 + 1  # 计算半径 r，公式为 r = z^2 + 1
x = r * np.sin(theta)  # 计算 x 坐标，x = r * sin(theta)
y = r * np.cos(theta)  # 计算 y 坐标，y = r * cos(theta)

ax1.plot(x, y, z)  # 绘制三维曲线图
ax1.set_xlabel('x', fontsize=15)  # 设置 x 轴标签，字体大小为 15
ax1.set_ylabel('y', fontsize=15)  # 设置 y 轴标签，字体大小为 15
ax1.set_zlabel('z', fontsize=15)  # 设置 z 轴标签，字体大小为 15


ax2 = fig.add_subplot(222, projection='3d') # 绘制三维散点图
# 在图形中添加一个子图，222 表示 2x2 网格中的第二个子图，projection='3d' 表示创建三维坐标轴
x = np.random.randn(500)  # 生成 500 个符合标准正态分布的随机数，作为 x 轴数据
y = np.random.randn(500)  # 生成 500 个符合标准正态分布的随机数，作为 y 轴数据
z = np.random.randn(500)  # 生成 500 个符合标准正态分布的随机数，作为 z 轴数据
ax2.scatter(x, y, z, c='r')  # 绘制三维散点图，点的颜色为红色
ax2.set_xlabel('x', fontsize=15)  # 设置 x 轴标签，字体大小为 15
ax2.set_ylabel('y', fontsize=15)  # 设置 y 轴标签，字体大小为 15
ax2.set_zlabel('z', fontsize=15)  # 设置 z 轴标签，字体大小为 15


ax3 = fig.add_subplot(223, projection='3d') # 绘制三维曲面图
# 在图形中添加一个子图，223 表示 2x2 网格中的第三个子图，projection='3d' 表示创建三维坐标轴
x = np.linspace(-2, 2, 500)  # 生成在 -2 到 2 之间均匀分布的 500 个点，作为 x 轴数据
y = np.linspace(-2, 2, 500) # 生成 y 轴数据，在 -2 到 2 之间均匀分布 500 个点
x, y = np.meshgrid(x, y) # 根据 x 和 y 的范围生成网格点坐标矩阵 这里假设 x 之前已经定义过，若未定义会报错，此代码片段可能是接着前面代码的
z = np.sqrt(x ** 2 + y ** 2)    # 计算每个网格点对应的 z 值，z 为点 (x, y) 到原点的距离
ax3.plot_surface(x, y, z, cmap=plt.cm.winter)   # 绘制三维曲面图，使用冬季色图（blue-green 色调）来显示曲面
ax3.set_xlabel('x', fontsize=15)    # 设置 x 轴标签，字体大小为 15
ax3.set_ylabel('y', fontsize=15)    # 设置 y 轴标签，字体大小为 15
ax3.set_zlabel('z', fontsize=15)    # 设置 z 轴标签，字体大小为 15


ax4 = fig.add_subplot(224, projection='3d') # 绘制三维条形图 在图形中添加一个子图，224 表示 2x2 网格中的第四个子图，projection='3d' 表示创建三维坐标轴
for z in np.arange(0, 40, 10):      # 循环生成不同 z 值的条形图
    x = np.arange(20)   # 生成 20 个在 0 到 20 之间均匀分布的 x 值
    y = np.random.rand(20)  # 生成 20 个随机数作为 y 值

    ax4.bar(x, y, zs=z, zdir='y')    # 绘制三维条形图，zs 指定条形图的基线高度，zdir 指定条形图的方向为 y 方向
ax4.set_xlabel('x', fontsize=15)    # 设置 x 轴标签，字体大小为 15
ax4.set_ylabel('y', fontsize=15)    # 设置 y 轴标签，字体大小为 15
ax4.set_zlabel('z', fontsize=15)    # 设置 z 轴标签，字体大小为 15

plt.show()

"""
在本例中，我们使用了Matplotlib的三维绘图模块，共绘制了四种图形，
前两个三维图形的绘制方法与二维绘图方法类似，这里不再赘述。需要注意的是曲面图与条形图的绘制。
在第三个三维曲面图中，meshgrid()函数对x、y进行了一一映射，将其处理成网格数据，经过meshgrid()函数处理后（代码第36行），才能对z轴坐标进行取样。
绘制三维条形图时，需要注意的是bar()函数中的参数，三维条形图更像将几组二维条形图放在了统一坐标系下。
具体函数原型为Axes3D.bar(left, height, zs=0, zdir='z',*args, **kwargs)，
其中参数
left表示组的宽度，
height表示条形图的高度，
zs表示二维条形图的组数，
zdir指定哪个坐标轴将充当z轴，多个二维条形图延该轴方向排列，从而表现出三维效果。
"""
