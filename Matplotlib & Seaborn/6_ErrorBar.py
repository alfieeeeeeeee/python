import math
import matplotlib.pyplot as plt
import numpy as np

"""
在机器学习中，单次实验总难免会产生误差。为减少误差的影响，我们经常实验多次，然后用实验的均值表示要测量或计算的值。
这时，我们可以用误差条（Error Bar）来表征数据的分布，其中误差条的高度为“±标准误”。
在Matplotlib中，errorbar()函数可用于评估预测结果的浮动程度，并显示预测值与真实值之间的误差，从而体现模型的拟合程度。
"""

plt.rcParams['axes.unicode_minus'] = False  # 设置 matplotlib 的参数，确保在图形中正确显示负号

x = np.linspace(-math.pi, math.pi, num=48)  # 使用 numpy 的 linspace 函数生成在 -π 到 π 之间均匀分布的 48 个点，作为 x 轴数据
y = np.sin(x + 0.05 * np.random.standard_normal(len(x)))   # 计算正弦函数值，并添加一些随机噪声（使用标准正态分布的随机数）
y_error = np.abs(0.1 * np.random.standard_normal(len(x)))   # 生成与 x 数据长度相同的随机误差值，用于后续的误差条绘制

fig = plt.figure()  # 创建一个新的图形对象
axis = fig.add_subplot(111)  # 在图形中添加一个子图，111 表示 1x1 网格中的第一个子图

axis.set_ylim(-0.5 * math.pi, 0.5 * math.pi)    # 设置 y 轴的显示范围为 -0.5π 到 0.5π
plt.plot(x, y, 'r--', label='sin(x)')    # 绘制 x 和 y 的折线图，线条样式为红色虚线，并设置标签为 'sin(x)'
plt.errorbar(x, y, yerr=y_error, fmt='o')       # 绘制误差条，x 和 y 为数据点，yerr 为 y 方向的误差值，fmt='o' 表示数据点用圆圈标记

plt.legend(loc='best')
plt.show()

"""
代码实现的功能是模拟一个目标函数y=sin(x)。自变量x存在测量误差，
这里我们用NumPy中的random.standard_normal()来模拟测量误差。
该函数产生与自变量x等长度的正态分布（即均值为0，方差为1）随机数。
为了防止误差过大而淹没正常值，因此这里乘以比例因子0.05来降低影响。
代码中的plt.errorbar()函数可绘制误差条，其中最少含有三个参数：x值、y值，以及y的误差值。
fmt用于指定预测值形状，采用的就是圆点，圆点上的竖直线段就是预测值与真实值之间的误差。
这些竖直线段的长短表示误差的大小。
"""
