import time
import datetime
from datetime import timedelta
import pandas as pd
import numpy as np
from dateutil.parser import parse

# TODO Pandas时序数据
"""
时间序列（Time Series）数据是一类非常重要的数据。事物的发展总是伴随着时间推进，数据指标也在各个时间点上产生。
时间序列（简称“时序”）是在一个时间周期内，测量值按照时间顺序变化，将这个变量与关联的时间对应而形成的一个数据序列。
"""
# TODO 3.1固定时间
"""
在计算机中，时间多用时间戳来表示。时间戳（Timestamp）是指格林威治时间1970年1月1日00时00分00秒起至当下的总秒数。
它是一个非常大的数字，一直在增加，如1591684854代表北京时间2020/6/9 14:40:54。
那么1970年以前的时间怎么表示呢？用负数，如–1591684957代表1919/7/26 2:17:23。
"""
# 创建时间点
# pd.Timestamp()是Pandas定义时间的主要函数，代替Python中的datetime.datetime对象。
# 至少需要年月日
# print(pd.Timestamp(datetime.datetime(2025, 7, 24))) # 2025-07-24 00:00:00
# 制定时分秒
# print(pd.Timestamp(datetime.datetime(2025, 7, 24,12,12,12))) # 2025-07-24 12:12:12

# 指定时间字符串
# print(pd.Timestamp('2025/01/01')) # 2025-01-01 00:00:00
# print(pd.Timestamp('2025/01/01T12')) # 2025-01-01 12:00:00

# 指定时间位置数字，可依次定义year、month、day、hour、minute、second、microsecond
# print(pd.Timestamp(year=2023, month=10, day=1, hour=12, minute=30)) # 2023-10-01 12:30:00
# print(pd.Timestamp(1672531200, unit='s'))  # 单位可以是 's', 'ms', 'us', 'ns' 2023-01-01 00:00:00
# 用tz指定时区，需要记住的是北京时间值为Asia/Shanghai：2023-01-01 08:00:00+08:00
# print(pd.Timestamp(1672531200, unit='s', tz='Asia/Shanghai'))

# 获取到当前时间，从而可通过属性取到今天的日期、年份等信息
# print(pd.Timestamp('today'))  # 2025-07-24 15:46:28.714189
# print(pd.Timestamp('now'))  # 2025-07-24 15:46:28.714189
# print(pd.Timestamp('now').date())  # 2025-07-24

# 通过当前时间计算出昨天、明天、当月初等信息
# print(pd.Timestamp('now') - pd.Timedelta(days=1)) # 2025-07-23 15:47:59.820824
# print(pd.Timestamp('now') + pd.Timedelta(days=1)) # 2025-07-25 15:48:13.298603
# print(pd.Timestamp('now').replace(day=1)) # 2025-07-01 15:48:43.361176

# pd.to_datetime()也可以实现上述功能，不过根据语义，它常用在时间转换上。
# print(pd.to_datetime('now'))  # 2025-07-24 15:49:32.766702

# 时间的属性
# time = pd.Timestamp('now')
# print(time)  # 2025-07-24 15:55:37.947658
# print(time.asm8)  # 2025-07-24T15:55:37.947658 返回NumPy datetime64格式（以纳秒为单位）
# print(time.dayofweek)  # 1（周几，周一为0） # 3
# print(time.dayofyear)  # 205（一年的第几天）
# print(time.days_in_month)  # 31（当月有多少天）
# print(time.daysinmonth)  # 31（同上）
# # print(time.freqstr) # None（周期字符） 返回时间序列的频率字符串（如'D'表示天，'M'表示月），是freq属性的字符串形式。
# print(time.is_leap_year)  # False（是否闰年，公历的）
# print(time.is_month_end)  # False（是否当月最后一天）
# print(time.is_month_start)  # False（是否当月第一天）
# print(time.is_quarter_end)  # False（是否当季最后一天）
# print(time.is_quarter_start)  # False（是否当季第一天）
# print(time.is_year_end)  # False 是否当年最后一天
# print(time.is_year_start)  # False 是否当年第一天
# print(time.quarter)  # 3（当前季度数）
# print(time.tz)  # None（当前时区别名） 如指定，会返回类似<DstTzInfo 'Asia/Shanghai' CST+8:00:00 STD>
# print(time.week)  # 30（当年第几周）
# print(time.weekofyear)  # 30（同上）
# print(time.day)  # 24（日）
# print(time.fold)  # 0
# # print(time.freq) # None（频度周期）  返回时间序列的频率对象（如Day、MonthEnd等），表示时间间隔的周期单位。
# print(time.hour)  # 15
# print(time.microsecond)  # 947658
# print(time.minute)  # 55
# print(time.month)  # 7
# print(time.nanosecond)  # 0
# print(time.second)  # 37
# print(time.tzinfo)  # None
# print(time.value)  # 1753372537947658000
# print(time.year)  # 2025

