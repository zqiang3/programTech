## 下载

```
brew install chronograf
```



## 启动

```
sudo chronograf
```



## 打开web管理页面

```
http://localhost:8888/
```





## 依赖

```
To have launchd start kapacitor now and restart at login:
  brew services start kapacitor
Or, if you don't want/need a background service you can just run:
  kapacitord -config /usr/local/etc/kapacitor.conf
```



## info

```
/usr/local/Cellar/kapacitor/1.5.5: 6 files, 83.7MB

To have launchd start chronograf now and restart at login:
  brew services start chronograf
Or, if you don't want/need a background service you can just run:
  chronograf
```

