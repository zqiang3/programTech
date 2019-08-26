





# 常用

```bash
git status
git checkout test
git pull --rebase
git add
git commit -am
git push origin master
git merge
git log

# 修改远程仓库地址
git remote set-url origin [url]

# 查看所有分支
git branch -a

# 创建分支
git branch test       # 创建test分支
git checkout -b dev   # 创建并切换分支

# 切换分支
git checkout test

# 从远程checkout
git checkout -b feature/some_feature -t origin/feature/some_feature

# 删除本地分支
git branch -d test
-D  # 强制删除

# 删除远程仓库分支
git push origin :master
等同于
git push origin --delete master

# 推送分支
git push
不带任何参数的git push，默认只推送当前分支，这叫做simple方式。此外，还有一种matching方式，会推送所有有对应的远程分支的本地分支。Git 2.0版本之前，默认采用matching方法，现在改为默认采用simple方式。如果要修改这个设置，可以采用git config命令。

git push origin master
上面命令表示，将本地的master分支推送到origin主机的master分支。如果后者不存在，则会被新建。

# 关联远程分支
git push --set-upstream origin xxx
或git push -u origin xxx
上面命令将本地的master分支推送到origin主机，同时指定origin为默认主机，后面就可以不加任何参数使用git push了

使用场景: 本地新建一个分支后，必须要做远程分支关联。如果没有关联，git会在下面的操作中提示你显示的添加关联。关联目的是如果在本地分支下操作： git pull, git push ，不需要指定在命令行指定远程的分支．
git push --set-upstream origin feature/xxx
命令的最终修改都是针对config文件

# git config
git config --global push.default matching
或者
git config --global push.default simple


# 回退
git reset --hard HEAD^
git reset --hard 3628164
git中，HEAD表示当前版本，上一个版本是HEAD^，上上个版本是HEAD^^，往上100个版本是HEAD~100

# 撤销工作区的修改
git checkout file  # 丢弃工作区的修改,回复到最近一次git commit 或 git add的状态
git checkout 是用版本库里的文件版本替换工作区的版本，无论工作区文件是修改还是删除，都可以还原到版本库的状态。

# 撤销暂存区的修改
git reset HEAD file

# 撤销提交到本地的修改
git reset --hard HEAD^

# git diff
git diff
此命令比较的是工作目录和暂存区快照之间的差异，也就是修改之后还没暂存起来的内容

查看已经暂存起来的文件和上次提交时的快照之间HEAD之间的差异
git diff --cached
git diff --staged

显示工作版本和HEAD的差别
git diff HEAD

直接将两个分支上最新的提交做diff
git diff topic master 或 git diff topic..master

查看简单的diff结果，可以加上--stat参数
git diff --stat

比较两个历史版本之间的差异
git diff SHA1 SHA2


# 删除文件
git rm test.txt

# 拉取文件
git pull
git pull从远程仓库获取最新版本代码并merge到本地。

git pull --rebase
我们在使用git pull命令的时候，可以使用--rebase参数，这里表示把你的本地当前分支里的每个提交(commit)取消掉，并且把它们临时保存为补丁(patch)(这些补丁放到".git/rebase"目录中),然后把本地当前分支更新为最新的"origin"分支，最后把保存的这些补丁应用到本地当前分支上。

git config --global branch.autosetuprebase always  # 所有分支在pull时都使用rebase

# git log
可以加 --pretty=oneline 输出单行日志
git log --graph  可以查看分支合并图
git log --author=
git log --grep="something in the message"
git log --since=2.months.ago --until=1.days.ago

# 命令历史
git reflog
```



# git知识

git是以指针为基础。

git里的origin到底代表什么意思？远程仓库默认被称为origin。

git仓库就是那个.git目录，其中存放的就是我们提交的文档内容，git可基于文档索引对其所管理的文档进行追踪。