# 时间的方法
# time = pd.Timestamp('now', tz='Asia/Shanghai')  # 2025-07-24 16:00:12.465310+08:00
# print(time)
# print(time.astimezone('UTC')) # 2025-07-24 08:03:11.070416+00:00

# 转换单位，向上舍入
# print(time.ceil('s'))  # 转为以秒为单位 2025-07-24 16:04:20+08:00
# print(time.ceil('ns')) # 转为以纳秒为单位  2025-07-24 16:10:31.819943+08:00
# print(time.ceil('d')) # 保留日 2025-07-25 00:00:00+08:00
# print(time.ceil('h')) # 保留时 2025-07-24 17:00:00+08:00

# 转换单位，向下舍入
# print(time.floor('h'))  # 保留时 2025-07-24 16:00:00+08:00
# print(time.round('h'))  # 保留时 2025-07-24 16:00:00+08:00

# print(time.day_name()) # 'Thursday'
# print(time.month_name()) # 'July'

# 将时间戳规范化为午夜，保留tz信息
# print(time.normalize()) # 2025-07-24 00:00:00+08:00

# 将时间元素替换datetime.replace，可处理纳秒
# print(time.replace(year=2019)) # 年份换为2019年
# print(time.replace(month=8)) # 月份换为8月

# 转换为周期类型，将丢失时区
# print(time.to_period(freq='h'))  # 警告
# time_naive = time.tz_localize(None)  # 去除时区
# print(time_naive.to_period(freq="h"))  # 无警告 2025-07-24 16:00

# 转换为指定时区
# print(time.tz_convert('UTC'))  # 转为UTC时间 2025-07-24 08:18:06.234547+00:00

# 本地化时区转换
# time = pd.Timestamp('now')
# print(time.tz_localize('Asia/Shanghai')) # 2025-07-24 16:18:06.237554+08:00
# print(time.tz_localize(None))  # 删除时区 2025-07-24 16:18:06.237554

# # 时间缺失值
# print(pd.Timestamp(pd.NaT))    # NaT
# print(pd.Timedelta(pd.NaT))    # NaT
# print(pd.Period(pd.NaT))       # NaT
#
# # 类似np.nan
# print(pd.NaT == pd.NaT)        # False

# NaT可以代表固定时间、时长、时间周期为空的情况，类似于np.nan可以参与到时间的各种计算中
# 任何涉及 pd.NaT 的运算都会返回 pd.NaT，目的是避免因缺失值产生误导性结果。
# print(pd.NaT + pd.Timestamp('20201001'))    # NaT
# print(pd.NaT + pd.Timedelta('2 days'))      # NaT
# print(pd.Timedelta('2 days') - pd.NaT)      # NaT

# TODO 3.2时长的加减
# # 一天与5个小时相加
# print(pd.Timedelta(pd.offsets.Day(1)) + pd.Timedelta(pd.offsets.Hour(5))) # Timedelta('1 days 05:00:00')
# # 一天与5个小时相减
# pd.Timedelta(pd.offsets.Day(1)) - pd.Timedelta(pd.offsets.Hour(5)) # Timedelta('0 days 19:00:00')

# 固定时间与时长相加或相减会得到一个新的固定时间
# # 11月11日减去一天
# pd.Timestamp('2020-11-11') - pd.Timedelta(pd.offsets.Day(1))  # Timestamp('2020-11-10 00:00:00')
# # 11月11日加3周
# pd.Timestamp('2020-11-11') + pd.Timedelta('3W')  # Timestamp('2020-12-02 00:00:00')

# TODO 3.3时间序列
# TODO 3.3.1时序索引
# 在时间序列数据中，索引经常是时间类型，我们在操作数据时经常会与时间类型索引打交道
# DatetimeIndex是时间索引对象，一般由to_datetime()或date_range()来创建
# print(pd.to_datetime(['11/1/2020',                                          # 类时间字符串
#                       np.datetime64('2020-11-02'),                          # NumPy的时间类型
#                       datetime.datetime(2020, 11, 3)]))  # Python自带时间类型
# DatetimeIndex(['2020-11-01', '2020-11-02', '2020-11-03'], dtype='datetime64[ns]', freq=None)

