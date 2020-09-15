

## 镜像加速

网易：http://hub-mirror.c.163.com

Docker官方提供的中国镜像库：https://registry.docker-cn.com
七牛云加速器：https://reg-mirror.qiniu.com

## hub

https://hub.docker.com/

## Docker Hello World

```bash
docker run ubuntu:15.10 /bin/echo "hello world"
```

各个参数解析：

- **docker:** Docker 的二进制执行文件。
- **run:** 与前面的 docker 组合来运行一个容器。
- **ubuntu:15.10** 指定要运行的镜像，Docker 首先从本地主机上查找镜像是否存在，如果不存在，Docker 就会从镜像仓库 Docker Hub 下载公共镜像。
- **/bin/echo "Hello world":** 在启动的容器里执行的命令

以上命令完整的意思可以解释为：Docker 以 ubuntu15.10 镜像创建一个新容器，然后在容器里执行 bin/echo "Hello world"，然后输出结果。

## 运行交互式容器

```bash
docker run -i -t ubuntu:15.10 /bin/bash
```

各个参数解析：

- **-t:** 在新容器内指定一个伪终端或终端。
- **-i:** 允许你对容器内的标准输入 (STDIN) 进行交互。

注意第二行 **root@0123ce188bd8:/#**，此时我们已进入一个 ubuntu15.10 系统的容器

我们可以通过运行 exit 命令或者使用 CTRL+D 来退出容器。

## 后台方式启动容器

```bash
docker run -d ubuntu:15.10 /bin/sh -c "while true; do echo hello world; sleep 1; done"
docker ps
docker logs [CONTAINER ID]
docker stop [CONTAINER ID]
```

## help

```bash
docker
docker command --help
```

## command

###容器使用

```bash
# 获取镜像
docker pull ubuntu
# 启动容器
docker run -it ubuntu /bin/bash
# ps
docker ps -a
docker ps -l  # 查询最后一次创建的容器

# 启动一个已停止的容器
docker start [CONTAINER ID]

# 正在运行的容器，可以使用docker restart命令来重启
docker restart

# 后台运行
docker run -itd --name ubuntu-test unbuntu /bin/bash
# -d参数默认不会进入容器，想要进入容器使用指令docker exec

# 停止容器
docker stop [ID或者名字]

# restart
docker restart [ID或者名字]

# 进入窗口
docker attach [ID或者名字]
docker exec [ID或者名字]  # 推荐，此方式退出容器终端，不会导致容器终止

# 导出和导入容器
docker export e282fe92248a > ubuntu.tar

# 删除容器
docker rm -f [ID或者名字]
# 删除容器时，容器必须是停止状态，否则会报错

# 清理所有处于终止状态的容器
docker container prune

# 查看端口映射
docker port [ID或者名字]

# 查看日志
docker logs [ID或者名字]
# -f: 让 docker logs 像使用 tail -f 一样来输出容器内部的标准输出。

# top
docker top [ID或者名字]


# inspect
docker inspect [ID或者名字]

```

###镜像使用

```bash
# images 列出镜像列表
docker images

# search
docker search NAME

# 删除镜像
docker rmi NAME

# 更新镜像
docker commit -m="has update" -a="runoob" e218edb10161 runoob/ubuntu:v2
```

### 容器连接

```bash
# 指定容器绑定的网络地址
docker run -d -p 127.0.0.1:5001:5000 training/webapp python app.py
# 查看端口的绑定情况
docker port adoring_stonebraker 5000
# network
docker network ls
# create network
docker network create -d bridge test-net
```



## 如何构建一个镜像

## Dockerfile

### FROM

**FROM**：定制的镜像都是基于 FROM 的镜像，这里的 nginx 就是定制需要的基础镜像。后续的操作都是基于 nginx。

###RUN

用于执行后面跟着的命令行命令

```bash
RUN <命令行命令>
RUN ["./test.php", "dev", "offline"]
```

Dockerfile 的指令每执行一次都会在 docker 上新建一层。所以过多无意义的层，会造成镜像膨胀过大

```bash
FROM centos
RUN yum install wget
RUN wget -O redis.tar.gz "http://download.redis.io/releases/redis-5.0.3.tar.gz"
RUN tar -xvf redis.tar.gz
以上执行会创建 3 层镜像。可简化为以下格式：
FROM centos
RUN yum install wget \
    && wget -O redis.tar.gz "http://download.redis.io/releases/redis-5.0.3.tar.gz" \
    && tar -xvf redis.tar.gz
```

### COPY

复制指令，从上下文目录中复制文件或者目录到容器里指定路径。

```
COPY [--chown=<user>:<group>] <源路径1>...  <目标路径>
```

```bash
COPY hom* /mydir/
```

### ADD

