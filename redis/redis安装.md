## link

https://www.jianshu.com/p/bc84b2b71c1c



## 安装配置过程

```bash
# 下载
wget http://download.redis.io/releases/redis-3.0.0.tar.gz
# 解压
cp redis-3.0.0.rar.gz /usr/local
tar -zxvf redis-3.0.0.tar.gz

# make
cd /usr/local/redis-3.0.0
make PREFIX=/usr/local/redis install

# 拷贝配置文件到安装目录
cd /usr/local/redis
cp /usr/local/redis-3.0.0/redis.conf  /usr/local/redis/bin

# 后端模式启动
修改redis.conf配置文件， daemonize yes 以后端模式启动

# 启动redis
cd /usr/local/redis
./bin/redis-server ./redis.conf

# 连接redis
/usr/local/redis/bin/redis-cli 

# 关闭redis
cd /usr/local/redis
./bin/redis-cli shutdown

# 强行终止redis
pkill redis-server

# 开机自启动
vim /etc/rc.local
//添加
/usr/local/redis/bin/redis-server /usr/local/redis/etc/redis-conf
```

