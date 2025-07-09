import matplotlib.pyplot as plt
import numpy as np

"""
箱形图（boxplot）又称盒须图或箱线图，是一种用来显示某一组数据分散情况的统计图，因形状如箱子而得名。
箱形图是由美国的统计学家约翰·图基（John Tukey）在1977年发明的。箱形图在各种领域都有应用，尤其常见于品质管理领域。
它主要用于反映原始数据的分布特征，还可以实现多组数据分布特征的比较。
它是由六个数值点组成的：异常值（outlier）、最小值（min）、下四分位数（Q1，即第25%分位数）、
中位数（median，即第50%分位数）、上四分位数（Q3，即第75%分位数）、最大值（max），

四分位距离（interquartile range，简称IQR）被定义为Q3-Q1，即Q3和Q1的差值，也就是中间的50%部分。
如果某个值比Q1还小1.5倍的IQR，或者比Q3还大1.5倍的IQR，则被视为异常值。
依据这个标准，箱形图有时候也被用于异常检测。
箱形图是垂直放置的。对于垂直放置的箱形图，
其绘制方法是：先找出一组数据的上边缘（最大值）、下边缘（最小值）、中位数和两个四分位数（Q1和Q3）；
然后，连接两个四分位数画出箱体；再将上边缘（最大值）、下边缘（最小值）与箱体相连，中位数在箱体中间。
"""
data = []  # 初始化一个空列表，用于存储从文件中读取的数据

with open('Iris-data.csv', 'r') as file:  # 以只读模式打开文件
    lines = file.readlines()  # 读取文件中的所有行
    # 跳过标题行（第一行）
    for line in lines[1:]:  # 从第二行开始遍历
        temp = line.strip().split(',')  # 移除换行符并按逗号分割
        # 只取数值列（排除最后一列的字符串标签）
        data.append(temp[1:-1])  # 跳过第一列ID和最后一列标签

data_np = np.array(data).astype(float)  # 转换为NumPy数组并转为浮点数
labels = ['sepal length', 'sepal width', 'petal length', 'petal width'] # 定义特征的名称列表（注意：已跳过ID列）

# 绘制箱线图
plt.figure(figsize=(10, 6))
plt.boxplot(data_np, labels=labels)
plt.title('Iris Dataset Features Boxplot')
plt.ylabel('cm')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

"""
代码第03～09行的功能是，“纯手工”读取Iris.csv文件中的数据。
自然，如果我们利用Pandas，这部分代码可以简化为寥寥几行。在以鸢尾花的四个特征为数据绘制出的四个箱形图中，我们可以看到每个箱形图中都有五条横线。
从上到下，第一条横线为最大值所在位置，第二条横线是上四分位点（Q3）所在位置，箱体内的横线为中位数（median）所在位置，
第四条横线是下四分位点（Q1）所在位置，最下面的横线为最小值（min）所在位置。
如前所述，中间箱体为四分位距离IQR（Q3-Q1），大于Q3+1.5IQR，或小于Q1-1.5IQR的点，我们将它们视为异常值。
在sepal width这一特征的箱形图中有四个异常值点。
通过箱形图，我们对于中位数、异常值、分布区间等形信息一目了然。
数值的分布集中还是分散，观察箱体和线段的长短便能明白。
所以，在数据预处理阶段，我们可以先选择使用箱形图来查看数据的特征，以便后续处理。
"""