ADD 指令和 COPY 的使用格式一致（同样需求下，官方推荐使用 COPY）。功能也类似，不同之处如下：

- ADD 的优点：在执行 <源文件> 为 tar 压缩文件的话，压缩格式为 gzip, bzip2 以及 xz 的情况下，会自动复制并解压到 <目标路径>。

- ADD 的缺点：在不解压的前提下，无法复制 tar 压缩文件。会令镜像构建缓存失效，从而可能会令镜像构建变得比较缓慢。具体是否使用，可以根据是否需要自动解压来决定。

  

### CMD

类似于 RUN 指令，用于运行程序，但二者运行的时间点不同:

- CMD 在docker run 时运行。
- RUN 是在 docker build。

CMD 指令指定的程序可被 docker run 命令行参数中指定要运行的程序所覆盖。

如果 Dockerfile 中如果存在多个 CMD 指令，仅最后一个生效。

格式：

```
CMD <shell 命令> 
CMD ["<可执行文件或命令>","<param1>","<param2>",...] 
CMD ["<param1>","<param2>",...]  # 该写法是为 ENTRYPOINT 指令指定的程序提供默认参数
```

推荐使用第二种格式，执行过程比较明确。第一种格式实际上在运行的过程中也会自动转换成第二种格式运行，并且默认可执行文件是 sh。

### ENV

设置环境变量，定义了环境变量，那么在后续的指令中，就可以使用这个环境变量。

格式：

```
ENV <key> <value>
ENV <key1>=<value1> <key2>=<value2>...
```

### ARG

构建参数，与 ENV 作用一至。不过作用域不一样。ARG 设置的环境变量仅对 Dockerfile 内有效，也就是说只有 docker build 的过程中有效，构建好的镜像内不存在此环境变量。

### VOLUME

定义匿名数据卷。在启动容器时忘记挂载数据卷，会自动挂载到匿名卷。

作用：

- 避免重要的数据，因容器重启而丢失，这是非常致命的。
- 避免容器不断变大。

格式：

```
VOLUME ["<路径1>", "<路径2>"...]
VOLUME <路径>
```

### EXPOSE

仅仅只是声明端口。

作用：

- 帮助镜像使用者理解这个镜像服务的守护端口，以方便配置映射。
- 在运行时使用随机端口映射时，也就是 docker run -P 时，会自动随机映射 EXPOSE 的端口。



### WORKDIR

指定工作目录。用 WORKDIR 指定的工作目录，会在构建镜像的每一层中都存在。（WORKDIR 指定的工作目录，必须是提前创建好的）。

docker build 构建镜像过程中的，每一个 RUN 命令都是新建的一层。只有通过 WORKDIR 创建的目录才会一直存在。

格式：

```bash
WORKDIR <工作目录路径>
```

## Docker Compose

Compose 是用于定义和运行多容器 Docker 应用程序的工具。通过 Compose，您可以使用 YML 文件来配置应用程序需要的所有服务。



Compose 使用的三个步骤：

- 使用 Dockerfile 定义应用程序的环境。
- 使用 docker-compose.yml 定义构成应用程序的服务，这样它们可以在隔离环境中一起运行。
- 最后，执行 docker-compose up 命令来启动并运行整个应用程序。

## Get started

### Docker overview

Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. With docker, you can manage your infrastructure in the same ways you manage your applications. By taking advantage of Docker's methodologies for shipping, testing, and deploying code quickly, you can significantly reduce the delay between writing code and running it in production.



### Docker architecture

Docker uses a client-server architecture. The Docker client talks to the Docker daemon, which does the heavy lifting of building, running, and distributing your Docker containers. The Docker client and daemon can run on the same system, or you can connect a Docker client to a remote Docker daemon. The Docker client and daemon communicate using a REST API, over UNIX sockets or a network interface.



####The Docker daemon

The Docker daemon listens for Docker API requests and manages Docker objects such as images, containers, networks, and volumes. A daemon can alse communicate with other daemons to manage Docker services.

####The Docker client

The Docker client is the primary way that many Docker users interact with Docker. When you use commands such as `docker run`, the client sends these commands to `dockerd`, which carries them out. The `docker` command uses the Docker API. The Docker client can communicate with more than one daemon.



### Docker objects

#### IMAGES



#### CONTAINERS

A container is a runnable instance of an image. You can create, start, stop, move, or delete a container using the Docker API or CLI.

By default, a container is relatively well isolated from other containers and its host machine.



### The underlying technology

Docker is written in Go.

#### Namespaces



#### Control groups



#### Union file systems



#### Container format

Docker Engine combines the namespaces, control groups, and UnionFS into a wrapper called a container format. The default container format is `libcontainer`. In the future, Docker may support other container formats by integrating with technologies such as BSD Jails or Solaris Zones.















