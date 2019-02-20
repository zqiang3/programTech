```bash
cat /etc/mtab    # 显示当前系统已挂载的所有设备
cat /proc/mounts # 查看内核追踪到的已挂载的所有设备
fdisk -l
mount /dev/vda1 /device
df
blkid /dev/vda1
umount /device
```

## 对挂载目录的要求

1. 目录必须存在
2. 挂载点目录不可被其他进程使用
3. 挂载点原文件将被暂时隐藏

## 挂载方法

```bash
mount [-fnrsvw] [-t vfstype] [-o options] device dir
```

1. 设备文件：如/dev/sda5
2. 卷标：-L 'LABEL'
3. UUID, -U 'UUID'
4. 伪文件系统名称：proc, sysfs, devtmp, configfs

**常用命令选项**

* -t vsftype 指定文件系统类型

* -r readonly

* -w read and write

* -n 不更新/etc/mtab

* **-a**：自动挂载所有支持自动挂载的设备；(定义在了/etc/fstab文件中，且挂载选项中有“自动挂载”功能) 

  

**-o optins**

* async
* sync
* atime/noatime
* diratime/nodiratime
* auto/noauto
* exec/noexec
* dev/nodev
* suid/nosuid
* remount
* ro
* rw
* user/nouser
* acl 启用此文件系统上的acl功能 

