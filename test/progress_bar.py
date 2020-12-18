#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2020-11-22
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

import time,sys
 
for i in range(1, 101):
    percent = i / 100
    sys.stdout.write("\r{0}{1}".format("|"*i , '%.2f%%' % (percent * 100)))
    sys.stdout.flush()
    time.sleep(0.5)