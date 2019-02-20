## Tools

Deployment->configuration

### Connection

Host: 127.0.0.1 Port: xxx

User name: xxx

Authentication: **Key pair**

Private key path: rsa文件

### Mappings

Local path: windows目录

Deployment path: relative to the server root path



## 解释器设置

Settings->Project->Project Interpreter

点击Add，选择SSH Interpreter(表示远程解释器)

选择sftp（已配置），再填入远程解释器路径

## Edit Configurations

Script path: 解释器 脚本文件

Parameters: 参数