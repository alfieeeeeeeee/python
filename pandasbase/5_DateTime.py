import time
import datetime
from datetime import timedelta
import pandas as pd
import numpy as np
from dateutil.parser import parse

# TODO 日期和时间数据的类型及工具
"""
Python标准库包含了日期和时间数据的类型，也包括日历相关的功能。datetime、time和calendar模块是开始处理时间数据的主要内容。
datetime.datetime类型，或简写为datetime，是广泛使用的.
"""
# now = datetime.now()
# print(now)  # 2025-07-24 13:48:04.430044
# print(now.year, now.month, now.day)  # 2025 7 24

# # datetime既存储了日期，也存储了细化到微秒的时间。
# # timedelta表示两个datetime对象的时间差
# delta = datetime(2025, 1, 1) - datetime(2025, 7, 24, 12, 12)
# print(delta)  # -205 days, 11:48:00
# print(delta.days, delta.seconds)  # -205 42480
#
# # 你可以为一个datetime对象加上（或减去）一个timedelta或其整数倍来产生一个新的datetime对象
# start = datetime(2025, 1, 1)
# print(start + timedelta(12))  # 2025-01-13 00:00:00
# print(start - timedelta(365))  # 2024-01-02 00:00:00

"""
datetime模块的数据类型:
类型	        描述
date	    使用公历日历存储日历日期（年，月，日）
time	    将时间存储为小时，分钟，秒和微秒
datetime	存储日期和时间
timedelta	表示两个 datetime 值之间的差（如日，秒和微秒）
tzinfo	    用于存储时区信息的基本类型
"""
# TODO 1.1字符串与datetime互相转换
"""
可以使用str方法或传递一个指定的格式给strftime方法来对datetime对象和pandas的Timestamp对象进行格式化

datetime格式说明
类型	    描述
%Y	    四位的年份
%y	    两位的年份
%m	    两位的月份 [01, 12]
%d	    两位的日期号 [01, 31]
%H	    小时，24小时制 [00, 23]
%I	    小时，12小时制 [01, 12]
%M	    两位的分钟 [00, 59]
%S	    秒 [00, 61]（60、61是闰秒）
%w	    星期日期 [0（星期天），6]
%U	    一年中的星期数 [00, 53]。以星期天为每周的第一天，一年中第一个星期天前的日期作为“第0周”
%W	    一年中的星期数 [00, 53]。以星期一为每周的第一天，一年中第一个星期一前的日期作为“第0周”
%z	    格式为+HHMM或-HHMM的UTC时区偏移；如果没有时区则为空
%F	    %Y-%m-%d的简写（例如，2012-4-18）
%D	    %m/%d/%y的简写（例如，04/18/12）

可以使用datetime.srtptime和这些格式代码，将字符串转换日期
"""
# stamp = datetime(2025, 7, 24)
# print(str(stamp))  # 2025-07-24 00:00:00
# print(stamp.strftime('%Y-%m-%d'))  # 2025-07-24

# value = '2025/07/24'
# date_obj = datetime.strptime(value, '%Y/%m/%d')  # 先将字符串解析为 datetime 对象
# print(date_obj.strftime('%Y-%m-%d'))  # 再将 datetime 对象格式化为目标字符串 输出：2025-07-24

# datastrs = ['1/1/2025', '1/31/2025']
# [datetime.datetime(2025, 1, 1, 0, 0), datetime.datetime(2025, 1, 31, 0, 0)]
# print([datetime.strptime(x, '%m/%d/%Y') for x in datastrs])


"""
datetime.strptime是在已知格式的情况下转换日期的好方式。然而，每次都必须编写一个格式代码可能有点烦人，特别是对于通用日期格式。
在这种情况下，你可以使用第三方dateutil包的parser.parse方法（这个包在安装pandas时已经自动安装）
"""
# print(parse('2025/07/24'))  # 2025-07-24 00:00:00
# # dateutil能够解析大部分人类可理解的日期表示
# print(parse('Jan 31, 1997 10:45 PM'))  # 1997-01-31 22:45:00
# # 在国际场合下，日期出现在月份之前很常见，因此你可以传递dayfirst=True来表明这种情况
# print(parse('1/1/2025',dayfirst=True))  # 2025-01-01 00:00:00

"""
pandas主要是面向处理日期数组的，无论是用作轴索引还是用作DataFrame中的列。
to_datetime方法可以转换很多不同的日期表示格式。标准日期格式，比如ISO 8601可以非常快地转换.
"""
# datastrs = ['2025/1/1 12:00:00', '2025/2/1 12:00:00']
# print(pd.to_datetime(
#     datastrs))  # DatetimeIndex(['2025-01-01 12:00:00', '2025-02-01 12:00:00'], dtype='datetime64[ns]', freq=None)

# to_datetime方法还可以处理那些被认为是缺失值的值（None、空字符串等）
# idx = pd.to_datetime(datastrs + [None])
# print(idx)  # DatetimeIndex(['2025-01-01 12:00:00', '2025-02-01 12:00:00', 'NaT'], dtype='datetime64[ns]', freq=None)
# print(idx[2])  # NaT
# print(pd.isnull(idx))  # [False False  True]

# NaT（Not a time）是pandas中时间戳数据的是null值。
# dateutil.parser是一个有用但并不完美的工具。值得注意的是，它会将一些字符串识别为你并不想要的日期
# 例如，'42’将被解析为2042年的当前日期。


