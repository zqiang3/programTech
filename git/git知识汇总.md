## origin

远程名称是一个代码仓库别名，git clone默认使用的是origin

## index

文件.git/index 实际上就是一个包含文件索引的目录树，像是一个虚拟的工作区。在这个虚拟工作区的目录树中，记录了文件名、文件的状态信息（时间戳、文件长度等），文件的 内容并不存储其中，而是保存在 Git 对象库（.git/objects）中，文件索引建立了文件和对象库中对象实体之间的对应。

## git diff

git diff是针对工作区和stage进行比较，如果改动已经加入到了stage中，就不会在git diff中看到。
使用git diff --cached，可比较stage和HEAD中的内容。

## git remote 

git remote set-url origin ssh://git@git-cc.nie.netease.com:32200/microservice/mvideoquery.git



## git config

git config --global user.name "your name"
git config --global user.email "your email"



## 不产生无用的merge分支
有这么一种情况，用一个分支专门同步代码提供商的代码的时候，如果一般的pull会不断的产生一个merge看起来会很烦，用下边的使用添加一个--rebase就不会产生无用的merge了
$ git pull --rebase origin master



## 忽略机制

工作目录中有一些文件是不希望接受管理的，比如生成的临时文件等。可将工作目录不希望接受管理的文档写到同一目录的.gitignore文件中



## 清理本地分支 

// 拉取远程到本地，并更新本地和远程的对应关系

 git fetch -p

// 显示本地分支和服务器分支的映射关系
git branch -vv

// 显示本地、服务器所有分支
git branch -a

然后再执行 删除本地分支（远程已经没有的对应的分支）

$ git branch -r | awk '{print $1}' | egrep -v -f /dev/fd/0 <(git branch -vv | grep origin) | awk '{print $1}' | xargs git branch -d

上面不可用，使用下面的命令
git br -vv | grep gone | awk '{print $1}' | xargs git br -d (gone表示远端分支已删除）

## git

git里的origin到底代表什么意思
远程仓库默认被称为origin

在~/.gitconfig文件里进行别名设置
[alias]
​    st = status
​    ci = commit
​    br = branch
​    co = checkout
​    df = diff

文件.git/index 实际上就是一个包含文件索引的目录树，像是一个虚拟的工作区。在这个虚拟工作区的目录树中，记录了文件名、文件的状态信息（时间戳、文件长度等），文件的 内容并不存储其中，而是保存在 Git 对象库（.git/objects）中，文件索引建立了文件和对象库中对象实体之间的对应。

当对工作区修改（或新增）的文件执行 "git add" 命令时，暂存区的目录树被更新，同时工作区修改（或新增）的文件内容被写入到对象库中的一个新的对象中，而该对象的ID被记录在暂存区的文件索引中。

当执行提交操作（git commit）时，暂存区的目录树写到版本库（对象库）中，master分支会做相应的更新。即 master 指向的目录树就是提交时暂存区的目录树。

当执行 "git reset HEAD" 命令时，暂存区的目录树会被重写，被 master 分支指向的目录树所替换，但是工作区不受影响。

 当执行 "git rm --cached <file>" 命令时，会直接从暂存区删除文件，工作区则不做出改变。

当执行 "git checkout ." 或者 "git checkout -- <file>" 命令时，会用暂存区全部或指定的文件替换工作区的文件。这个操作很危险，会清除工作区中未添加到暂存区的改动。

当执行 "git checkout HEAD ." 或者 "git checkout HEAD <file>" 命令时，会用 HEAD 指向的 master 分支中的全部或者部分文件替换暂存区和以及工作区中的文件。这个命令也是极具危险性的，因为不但会清除工作区中未提交的改动，也会清除暂存区中未提交的改动。

使用git diff查看各个区之间的差异
git diff 和 git diff --cached容易混淆

git diff 比较的是工作区和暂存区的差别

git diff --cached 比较的是暂存区和版本库的差别

git diff HEAD 可以查看工作区和版本库的差别

每次commit后,git diff --cached没有内容，是因为暂存区的内容已经更新到版本库中，因此暂存区和版本库中的内容无差别



git仓库就是那个.git目录，其中存放的就是我们提交的文档内容，git可基于文档索引对其所管理的文档进行追踪。

