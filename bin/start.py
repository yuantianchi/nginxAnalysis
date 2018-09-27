#!/usr/bin/env python
#! -*- coding:utf-8 -*-

#Author: yuantc
#Create Time: 2018-09-26
import sys
sys.path.append(sys.path[0].replace("/bin", ""))

import os
import subprocess
from bin.base.log import Logger
from bin.base.util import Date, Path, FileUtil, OpJsonFile

if __name__ == '__main__':
    data_Dict = {}
    data_List = []
    P = Path.getInstance()
    O = OpJsonFile.getInstance()
    F = FileUtil.getInstance()
    L = Logger.getInstance()
    confPath = P.confPath + os.sep +"conf.json"
    shellPath = P.shellPath + os.sep + "nginxAnalysis.sh"

    jsonData = O.readFile(confPath)
    date = jsonData.get("date")
    headline = jsonData.get("Headline")
    log_path = jsonData.get("log_path")
    result_file = jsonData.get("result_file")

    if (date == ""):
        date = Date.getInstance().getYesterday()
    log_path = str(log_path) + "/access.log"+str(date)
    if(headline == "" or shellPath == "" or log_path==""):
        L.cri("\033[1;35m nginxAnalysis/conf/conf.json配置文件相关信息未指定\033[0m")
        sys.exit(1)

    #获取调用nginx shell分析脚本
    nginxData = subprocess.Popen(shellPath + ' -d ' + date + '  -n ' + headline + ' -p ' + log_path
, shell=True, stdout=subprocess.PIPE)
    for line in nginxData.stdout.readlines():
        tmpArr = line.strip().decode('utf-8').split()
        dict = {'count': tmpArr[0], 'ip': tmpArr[1], 'data': line.strip().decode('utf-8').lstrip(tmpArr[0]).strip().lstrip(tmpArr[1])}
        data_list = data_List.append(dict)

    if F.isExistFile(result_file):
        nginxData = O.readFile(result_file)
        nginxData[date] = data_List
        O.writeFile(result_file, nginxData)
    else:
        data_Dict[date] = data_List
        F.createJsonFile(result_file, data_Dict)
    L.info("成功获取nginx分析日志到"+result_file)
