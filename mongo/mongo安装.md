```bash
$ apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
gpg: Total number processed: 1
gpg:               imported: 1  (RSA: 1)

$ echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
$ apt-get update
$ apt-get install -y mongodb-org
# This command will install several packages containing latest stable version of MongoDB along with helpful management tools for the MongoDB server.

$ systemctl start mongod
$ systemctl status mongod
$ systemctl enable mongod
# The last step is to enable automatically starting MongoDB when the system starts.
```





## windows安装

设置存放数据库文件的路径,在mongodb下新建一个data的文件夹, 里面新建一个log文件夹用来存储日志

cd 到bin目录
mongod.exe --dbpath=d:/mongo/data

注册MongoDB的服务
D:\development\mongodb\bin\mongod.exe --dbpath=d:\development\mongodb\data -install --logpath=D:\development\mongodb\data\log\mongo.log
注册完了服务之后net start MongoDB启动