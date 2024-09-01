#!/bin/bash


echo "" > sys.info
# 显示日期和时间
echo "==== 系统信息 ====" >> sys.info
date >> sys.info

# 显示系统的运行时间
echo "==== 系统运行时间 ====" >> sys.info
uptime >> sys.info

# 显示CPU信息
echo "==== CPU 信息 ====" >> sys.info
lscpu | grep "Model name\|Socket(s)\|Core(s) per socket\|Thread(s) per core\|CPU(s)" >> sys.info

# 显示CPU使用情况
echo "==== CPU 使用情况 ====" >> sys.info
top -bn1 | grep "Cpu(s)" >> sys.info

# 显示内存使用情况
echo "==== 内存使用情况 ====" >> sys.info
free -h >> sys.info

# 显示磁盘使用情况
echo "==== 磁盘使用情况 ====" >> sys.info
df -h >> sys.info

# 显示交换分区使用情况
echo "==== 交换分区使用情况 ====" >> sys.info
swapon --show >> sys.info

# 显示网络接口的IPv4地址
echo "==== 网络接口的IPv4地址 ====" >> sys.info
ip -4 -o addr show | awk '{print $2 ": " $4}' >> sys.info

# 显示网络流量的概况
echo "==== 网络流量概况 ====" >> sys.info
awk '/^[[:alpha:]]/ {print $1 "接收流量: " $2/1024/1024 "MB 发送流量: " $10/1024/1024 "MB"}' /proc/net/dev >> sys.info

# 显示内存占用最高的三个进程
echo "==== 内存占用最高的三个进程 ====" >> sys.info
ps aux --sort=-%mem | head -4 | tail -3 >> sys.info

# 显示系统负载
echo "==== 系统负载 ====" >> sys.info
cat /proc/loadavg >> sys.info

