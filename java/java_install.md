## 1. 点击进入下载页

https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html

下载mac 64位 dmg安装馆藏

## 2. 安装

双击dmg安装馆藏，再双击pkg文件，即开始安装。

## 3. 配置系统的环境变量

由于MAC文件系统结构与windows有所不一样，所以jdk真实的主目录路径如下

/Library/Java/JavaVirtualMachines/jdk1.8.0_144.jdk/Contents/Home

在.bash_profile配置下面内容

```bash
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_45.jdk/Contents/Home
```

## 4. 验证

```bash
java
java -version
```