在提交时，git创建一个包含提交消息和相关数据的文件，并将其链接到一个树形文件，树形文件包含一个对象列表或者其他树，对象或二进制大数据对象是提交的真正内容，所有这些文件都以对象的SHA-1哈希为文件名进行存储。分支和标签只是一些文件，这些文件包含一个指身提交的SHA-1哈希值。使用这些引用在灵活性和速度上均有大幅提升，创建一个新的分支就和创建一个文件一样简单。

<b>所有的分支指针保存在.git/refs/heads目录下</b>，HEAD在.git/HEAD目录下，标签在.git/refs/tags目录下

<b>暂存区</b>

.git是Git的版本库，版本库中最重要的就是暂存区（称为stage或index）

git add时把文件修改添加到暂存区
git commit时把暂存区内容提交到当前分支

需要提交的文件通通放到暂存区，然后，一次性提交暂存区的所有修改。

提交后，如果工作区没作任何修改，工作区就是干净的(clean)，nothing to commit (working directory clean)。

暂存区是Git非常重要的概念，理解了暂存区是什么，就能明白Git的很多操作到底是在干什么



## origin

远程名称是一个代码仓库别名，git clone默认使用的是origin

## index

文件.git/index 实际上就是一个包含文件索引的目录树，像是一个虚拟的工作区。在这个虚拟工作区的目录树中，记录了文件名、文件的状态信息（时间戳、文件长度等），文件的 内容并不存储其中，而是保存在 Git 对象库（.git/objects）中，文件索引建立了文件和对象库中对象实体之间的对应。

## git diff

使用git diff查看各个区之间的差异

git diff是针对工作区和stage进行比较，如果改动已经加入到了stage中，就不会在git diff中看到。
使用git diff --cached，可比较stage和HEAD中的内容。

git diff 和 git diff --cached容易混淆

git diff 比较的是工作区和暂存区文件的差别

git diff --cached 比较的是暂存区和版本库的差别

git diff HEAD 可以查看工作区和版本库的差别

每次commit后,git diff --cached没有内容，是因为暂存区的内容已经更新到版本库中，因此暂存区和版本库中的内容无差别

## git remote 

git remote set-url origin ssh://git@xxx



## git config

git config --global user.name "your name"
git config --global user.email "your email"




# git status
执行git status命令时，真正发生了什么呢

依据.git/index中记录的文件时间戳、长度等信息判断工作区文件是否改变。如果时刻戳改变，git需要打开文件，读取文件内容和之前的文件相比较。比较之后，如果发现文件内容没有改变，则记录文件新的时间戳。
判断文件是否更改，使用时间戳、文件长度等信息进行比较要比通过文件内容比较要快的多，所以 Git 这样的实现方式可以让工作区状态扫描更快速的执行，这也是 Git 高效的因素之一。
文件.git/index 实际上就是一个包含文件索引的目录树，像是一个虚拟的工作区。在这个虚拟工作区的目录树中，记录了文件名、文件的状态信息（时间戳、文件长度等），文件的 内容并不存储其中，而是保存在 Git 对象库（.git/objects）中，文件索引建立了文件和对象库中对象实体之间的对应。

# git add
当对工作区修改（或新增）的文件执行 “git add” 命令时，暂存区的目录树被更新，同时工作区修改（或新增）的文件内容被写入到对象库中的一个新的对象中，而该对象的ID 被记录在暂存区的文件索引中。

# git commit 
当执行提交操作（git commit）时，暂存区的目录树写到版本库（对象库）中，master 分支会做相应的更新。即 master 指向的目录树就是提交时暂存区的目录树。

# git reset HEAD
当执行 “git reset HEAD” 命令时，暂存区的目录树会被重写，被 master 分支指向的目录树所替换，但是工作区不受影响。

# git rm --cached <file>
当执行 “git rm –cached <file>” 命令时，会直接从暂存区删除文件，工作区则不做出改变。

# git checkout <file>
当执行 “git checkout .” 或者 “git checkout — <file>” 命令时，会用暂存区全部或指定的文件替换工作区的文件。这个操作很危险，会清除工作区中未添加到暂存区的改动。

