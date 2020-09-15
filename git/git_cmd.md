## 删除远程仓库所有已合并的分支

可以直接在github上操作，找到'branches'.

There is a red trashcan icon on the side which will delete all branches merged.



## 删除本地已合并的分支

````bash
git br --merged | egrep -v "(^\*|master)" | xargs git br -d
````



## 删除远程分支

```bash
git b -r | grep szq | awk -F '/' '{print $2}' | xargs -I {} git push origin :{}

git b | grep -v master | xargs git b -D

git branch -r --merged | awk -F '/' '{print $2}' | xargs -I {} git push origin :{}

# -r 列出远程分支
# --merged列出已合并到当前分支的分支
# -F ‘/’ 已斜杠分割字符串 ， 因为branch命令加了-r参数，输出类似‘origin/bugfix1’, 分割后结果为 origin bugfix1
‘{print $2}’输出分隔后的第二部门
# -I 指定占位符
```

## git pull --rebase

```
git pull --rebase
git push
```

The full syntax is:

```
git pull --rebase origin master
git push origin master
```

## git push -u origin master

I would recommend a:

```
git push -u origin master
```

That would establish a tracking relationship between your local master branch and its upstream branch.
After that, any future push for that branch can be done with a simple:

```
git push
```