# date_range()可以给定开始或者结束时间，并给定周期数据、周期频率，会自动生成在此范围内的时间索引数据
# 默认频率为天
# print(pd.date_range('2020-01-01', periods=10))
# print(pd.date_range('2020-01-01', '2020-01-10')) # 同上
# print(pd.date_range(end='2020-01-10', periods=10)) # 同上 设置了end参数
'''
DatetimeIndex(['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04',
               '2020-01-05', '2020-01-06', '2020-01-07', '2020-01-08',
               '2020-01-09', '2020-01-10'],
              dtype='datetime64[ns]', freq='D')
'''
# pd.bdate_range()生成数据可以跳过周六日，实现工作日的时间索引序列
# 频率为工作日
# pd.bdate_range('2020-11-1', periods=10)
'''
DatetimeIndex(['2020-11-02', '2020-11-03', '2020-11-04', '2020-11-05',
               '2020-11-06', '2020-11-09', '2020-11-10', '2020-11-11',
               '2020-11-12', '2020-11-13'],
              dtype='datetime64[ns]', freq='B')
'''

# TODO 3.3.2创建时序数据
# 创建包含时序的Series和DataFrame与创建普通的Series和DataFrame一样，将时序索引序列作为索引或者将时间列转换为时间类型。
# # 生成时序索引
# tidx = pd.date_range('2020-11-1', periods=10)
# # 应用时序索引
# s = pd.Series(range(len(tidx)), index=tidx)
'''
2020-11-01    0
2020-11-02    1
2020-11-03    2
2020-11-04    3
2020-11-05    4
2020-11-06    5
2020-11-07    6
2020-11-08    7
2020-11-09    8
2020-11-10    9
Freq: D, dtype: int64
'''
# 如果将其作为Series的内容，我们会看到序列的数据类型为datetime64[ns]
# pd.Series(tidx)
'''
0   2020-11-01
1   2020-11-02
2   2020-11-03
3   2020-11-04
4   2020-11-05
5   2020-11-06
6   2020-11-07
7   2020-11-08
8   2020-11-09
9   2020-11-10
dtype: datetime64[ns]
'''
# 创建DataFrame
# # 索引
# tidx1 = pd.date_range('2020-11-1', periods=10)
# # 应用索引生成DataFrame
# df = pd.DataFrame({'A': range(len(tidx1)), 'B': range(len(tidx1))[::-1]}, index=tidx1)
'''
            A  B
2020-11-01  0  9
2020-11-02  1  8
2020-11-03  2  7
2020-11-04  3  6
2020-11-05  4  5
2020-11-06  5  4
2020-11-07  6  3
2020-11-08  7  2
2020-11-09  8  1
2020-11-10  9  0
'''

# TODO 3.3.3数据访问
# 首先创建时序索引数据。以下数据包含2020年和2021年，以小时为频率。
# idx2 = pd.date_range('1/1/2020', '12/1/2021', freq='H')
# ts = pd.Series(np.random.randn(len(idx2)), index=idx2)
'''
2020-01-01 00:00:00   -0.151906
2020-01-01 01:00:00    1.837362
2020-01-01 02:00:00    0.921446
                         ...
2021-11-30 23:00:00    2.165372
2021-12-01 00:00:00   -1.402078
Freq: H, Length: 16801, dtype: float64
'''

# 查询访问数据时，和 []、loc等的用法一样，可以按切片的操作对数据进行访问。
# 指定区间的
# ts[5:10]
'''
2020-01-01 05:00:00    1.293141
2020-01-01 06:00:00   -0.343630
2020-01-01 07:00:00    1.177247
2020-01-01 08:00:00    0.048835
2020-01-01 09:00:00    0.191761
Freq: H, dtype: float64
'''

# 只筛选2020年的
# ts['2020']
'''
2020-01-01 00:00:00   -0.151906
2020-01-01 01:00:00    1.837362
2020-01-01 02:00:00    0.921446
                         ...
2020-12-31 23:00:00    1.281032
Freq: H, Length: 8784, dtype: float64
'''

# 还支持传入时间字符和各种时间对象
# 指定天，结果相同
# ts['11/30/2020']
# ts['2020-11-30']
# ts['20201130']
'''
2020-11-30 00:00:00    0.008456
2020-11-30 01:00:00    1.392987
2020-11-30 02:00:00    0.050375
...
...
2020-11-30 22:00:00    1.706308
2020-11-30 23:00:00   -0.395945
Freq: H, dtype: float64
'''
# 指定时间点
# ts[datetime.datetime(2020, 11, 30)]
# ts[pd.Timestamp(2020, 11, 30)] # 同上
# ts[pd.Timestamp('2020-11-30')] # 同上
# ts[np.datetime64('2020-11-30')] # 同上
# 0.008455884999761536

# 也可以使用部分字符查询一定范围内的数据
# ts['2021'] # 查询整个2021年的
# ts['2021-6'] # 查询2021年6月的
# ts['2021-6':'2021-10'] # 查询2021年6月到10月的
# dft['2021-1':'2021-2-28 00:00:00'] # 精确时间
# dft['2020-1-15':'2020-1-15 12:30:00']
# dft2.loc['2020-01-05']

