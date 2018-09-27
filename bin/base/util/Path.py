#!/usr/bin/env python
#! -*- coding:utf-8 -*-
import sys
import os
class Path(object):
    def __init__(self):
        self.path = sys.path[0]
        self.projectPath = self.path[0:self.path.rindex("bin")]
        self.logsDirPath = self.projectPath + "logs"
        self.confPath = self.projectPath + "conf"
        self.shellPath = self.projectPath + "shell"

def getInstance():
    return Path()