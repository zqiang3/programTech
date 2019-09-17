du -sh # 查看该目录总的大小

du -sh *

查看整个磁盘剩余多少空间
df -h
df -hl

当前文件夹的磁盘使用情况
du --max-depth=1 -h
# -h human readable
# 得到结果中，前面n-1行的是该目录下每个文件夹的大小。最后一行显示的是该目录总的大小


# 排除隐藏文件
du -ah --max-depth=1 --exclude="*/.*

# 如何找到最大的文件
du -sh * | sort -nr
