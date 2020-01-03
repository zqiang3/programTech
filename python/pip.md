

## 安装pip3

如果通过 homebrew 安装 python3，那么 pip3 会同时安装。所以建议直接通过 homebrew 安装 python3

```bash
brew install python3
apt-get install python3-pip
```

如果你已经通过其他渠道安装了 python3 但是尚未安装 pip3，那么需要通过以下步骤实现安装

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

查看pip3的版本

```
pip3 -V
```





## 安装第三方库

```bash
pip3 install flask
```



## 下载速度慢？

在~(你的用户目录)下创建一个.pip目录，在下面创建一个pip.conf文件，添加以下内容

```bash
[global]
index-url = https://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host=mirrors.aliyun.com
```

