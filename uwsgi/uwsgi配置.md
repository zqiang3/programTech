## 链接

<https://uwsgi-docs-zh.readthedocs.io/zh_CN/latest/ConfigLogic.html>



## if-env

检查是否定义了一个环境变量，将其值放在上下文占位符中。

```bash
[uwsgi]
if-env = PATH
print = Your path is %(_)
check-static = /var/www
endif =
socket = :3031
```

## 示例

```bash
if-env = NUM_PROCESSES
processes=%(_)
endif =
if-not-env = NUM_PROCESSES
processes=90
endif =
```

