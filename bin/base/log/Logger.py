#!/usr/bin/env python
# -*-  coding:utf-8 -*-
import logging
import logging.handlers
import os

from bin.base.util import Path


class Logger():
    def __init__(self, path, clevel=logging.DEBUG, Flevel=logging.DEBUG):

        self.logger = logging.getLogger(path)  ##设置日志输出文件
        self.logger.setLevel(logging.DEBUG) ##设置日志输出等级，即只有日志级别大于等于该级别的日志才会输出
        fmt = logging.Formatter('[%(levelname)8s]-[%(asctime)s]-%(filename)s :Line:%(lineno)d : %(message)s')#日志格式
        # 设置CMD日志
        # sh = logging.StreamHandler()
        # sh.setFormatter(fmt)
        # sh.setLevel(clevel)

        # 设置文件日志
        fh = logging.FileHandler(path)
        fh.setFormatter(fmt)
        fh.setLevel(Flevel)
        # self.logger.addHandler(sh)
        self.logger.addHandler(fh)# 为Logger实例增加一个处理器


    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def war(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def cri(self, message):
        self.logger.critical(message)


def getInstance():
    logPath = Path.getInstance().logsDirPath
    log_Path = logPath + os.sep + "log.log"
    return Logger(log_Path)

