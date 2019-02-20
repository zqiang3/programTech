## linux方法
```
bash
cd ~
touch .git-credentials
vim .git-credentials
https://{username}:{password}@github.com
```

在终端下输入：
```
bash
git config --global credential.helper store
```
