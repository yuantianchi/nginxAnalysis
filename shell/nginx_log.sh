#nginx日志切割脚本

#!/bin/bash
#设置日志文件存放目录
logs_path="/usr/local/nginx/logs"
#设置pid文件
pid_path="/usr/local/nginx/logs/nginx.pid"

#重命名日志文件
mv ${logs_path}/error.log ${logs_path}/error_logs/$(date -d "yesterday" +"%Y%m%d").log
mv ${logs_path}/access.log ${logs_path}/info_logs/$(date -d "yesterday" +"%Y%m%d").log

find ${logs_path}/error_logs/ -mtime +7 -exec rm -rf {} \;
find ${logs_path}/info_logs/ -mtime +7 -exec rm -rf {} \;


#向nginx主进程发信号重新打开日志
kill -USR1 `cat ${pid_path}`
