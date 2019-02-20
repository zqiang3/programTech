## 删除远程仓库所有已合并的分支

可以直接在github上操作，找到'branches'.

There is a red trashcan icon on the side which will delete all branches merged.



## 删除本地已合并的分支

````bash
git br --merged | egrep -v "(^\*|master)" | xargs git br -d
````