# TODO 3.3.4索引选择器
# index = pd.MultiIndex.from_tuples(
#     [("A", "2020-01-01"), ("A", "2020-01-05"), ("B", "2020-01-05")],
#     names=["Category", "Date"]
# )
# dft2 = pd.DataFrame({"Value": [1, 2, 3]}, index=index)
# idx = pd.IndexSlice
# dft2.loc[idx[:, '2020-01-05'], :]

# df.truncate()作为一个专门对索引的截取工具，可以很好地应用在时序索引上
# 给定开始时间和结束时间来截取部分时间
# ts.truncate(before='2020-11-10 11:20', after='2020-12')
'''
2020-11-10 12:00:00   -0.491139
2020-11-10 13:00:00    0.249429
2020-11-10 14:00:00    1.533352
2020-11-10 15:00:00    0.069323
2020-11-10 16:00:00   -0.244138
                         ...
2020-11-30 20:00:00   -1.411992
2020-11-30 21:00:00    0.006023
2020-11-30 22:00:00    1.706308
2020-11-30 23:00:00   -0.395945
2020-12-01 00:00:00   -0.652092
Freq: H, Length: 493, dtype: float64
'''

# TODO 3.3.5类型转换
"""
由于时间格式样式比较多，很多情况下Pandas并不能自动将时序数据识别为时间类型，所以我们在处理前的数据清洗过程中，需要专门对数据进行时间类型转换。
astype是最简单的时间转换方法，它只能针对相对标准的时间格式，如以下数据的数据类型是object.
"""
# s = pd.Series(['2020-11-01 01:10', '2020-11-11 11:10', '2020-11-30 20:10'])
# print(s)
'''
0    2020-11-01 01:10
1    2020-11-11 11:10
2    2020-11-30 20:10
dtype: object
'''
# 转为时间类型
# print(s.astype('datetime64[ns]'))
'''
0   2020-11-01 01:10:00
1   2020-11-11 11:10:00
2   2020-11-30 20:10:00
dtype: datetime64[ns]
'''
# 转为时间类型，指定频率为天
# print(s.astype('datetime64[D]'))
'''
0   2020-11-01
1   2020-11-11
2   2020-11-30
dtype: datetime64[ns]
'''
# 转为时间类型，指定时区为北京时间
# print(s.astype('datetime64[ns, Asia/Shanghai]'))
'''
0   2020-11-01 01:10:00+08:00
1   2020-11-11 11:10:00+08:00
2   2020-11-30 20:10:00+08:00
dtype: datetime64[ns, Asia/Shanghai]
'''
# pd.to_datetime()也可以转换时间类型
# 转为时间类型
# print(pd.to_datetime(s))
'''
0   2020-11-01 01:10:00
1   2020-11-11 11:10:00
2   2020-11-30 20:10:00
dtype: datetime64[ns]
'''
# pd.to_datetime()还可以将多列组合成一个时间进行转换
# df = pd.DataFrame({'year': [2020, 2020, 2020],
#                    'month': [10, 11, 12],
#                    'day': [10, 11, 12]})
# print(df)
'''
   year  month  day
0  2020     10   10
1  2020     11   11
2  2020     12   12
'''

# 转为时间类型
# print(pd.to_datetime(df))
# print(pd.to_datetime(df[['year', 'month', 'day']]))
'''
0   2020-10-10
1   2020-11-11
2   2020-12-12
dtype: datetime64[ns]
'''
# 用pd.DatetimeIndex直接转为时间序列索引
# 转为时间序列索引，自动推断频率
# print(pd.DatetimeIndex(['20201101', '20201102', '20201103'], freq='infer'))
# DatetimeIndex(['2020-11-01', '2020-11-02', '2020-11-03'], dtype='datetime64[ns]', freq='D')

# TODO 3.3.6按格式转换
# # 不规则格式转换时间
# print(pd.to_datetime('2020_11_11', format='%Y_%m_%d', errors='ignore')) # Timestamp('2020-11-11 00:00:00')
#
# # 可以让系统自己推断时间格式
# print(pd.to_datetime('20200101', infer_datetime_format=True, errors='ignore')) # datetime.datetime(2020, 1, 1, 0, 0)
#
# # 将errors参数设置为coerce，将不会忽略错误，返回空值
# print(pd.to_datetime('20200101', format='%Y%m%d', errors='coerce')) # NaT
#
# # 列转为字符串，再转为时间类型
# print(pd.to_datetime(df.d.astype(str), format='%m/%d/%Y'))
#
# # 其他
# print(pd.to_datetime('2020/11/12', format='%Y/%m/%d')) # Timestamp('2020-11-12 00:00:00')
# print(pd.to_datetime('01-10-2020 00:00', format='%d-%m-%Y %H:%M')) # Timestamp('2010-10-01 00:00:00')
#
# # 对时间戳进行转换，需要给出时间单位，一般为秒
# print(pd.to_datetime(1490195805, unit='s'))             # Timestamp('2017-03-22 15:16:45')
# print(pd.to_datetime(1490195805433502912, unit='ns'))   # Timestamp('2017-03-22 15:16:45.433502912')

