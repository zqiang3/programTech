**只有少量提交时使用变基。**

大部分情况下的提交修改内容并不会受他人影响，所以可以使用 `git pull --rebase` 进行拉取，此操作会重新生成已有的提交，会导致提交时间修改，但是作者时间保持不变。





## 合并几次提交

```bash
git rebase -i  [startpoint]  [endpoint]
```

其中`-i`的意思是`--interactive`，即弹出交互式的界面让用户编辑完成合并操作，`[startpoint]` `[endpoint]`则指定了一个编辑区间，如果不指定`[endpoint]`，则该区间的终点默认是当前分支`HEAD`所指向的`commit`(注：该区间指定的是一个前开后闭的区间)。
在查看到了log日志后，我们运行以下命令：

```
git rebase -i 36224db
git rebase -i HEAD~3
```

命令说明：

- pick：保留该commit（缩写:p）
- reword：保留该commit，但我需要修改该commit的注释（缩写:r）
- edit：保留该commit, 但我要停下来修改该提交(不仅仅修改注释)（缩写:e）
- squash：将该commit和前一个commit合并（缩写:s）
- fixup：将该commit和前一个commit合并，但我不要保留该提交的注释信息（缩写:f）
- exec：执行shell命令（缩写:x）
- drop：我要丢弃该commit（缩写:d）