dig命令主要用来从DNS域名服务器查询主机地址信息。

```bash
dig baidu.com
dig baidu.com CNAME
dig @8.8.8.8 baidu.com
dig +short baidu.com
dig abc.filterinto.com +noall +answer
dig +trace abc.filterinto.com

```