# TODO 3.3.7时间访问器.dt
"""
之前介绍过了文本访问器（.str）和分类访问器（.cat），对时间Pandas也提供了一个时间访问器.dt.<method>，
用它可以以time.dt.xxx的形式来访问时间序列数据的属性和调用它们的方法，返回对应值的序列。
"""
# s = pd.Series(pd.date_range('2020-11-01', periods=5, freq='d'))
# print(s)
'''
0   2020-11-01
1   2020-11-02
2   2020-11-03
3   2020-11-04
4   2020-11-05
dtype: datetime64[ns]
'''

# 各天是星期几
# print(s.dt.day_name())
'''
0       Sunday
1       Monday
2      Tuesday
3    Wednesday
4     Thursday
dtype: object
'''
# # 时间访问器操作
# print(s.dt.date)
# print(s.dt.time)
# print(s.dt.timetz)
#
# # 以下为时间各成分的值
# print(s.dt.year)
# print(s.dt.month)
# print(s.dt.day)
# print(s.dt.hour)
# print(s.dt.minute)
# print(s.dt.second)
# print(s.dt.microsecond)
# print(s.dt.nanosecond)
#
# # 以下为与周、月、年相关的属性
# print(s.dt.week)
# print(s.dt.weekofyear)
# print(s.dt.dayofweek)
# print(s.dt.weekday)
# print(s.dt.dayofyear) # 一年中的第几天
# print(s.dt.quarter) # 季度数
# print(s.dt.is_month_start) # 是否月第一天
# print(s.dt.is_month_end) # 是否月最后一天
# print(s.dt.is_quarter_start) # 是否季度第一天
# print(s.dt.is_quarter_end) # 是否季度最后一天
# print(s.dt.is_year_start) # 是否年第一天
# print(s.dt.is_year_end) # 是否年最后一天
# print(s.dt.is_leap_year) # 是否闰年
# print(s.dt.daysinmonth) # 当月有多少天
# print(s.dt.days_in_month) # 同上
# print(s.dt.tz) # 时区
# print(s.dt.freq) # 频率

# 以下为转换方法
# print(s.dt.to_period)
# print(s.dt.to_pydatetime)
# print(s.dt.tz_localize)
# print(s.dt.tz_convert)
# print(s.dt.normalize)
# print(s.dt.strftime)
# print(s.dt.round(freq='D'))  # 类似四舍五入
# print(s.dt.floor(freq='D'))  # 向下舍入为天
# print(s.dt.ceil(freq='D'))  # 向上舍入为天
#
# print(s.dt.month_name)  # 月份名称
# print(s.dt.day_name)  # 星期几的名称
# print(s.dt.start_time)  # 开始时间
# print(s.dt.end_time)  # 结束时间
# print(s.dt.days)  # 天数
# print(s.dt.seconds)  # 秒
# print(s.dt.microseconds)  # 毫秒
# print(s.dt.nanoseconds)  # 纳秒
# print(s.dt.components)  # 各时间成分的值
# print(s.dt.to_pytimedelta)  # 转为Python时间格式
# print(s.dt.total_seconds)  # 总秒数


# TODO 3.3.8时序数据移动
# shift()方法可以在时序对象上实现向上或向下移动。
# rng = pd.date_range('2020-11-01', '2020-11-04')
# ts = pd.Series(range(len(rng)), index=rng)
# print(ts)
'''
2020-11-01    0
2020-11-02    1
2020-11-03    2
2020-11-04    3
Freq: D, dtype: int64
'''
# 向上移动一位
# print(ts.shift(-1))
'''
2020-11-01    1.0
2020-11-02    2.0
2020-11-03    3.0
2020-11-04    NaN
Freq: D, dtype: float64
'''

# shift()方法接受freq频率参数，该参数可以接受DateOffset类或其他类似timedelta的对象，也可以接受偏移别名
# 向上移动一个工作日，11-01是周日
# ts.shift(-1, freq='B')
'''
2020-10-30    0
2020-10-30    1
2020-11-02    2
2020-11-03    3
dtype: int64
'''

