scp一般有六种使用方法
本地复制远程文件：（把远程的文件复制到本地）
scp root@www.test.com:/val/test/test.tar.gz /val/test/test.tar.gz
远程复制本地文件：（把本地的文件复制到远程主机上）
scp /val/test.tar.gz root@www.test.com:/val/test.tar.gz
本地复制远程目录：（把远程的目录复制到本地）
scp -r root@www.test.com:/val/test/ /val/test/
远程复制本地目录：（把本地的目录复制到远程主机上）
scp -r ./ubuntu_env/ root@192.168.0.111:/home/pipi

