#! /bin/bash
#d,date,欲查看的日期。n,number,要查看调用次数排名前多少行的数据。p,path和name,nginx日志绝对路径和文件名。
touch testwrite_HIuyhuiIH ||exit 1
rm -f testwrite_HIuyhuiIH 
while getopts ":d:n:p:" opt;
do
   case $opt in
   d) date=$OPTARG;;
   n) number=$OPTARG;;
   p) pandn=$OPTARG;;
  \?) exit ;;
  esac
done
if [ "${date}" == "" ]||[ "${number}" == "" ]||[ "${pandn}" == "" ]
then
echo "少参数!" 
	exit 
else
	true
fi
year=${date:0-8:4}
month=${date:0-4:2}
day=${date:0-2:2}
monthnoToletter() {
case $month in
  01 ) month="Jan"  ;;
  02 ) month="Feb"  ;;
  03 ) month="Mar"  ;;
  04 ) month="Apr"  ;;
  05 ) month="May"  ;;
  06 ) month="Jun"  ;;
  07 ) month="Jul"  ;;
  08 ) month="Aug"  ;;
  09 ) month="Sep"  ;;
  10) month="Oct"  ;;
  11) month="Nov"  ;;
  12) month="Dec"  ;;
  * ) echo " 未知月份 $month" >&2; exit 1
  esac
return 0
 }
monthnoToletter
printpost () {
grep "$day/$month/$year:[0-23]" ${pandn}|grep "hnis/services/com.longrise.services.leap"|grep "importCaseinfo" >logged2333
awk '{print $1}' logged2333| sort | uniq -c | sort -n -k 1 -r | head -n ${number} | while read line    # 修改点！！    # sort(其实省略了-t分隔符选项，默认空格作为分隔符),-n按照字符串数值,字母顺序等常规排序，-k 1,参照第一个值（域），-r倒序。
do
ip=`echo ${line}|awk '{print $2}'` 
req_ip=`grep "${ip}" logged2333|head -1` #修改点  ！！！             #grep  log中包含数组里的ip,给定格式的时间,再以"作为分隔符,awk输出第二个域,即 nginx的request字段. 
echo  "${line} ${req_ip}"
done
}
printpost # >output
if [ -f "logged2333" ];then
rm -f logged2333 
else
echo "logged2333 not exist"
exit 1
fi
