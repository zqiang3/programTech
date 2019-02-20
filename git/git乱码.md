## linux乱码
在Linux如果要提交的文件名是中文的，默认git commit的时候就会把中文显示为一串数字如下:
```
create mode 100644 "\346\265\213\350\257\225"
```
这个时候只需要添加相应的配置即可显示正常的中文，执行以下命令即可
```bash
git config --global core.quotepath false
```
