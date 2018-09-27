#!/usr/bin/env python
# -*-  coding:utf-8 -*-
import logging
import os

from bin.base.util import Path

logPath = Path.getInstance().logsDirPath


class Logger(logging.Logger):
    def __init__(self, filename=None):
        super(Logger, self).__init__(self)
        self.log_all = logPath + os.sep + "log.log"
        # formatter = logging.Formatter('[%(asctime)s] - %(filename)s [Line:%(lineno)d] - [%(levelname)s]-[thread:%(thread)s]-[process:%(process)s] - %(message)s')
        formatter = logging.Formatter('[%(levelname)8s]-[%(asctime)s]-%(filename)s :Line:%(lineno)d : %(message)s')
        # 日志文件名
        if filename is not None:
            self.log_all = logPath + os.sep + filename
        # 定义一个RotatingFileHandler，按照大小自动分割日志文件，一旦达到指定的大小重新生成文件  最多备份1个日志文件，每个日志文件最大1M
        # delay为true时，文件直到emit方法被执行才会打开。默认情况下，日志文件可以无限增大。
        # mode = 'a'    模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
        # rHandler = RotatingFileHandler(self.log, maxBytes=1024*1024, encoding='utf-8', delay=False)
        fh_all = logging.handlers.RotatingFileHandler(self.log_all, mode='a', maxBytes=1024 * 1024, backupCount=100, encoding='utf-8', delay=0)
        fh_all.setLevel(logging.DEBUG)
        fh_all.setFormatter(formatter)  # 定义handler的输出格式
        self.addHandler(fh_all)


        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)  # 定义handler的输出格式
        self.addHandler(ch)  # 给logger添加handler


def getInstance(filename=None):
    return Logger(filename)


if __name__ == "__main__":
    getInstance().info("AAAA")
