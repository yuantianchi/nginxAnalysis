# nginxAnalysis
对nginx日志进行切割，分析记录当天访问次数较多的ip信息，以方便阅读调用的JSON格式保存

使用说明:
运行需要Python3.x环境
1.编辑 conf/conf.json：
                       log_path： 代表nginx日志切割后的保存目录
                       date：     默认为空时查询前一天的nginx日志信息， 若指定日期则只查询指定日期的信息（推荐为空）
                       Headline： 指定记录访问次数最多的前N个Ip信息
                       result_file：指定保存结果信息的文件
2.shell/nginx_log.sh   为日志切割脚本，将其添加到定时任务中，每日执行一次。并为其指定创建切割日志文件存放的目录
3.添加nginxAnalysis到定时任务每日执行一次。bin/star.py为程序入口


                       
