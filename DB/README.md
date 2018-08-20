DB
--

MongoDB 安装步骤

## 1. 下载
`curl -O https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu1604-3.4.16.tgz`

## 2. 解压
tar -vzxf mongodb-linux-x86_64-ubuntu1604-3.4.16.tgz

## 3.新建目录
mkdir -p /data/db
mkdir -p /data/logs

## 4. 新建启动配置 mongodb.conf
```
cd /bin
vi mongodb.conf
```
内容如下：
```
dbpath = /data/db #数据文件存放目录  
logpath = /data/logs/mongodb.log #日志文件存放目录  
port = 27017  #端口  
fork = true  #以守护程序的方式启用，即在后台运行  
```

## 5. 启动数据库
cd /bin
./mongod -f mongodb.conf
