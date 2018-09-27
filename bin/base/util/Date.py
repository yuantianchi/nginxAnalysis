#!/usr/bin/env python
#! -*- coding:utf-8 -*-

import datetime

class Data(object):
    def __init__(self):
        pass

    def getYesterday(self):
        today = datetime.date.today()
        oneday = datetime.timedelta(days=1)
        yesterday = today-oneday
        return yesterday.strftime('%Y%m%d')

def getInstance():
    return Data()