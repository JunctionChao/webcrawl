#!/usr/bin/env python
# -*- coding: utf-8 -*-



import datetime, time

# 今天日期
today = datetime.date.today()
print(today, type(today))

# 今天开始时间戳
today_start_timestamp = int(time.mktime(time.strptime(str(today), '%Y-%m-%d')))
print(today_start_timestamp)


# 今天结束时间戳
tomorrow = today + datetime.timedelta(days=1)
today_end_timestamp = int(time.mktime(time.strptime(str(tomorrow), '%Y-%m-%d'))) - 1
print(today_end_timestamp)


import random
print(random.randint(today_start_timestamp, today_end_timestamp)) # 生成今天随机时间的时间戳

# 生成n位随机数
import string

def random_num(random_len=3):
     digit = list(string.digits)
     random.shuffle(digit)
     return ''.join(digit[:random_len])

print(random_num(3))