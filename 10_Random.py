import numpy as np

# TODO 10 随机数模块
"""
除了生成指定元素的N维数组，NumPy中也含有随机数模块，即random模块。numpy.random模块中提供了大量与随机数相关的函数。
"""
# 生成0~1之间的均匀分布随机数
print(np.random.rand())  # 单个
print(np.random.rand(3))  # 一维数组
print(np.random.rand(2, 3))  # 二维数组
"""
0.5486040736432893

[0.48721932 0.96487338 0.68556959]

[[0.36331562 0.59345078 0.2857618 ]
 [0.86871511 0.07241488 0.45783679]]
"""
# 生成标准正态分布随机数
print(np.random.randn(3, 2))
"""
[[ 0.48585648  0.61657352]
 [ 0.11688326 -1.76308133]
 [ 1.31218007  1.02929555]]
"""

# 生成指定范围的整数
print(np.random.randint(1, 10))  # [1, 10)之间的单个整数  2
print(np.random.randint(1, 10, size=5))  # 一维数组  [6 2 7 2 5]

# 随机排列和采样
arr = np.arange(10)
np.random.shuffle(arr)  # 原地打乱
print(arr)  # [6 0 2 9 7 4 5 3 1 8]

# 随机采样（不放回）
sample = np.random.choice(arr, size=3, replace=False)
print(sample)  # [2 5 3]

# 3. 设置随机种子
np.random.seed(42)  # 种子seed是随机数生成器的起点编号,类似于选择了42号种子，后续的只是固定的
print(np.random.rand(1))  # [0.37454012 0.95071431]  rand后面的参数是随机数的数量

# 4 生成其他分布的随机数
# 生成服从正态分布的随机数
print(np.random.normal(loc=0, scale=1, size=5))  # [ 0.64768854  1.52302986 -0.23415337 -0.23413696  1.57921282]
# 生成服从二项分布的随机数
print(np.random.binomial(n=10, p=0.5, size=5))  # [2 8 7 4 4]
