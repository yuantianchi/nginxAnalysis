#!/usr/bin/env python
#! -*- coding:utf-8 -*-
import os
import codecs
import json
from bin.base.log import Logger
L = Logger.getInstance()

class FileUtil(object):
    def __init__(self):
        pass

    def isExistFile(self, path):
        if os.path.exists(path):
            return True
        return False

    def appendToFile(self, path, content):
        try:
            with codecs.open(path, 'a', encoding='utf-8') as f:
                f.write(str(content))
        except Exception as e:
            L.error("add nginxInfo fail to %s ,err:%s" % (str(content), str(e)))

    def createFile(self, path, content):
        try:
            if not os.path.exists(os.path.dirname(path)):
                os.mkdir(os.path.dirname(path))
            with codecs.open(path, 'w', encoding='utf-8') as f:
                f.write(str(content))
        except Exception as e:
            L.error("create %s fail %s" % (str(content), str(e)))

    def createJsonFile(self, path, data):
        try:
            if not os.path.exists(os.path.dirname(path)):
                os.mkdir(os.path.dirname(path))
            with codecs.open(path, 'w', encoding='utf-8') as f:
                f.write(json.dumps(data, ensure_ascii=False, indent=4))
        except Exception as e:
            L.error("create %s fail %s" % (str(data), str(e)))

def getInstance():
    return FileUtil()