## 虚拟主机
利用虚拟主机，不需要为每个网站提供一台单独的Nginx服务器或运行一组Nginx进程。虚拟主机提供了在同一台服务器、同一组Nginx进程上运行多个网站的功能。

```bash
http
{
    server
    {
        listen 80 default;
        server_name _ *;
        access_log logs/default.access.log combined;
```

## 客户端的真实IP
如果将nginx作为web服务器，位于负载均衡设备、Squid、Nginx反射代理之后，就不能获取到客户端的真实IP了。原因是在客户端和Web服务器之间增加了中间层，$remote_addr拿到的是反射代理服务器的IP地址
在日志格式中，变量$remote_addr和$http_x_forwarded_for用于记录IP地址。$http_referer用于记录是从哪个页面链接访问过来的；$http_user_agent用于记录客户端浏览器的相关信息。

## FastCGI
FastCGI是语言无关的、可伸缩架构的CGI开放扩展，其主要行为是将CGI解释器进程保持在内存中并因此获得较高的性能。众所周知，CGI解释器的反复加载是CGI性能低下的主要原因，如果CGI解释器保持在内存中并接受FastCGI进程器调度，则可以提供良好的性能、伸缩性、Fail-Over特性等。

