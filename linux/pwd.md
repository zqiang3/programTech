## pwdx

report current working directory of a process

## Synopsis

```
pwdx pids...
pwdx -V
```

## Description

The pwdx command reports the current working directory of a process or processes





## pwd

pwd 可以打印当前路径，但是也不一定是脚本的位置。

```bash
lcd:/home/lcd/shell/ $ bash ./mytest.sh 
# pwd=/home/lcd/shell/
lcd:/home/lcd/ $ bash ./shell/mytest.sh
# pwd=/home/lcd/
lcd:/root/ $bash /home/lcd/shell/mytest.sh
# pwd=/root/
```

可见，只有第一条的执行情况才满足实际需要，pwd  打印的是你站在那里，而不是脚本在哪里。