# TODO 3.3.9频率转换
# 更换时间频率是将时间序列由一个频率单位更换为另一个频率单位，实现时间粒度的变化。更改频率的主要功能是asfreq()方法。
# 以下是一个频率为自然日的时间序列
# rng = pd.date_range('2020-11-01', '2020-12-01')
# ts = pd.Series(range(len(rng)), index=rng)
# print(ts)
'''
2020-11-01     0
2020-11-02     1
2020-11-03     2
2020-11-04     3
...
2020-11-29    28
2020-11-30    29
2020-12-01    30
Freq: D, dtype: int64
'''
# 我们将它的频率变更为更加细的粒度，会产生缺失值
# 频率转为12小时
# print(ts.asfreq(pd.offsets.Hour(12)))
'''
2020-11-01 00:00:00     0.0
2020-11-01 12:00:00     NaN
2020-11-02 00:00:00     1.0
2020-11-02 12:00:00     NaN
2020-11-03 00:00:00     2.0
                       ...
2020-11-29 00:00:00    28.0
2020-11-29 12:00:00     NaN
2020-11-30 00:00:00    29.0
2020-11-30 12:00:00     NaN
2020-12-01 00:00:00    30.0
Freq: 12H, Length: 61, dtype: float64
'''
# 对于缺失值可以用指定值或者指定方法进行填充
# 对缺失值进行填充
# print(ts.asfreq(freq='12h', fill_value=0))
'''
2020-11-01 00:00:00     0
2020-11-01 12:00:00     0
2020-11-02 00:00:00     1
2020-11-02 12:00:00     0
2020-11-03 00:00:00     2
                       ..
2020-11-29 00:00:00    28
2020-11-29 12:00:00     0
2020-11-30 00:00:00    29
2020-11-30 12:00:00     0
2020-12-01 00:00:00    30
Freq: 12H, Length: 61, dtype: int64
'''

# 对产生的缺失值使用指定方法填充
# print(ts.asfreq(pd.offsets.Hour(12), method='pad')) # 填充逻辑：用前一个有效值填充缺失值。
'''
2020-11-01 00:00:00     0
2020-11-01 12:00:00     0
2020-11-02 00:00:00     1
2020-11-02 12:00:00     1
2020-11-03 00:00:00     2
                       ..
2020-11-29 00:00:00    28
2020-11-29 12:00:00    28
2020-11-30 00:00:00    29
2020-11-30 12:00:00    29
2020-12-01 00:00:00    30
Freq: 12H, Length: 61, dtype: int64
'''
# TODO 3.3.10时间偏移
"""
ateOffset类似于时长Timedelta，但它使用日历中时间日期的规则，而不是直接进行时间性质的算术计算，让时间更符合实际生活。
比如工作日就是一个很常见的应用，周四办事，承诺三个工作日内办结，不是最迟周日办完，而是跳过周六周日，最迟周二办完。
"""
# DateOffset对象
# 我们通过夏令时来理解DateOffset对象。有些地区使用夏令时，每日偏移时间有可能是23或24小时，甚至25个小时。
# 生成一个指定的时间，芬兰赫尔辛基时间执行夏令时
# t = pd.Timestamp('2016-10-30 00:00:00', tz='Europe/Helsinki')
# print(t)  # Timestamp('2016-10-30 00:00:00+0300', tz='Europe/Helsinki')
# print(t + pd.Timedelta(days=1))  # 增加一个自然天 # Timestamp('2016-10-30 23:00:00+0200', tz='Europe/Helsinki')
# print(t + pd.DateOffset(days=1))  # 增加一个时间偏移天 # Timestamp('2016-10-31 00:00:00+0200', tz='Europe/Helsinki')

# 工作日的情况
# 定义一个日期
# d = pd.Timestamp('2020-10-30')
# print(d) # Timestamp('2020-10-30 00:00:00')
# print(d.day_name()) # 'Friday'

# 增加两个工作日
# 定义2个工作日时间偏移变量
# two_business_days = 2 * pd.offsets.BDay()

# 增加两个工作日
# print(d + two_business_days)  # 同上 Timestamp('2020-11-03 00:00:00')

# 取增加两个工作日后的星期
# print((d + two_business_days).day_name())  # 'Tuesday'

"""
我们发现，与时长Timedelta不同，时间偏移DateOffset不是数学意义上的增加或减少，而是根据实际生活的日历对现有时间进行偏移。
时长可以独立存在，作为业务的一个数据指标，而时间偏移DateOffset的意义是找到一个时间起点并对它进行时间移动。
"""

