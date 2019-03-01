OpenResty 的目标是让你的 Web 服务直接跑在 Nginx 服务内部,充分利用 Nginx 的非阻塞 I/O 模型,不仅仅对 HTTP 客户端请求,甚至于对远程后端诸如 MySQL,PostgreSQL,~Memcaches 以及 ~Redis 等都进行一致的高性能响应。

所以对于一些高性能的服务来说，可以直接使用 OpenResty 访问 Mysql或Redis等，而不需要通过第三方语言（PHP、Python、Ruby）等来访问数据库再返回，这大大提高了应用的性能。

**依赖库**

```bash
apt-get install libreadline-dev libpcre3-dev libssl-dev perl
```

**下载源码包并安装**

```bash
wget https://openresty.org/download/ngx_openresty-1.9.7.1.tar.gz   # 下载
tar xzvf ngx_openresty-1.9.7.1.tar.gz       # 解压
cd ngx_openresty-1.9.7.1/ 
./configure
make 
make install
```

openresty默认安装在/usr/local/openresty目录下。

**启动openresty**

```bash
/usr/local/openresty/nginx/sbin/nginx -p /home/www/ -c /home/www/conf/nginx.conf
```

## 嵌入lua脚本

nginx 如何嵌入 lua 脚本。方法就是在nginx的配置文件nginx.conf 中使用 content_by_lua 或者 cotent_by_lua_file 指令

1. content_by_lua 一般在很简单的lua脚本时使用

```nginx
location /lua {
    set $test "hello, world";
    content_by_lua '
        ngx.header.content_type = "text/plain";
    	nax.say(ngx.var.test);
    ';
}
```

**执行阶段**

```nginx
 location /mixed {
            set_by_lua $a 'ngx.log(ngx.ERR, "set_by_lua")';
            rewrite_by_lua 'ngx.log(ngx.ERR, "rewrite_by_lua")';
            access_by_lua 'ngx.log(ngx.ERR, "access_by_lua")';
            header_filter_by_lua 'ngx.log(ngx.ERR, "body_filter_by_lua")';
            log_by_lua 'ngx.log(ngx.ERR, "log_by_lua")';
            content_by_lua 'ngx.log(ngx.ERR, "content_by_lu")';
}
```

