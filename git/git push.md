## delete 远程分支

git push origin --delete feature/xxx

等同于
git push origin :master



## 关联远程分支

git push --set-upstream origin xxx

或git push -u origin xxx

命令的最终修改都是针对config文件