# git checkout HEAD .
当执行 “git checkout HEAD .” 或者 “git checkout HEAD <file>” 命令时，会用 HEAD 指向的 master 分支中的全部或者部分文件替换暂存区和以及工作区中的文件。这个命令也是极具危险性的，因为不但会清除工作区中未提交的改动，也会清除暂存区中未提交的改 动。





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
git br -vv | grep gone | awk '{print $1}' | xargs git br -d (gone表示远端分支已删除）]




#回滚代码
如果修改还没提交
git reset HEAD lib/foo.b
如果已经提交了一次
git commit -amend
这将圆滚到上一次的提交
回滚本地代码库
git reset --hard commit_id :回滚到commit_id
git reset --hard HEAD~3：将最近3次的提交回滚

回滚远程代码库
应用场景：自动部署系统发布后发现问题，需要回滚到某一个commit，再重新发布
原理：先将本地分支退回到某个commit，删除远程分支，再重新push本地分支

# git blame
寻找谁更改了一个文件中的一行代码经常会用到
git blame FILE
git blame -c FILE
git gui blame FILE

git的维护
git count-objects -v
垃圾回收重复内容
git gc

操作步骤：

1、git checkout develop && git pull
3、git branch backup_branch //备份一下这个分支当前的情况
4、git reset --hard commit_id//把develop本地回滚到commit_id
5、git push origin :develop//删除远程 develop
6、git push origin develop//用回滚后的本地分支重新建立远程分支
7、git branch -d backup_branch//如果前面都成功了，删除这个备份分支

如果使用了gerrit做远程代码中心库和code review平台，需要确保操作git的用户具备分支的push权限，并且选择了 Force Push选项（在push权限设置里有这个选项）

另外，gerrit中心库是个bare库，将HEAD默认指向了master，因此master分支是不能进行删除操作的，最好不要选择删除master分支的策略，换用其他分支。如果一定要这样做，可以考虑到gerrit服务器上修改HEAD指针。。。不建议这样搞



# git push , git pull的默认行为
如果你未曾改动过git config中的push.default属性，根据我们使用的git不同版本（Git 2.0之前或之后），git push通常会有两种截然不同的行为:

develop分支中本地新增的commit被push到远程仓库
push失败，并收到git如下的警告

fatal: The current branch new has no upstream branch.  
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin develop

为什么git版本不同会有两种不同的push行为？

因为在git的全局配置中，有一个push.default属性，其决定了git push操作的默认行为。在Git 2.0之前，这个属性的默认被设为'matching'，2.0之后则被更改为了'simple'。

我们可以通过git version确定当前的git版本（如果小于2.0，更新是个更好的选择），通过git config --global push.default 'option'改变push.default的默认行为（或者也可直接编辑~/.gitconfig文件）。

push.default 有以下几个可选值： 
nothing, current, upstream, simple, matching

其用途分别为：

nothing - push操作无效，除非显式指定远程分支，例如git push origin develop（我觉得。。。可以给那些不愿学git的同事配上此项）。

current - push当前分支到远程同名分支，如果远程同名分支不存在则自动创建同名分支。

upstream - push当前分支到它的upstream分支上（这一项其实用于经常从本地分支push/pull到同一远程仓库的情景，这种模式叫做central workflow）。

simple - simple和upstream是相似的，只有一点不同，simple必须保证本地分支和它的远程 upstream分支同名，否则会拒绝push操作。

matching - push所有本地和远程两端都存在的同名分支。

因此如果我们使用了git2.0之前的版本，push.default = matching，git push后则会推送当前分支代码到远程分支，而2.0之后，push.default = simple，如果没有指定当前分支的upstream分支，就会收到上文的fatal提示。

初次提交本地分支，例如git push origin develop操作，并不会定义当前本地分支的upstream分支，我们可以通过git push --set-upstream origin develop，关联本地develop分支的upstream分支，另一个更为简洁的方式是初次push时，加入-u参数，例如git push -u origin develop，这个操作在push的同时会指定当前分支的upstream