# TODO 3.3.11时间段
# Pandas中的Period()对象表示一个时间段，比如一年、一个月或一个季度。与时间长度不同，它表示一个具体的时间区间，有时间起点和周期频率。
# 创建一个时间段（年）
# print(pd.Period('2020')) # 创建一个时间段（季度）# Period('2020', 'A-DEC')
# 以第一个为例，返回的时间段对象里有两个值：第一个是这个时间段的起始时间；第二个字符串“A-DEC”中“A”为年度（Annual），“DEC”为12月（December）。
# 这个时间段对象代表一个在2020年结束于12月的全年时间段。
# print(pd.Period('2020Q4'))  # Period('2020Q4', 'Q-DEC')

# 创建时间段，我们还可以传入更多参数
# 2020-01-01全天的时间段
# print(pd.Period(year=2020, freq='D'))  # Period('2020-01-01', 'D')

# 一周
# print(pd.Period('20201101', freq='W'))  # Period('2020-10-26/2020-11-01', 'W-SUN')

# 默认周期，对应到最细粒度——分钟
# print(pd.Period('2020-11-11 23:00'))  # Period('2020-11-11 23:00', 'T')

# 指定周期
# print(pd.Period('2020-11-11 23:00', 'D'))  # Period('2020-11-11', 'D')

# Period()对象的属性方法
# p = pd.Period('2020Q4')
# print(p.start_time)  # Timestamp('2020-10-01 00:00:00')
# print(p.end_time)  # Timestamp('2020-12-31 23:59:59.999999999')

# 时间段的计算
# 在2020Q4上增加一个周期
# print(pd.Period('2020Q4') + 1) # Period('2021Q1', 'Q-DEC')
# 在2020Q4上减少一个周期
# print(pd.Period('2020Q4') - 1) # Period('2020Q3', 'Q-DEC')

# 时间段对象也可以和时间偏移对象做加减
# 增加一小时
# print(pd.Period('20200101 15') + pd.offsets.Hour(1))  # Period('2020-01-01 16:00', 'H')
# 增加10天
# print(pd.Period('20200101') + pd.offsets.Day(10))    # Period('2020-01-11', 'D')

# 时间段索引
# 类似于时间范围pd.date_range()生成时序索引数据，pd.period_range()可以生成时间段索引数据
# 生成时间段索引对象
# print(pd.period_range('2020-11-01 10:00', periods=10, freq='H'))
'''
PeriodIndex(['2020-11-01 10:00', '2020-11-01 11:00', '2020-11-01 12:00',
             '2020-11-01 13:00', '2020-11-01 14:00', '2020-11-01 15:00',
             '2020-11-01 16:00', '2020-11-01 17:00', '2020-11-01 18:00',
             '2020-11-01 19:00'],
            dtype='period[H]', freq='H')
'''

# 指定开始和结束时间
# print(pd.period_range('2020Q1', '2021Q4', freq='Q-NOV'))
'''
PeriodIndex(['2020Q1', '2020Q2', '2020Q3', '2020Q4', '2021Q1', '2021Q2',
             '2021Q3', '2021Q4'],
            dtype='period[Q-NOV]', freq='Q-NOV')
'''

# TODO 3.3.12时间操作
# 时区转换
# Pandas使用pytz和dateutil库或标准库中的datetime.timezone对象为使用不同时区的时间戳提供了丰富的支持。
import pytz

# print(pytz.common_timezones)
# print(pytz.timezone)

# ts = pd.date_range('11/11/2020 00:00', periods=10, freq='D')
# print(ts.tz is None) # True
# print(pd.date_range('2020-01-01', periods=10, freq='D', tz='Asia/Shanghai'))
# print(pd.Timestamp('2020-01-01', tz='Asia/Shanghai'))

# 从一个时区转换为另一个时区，使用tz_convert方法
# 使用pytz支持
# rng_pytz = pd.date_range('11/11/2020 00:00', periods=3,
#                          freq='D', tz='Europe/London')
# print(rng_pytz.tz_convert('US/Eastern'))
'''
DatetimeIndex(['2020-03-05 19:00:00-05:00', '2020-03-06 19:00:00-05:00',
               '2020-03-07 19:00:00-05:00'],
              dtype='datetime64[ns, US/Eastern]', freq='D')
'''
# 时间的格式化
# 解析时间格式
# print(pd.to_datetime('2020*11*12', format='%Y*%m*%d'))  # Timestamp('2020-11-12 00:00:00')
# 输出的时间格式
# print(pd.Timestamp('now').strftime('%Y年%m月%d日'))  # '2020年11月05日'

