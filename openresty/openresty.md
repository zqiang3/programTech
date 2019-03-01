## 链接

https://blog.csdn.net/u012618915/article/details/81301258

http://wiki.jikexueyuan.com/project/openresty-best-practice/log.html  OpenResty最佳实践

## 学习资料

https://github.com/openresty/lua-nginx-module 
nginx 所有模块说明 
http://nginx.org/en/docs/ 
这都是最原始的资料， 里面也是最官方的说明， 内容非常好，必备网址 
openresty是nginx lua的打包程序并对其做了优化， 所以openresty的说明也是官方，必备， 有一点特别好， 中国人自己写的， 所以有中文版，对于像我这样英文不怎么好的人来说就是一个福音 
https://legacy.gitbook.com/book/moonbingbing/openresty-best-practices/details 
http://openresty.org/cn/ 
那搭建openresy nginx+lua开发环境呢，我本身是做流媒体开发的，所以我都是整体编译的。环境搭建过程请看我之前博客 

https://blog.csdn.net/u012618915/article/details/81180421 

## 介绍

openresty是什么？openresty可理解为是nginx web服务器的一个超集，并集成了lua即时解释器。lua的优势在于速度很快。总结来说，openresty包含了许多精良的lua库，大量高效的第三方nginx模块和大部分的外部依赖。它的目标是帮助开发者容易地构建可扩展的web应用，web服务和动态网关。

OpenResty is a full-fledged web application server by boundling the standard Nginx core, lots of 3rd-party Nginx modules, as well as mos of their external dependencies.

## 原理

Nginx 采用的是 master-worker 模型，一个 master 进程管理多个 worker 进程，基本的事件处理都是放在 woker 中，master 负责一些全局初始化，以及对 worker 的管理。

在OpenResty中，每个worker使用一个LuaVM，当请求被分配

## 安装部署

You can add the `openresty` repository to your Debian system so as to easily install our packages and receive updates in the future (via the `apt-get update`command). To add the repository, just run the following commands (only need to run once for each system):

```bash
wget -qO - https://openresty.org/package/pubkey.gpg |  apt-key add -
apt-get -y install software-properties-common
add-apt-repository -y "deb http://openresty.org/package/debian $(lsb_release -sc) openresty"  
apt-get update
# 以上每个系统只需执行一次
apt-get install openresty
```

## 安装目录

/usr/local/openresty



## 用法

```bash
/opt/openresty/nginx/sbin/nginx -c /opt/openresty/nginx/conf/nginx.conf -p /opt/openresty/nginx/

# reload
/usr/local/openresty/nginx/sbin/nginx -p /home/www/ -c /home/www/conf/nginx.conf -s reload
```

```nginx
content_by_lua 'ngx.say("hello world")'; 
```

## 利用lua实现通用的输入输出日志打印

**教程**

https://github.com/openresty/lua-nginx-module