# 时间重采样
"""
Pandas可以对时序数据按不同的频率进行重采样操作，
例如，原时序数据频率为分钟，使用resample()可以按5分钟、15分钟、半小时等频率进行分组，然后完成聚合计算。
时间重采样在资金流水、金融交易等业务下非常常用。
"""
# idx = pd.date_range('2020-01-01', periods=500, freq='Min')
# ts = pd.Series(range(len(idx)), index=idx)
# print(ts)
'''
2020-01-01 00:00:00      0
2020-01-01 00:01:00      1
2020-01-01 00:02:00      2
                      ...
2020-01-01 08:18:00    498
2020-01-01 08:19:00    499
Freq: T, Length: 500, dtype: int64
'''

# 每5分钟进行一次聚合
# print(ts.resample('5Min').sum())
'''
2020-01-01 00:00:00      10
2020-01-01 00:05:00      35
2020-01-01 00:10:00      60
2020-01-01 00:15:00      85
2020-01-01 00:20:00     110
                       ...
2020-01-01 07:55:00    2385
2020-01-01 08:00:00    2410
2020-01-01 08:05:00    2435
2020-01-01 08:10:00    2460
2020-01-01 08:15:00    2485
Freq: 5T, Length: 100, dtype: int64
'''
# 重采样功能非常灵活，你可以指定许多不同的参数来控制频率转换和重采样操作。
# 通过类似于groupby聚合后的各种统计函数实现数据的分组聚合，包括sum、mean、std、sem、max、min、mid、median、first、last、ohlc。
# print(ts.resample('5Min').mean()) # 平均
# print(ts.resample('5Min').max()) # 最大值
# 其中ohlc是又叫美国线（Open-High-Low-Close chart，OHLC chart），可以呈现类似股票的开盘价、最高价、最低价和收盘价
# 两小时频率的美国线
# print(ts.resample('2h').ohlc())
'''
                     open  high  low  close
2020-01-01 00:00:00     0   119    0    119
2020-01-01 02:00:00   120   239  120    239
2020-01-01 04:00:00   240   359  240    359
2020-01-01 06:00:00   360   479  360    479
2020-01-01 08:00:00   480   499  480    499
'''

# 以将closed参数设置为“left”或“right”，以指定开闭区间的哪一端
# print(ts.resample('2h', closed='left').mean())
'''
2020-01-01 00:00:00     59.5
2020-01-01 02:00:00    179.5
2020-01-01 04:00:00    299.5
2020-01-01 06:00:00    419.5
2020-01-01 08:00:00    489.5
Freq: 2H, dtype: float64
'''

# print(ts.resample('2h', closed='right').mean())
'''
2019-12-31 22:00:00      0.0
2020-01-01 00:00:00     60.5
2020-01-01 02:00:00    180.5
2020-01-01 04:00:00    300.5
2020-01-01 06:00:00    420.5
2020-01-01 08:00:00    490.0
Freq: 2H, dtype: float64
'''

# 上采样
"""
上采样（upsampling）一般应用在图形图像学中，目的是放大图像。由于原数据有限，放大图像后需要对缺失值进行内插值填充。
在时序数据中同样存在着类似的问题，上例中的数据频率是分钟，我们要对其按30秒重采样
"""
# print(ts.head(3).resample('30S').asfreq())
'''
2020-01-01 00:00:00    0.0
2020-01-01 00:00:30    NaN
2020-01-01 00:01:00    1.0
2020-01-01 00:01:30    NaN
2020-01-01 00:02:00    2.0
Freq: 30S, dtype: float64
'''
# 我们发现由于原数据粒度不够，出现了缺失值，这就需要用.ffill()和.bfill()来计算填充值
# print(ts.head(3).resample('30S').ffill())
'''
2020-01-01 00:00:00    0
2020-01-01 00:00:30    0
2020-01-01 00:01:00    1
2020-01-01 00:01:30    1
2020-01-01 00:02:00    2
Freq: 30S, dtype: int64
'''

# print(ts.head(3).resample('30S').bfill())
'''
2020-01-01 00:00:00    0
2020-01-01 00:00:30    1
2020-01-01 00:01:00    1
2020-01-01 00:01:30    2
2020-01-01 00:02:00    2
Freq: 30S, dtype: int64
'''

# 重采样聚合
# df = pd.DataFrame(np.random.randn(1000, 3),
#                   index=pd.date_range('1/1/2020', freq='S', periods=1000),
#                   columns=['A', 'B', 'C'])
#
# # 生成Resampler重采样对象
# r = df.resample('3T')
# print(r.mean())
'''
                            A         B         C
2020-01-01 00:00:00  0.027794 -0.079557 -0.075456
2020-01-01 00:03:00  0.112137  0.035522 -0.017160
2020-01-01 00:06:00  0.090148 -0.057349 -0.042678
2020-01-01 00:09:00  0.125550 -0.041914 -0.004795
2020-01-01 00:12:00 -0.107330 -0.043023  0.074237
2020-01-01 00:15:00 -0.021769 -0.142557  0.066897
'''
