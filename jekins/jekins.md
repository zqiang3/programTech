## log

Jenkins initial setup is required. An admin user has been created and a password generated.
Please use the following password to proceed to installation:

a3604701b24f49be92b64e023706b206



## localhost:8080

为了确保管理员安全地安装 Jenkins，密码已写入到日志中（[不知道在哪里？](https://jenkins.io/redirect/find-jenkins-logs)）该文件在服务器上：

```
/Users/spark/.jenkins/secrets/initialAdminPassword
```



## user

zqiang.3

zhangqiang.3@bytedance.com



## agent 

 `agent` 指令告诉Jenkins在哪里以及如何执行Pipeline或者Pipeline子集。 正如您所预料的，所有的Pipeline都需要 `agent` 指令。

流水线代码块顶部的 [`agent`](https://jenkins.io/doc/book/pipeline/syntax#agent) 部分指定的的 `none` 参数意味着不会为 整个流水线的执行分配全局代理 ，并且每个 [`stage`](https://jenkins.io/doc/book/pipeline/syntax/#stage) 指令必须制定自己的 `agent` 部分。



## 使用环境变量

```bash
Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any

    environment {
        DISABLE_AUTH = 'true'
        DB_ENGINE    = 'sqlite'
    }

    stages {
        stage('Build') {
            steps {
                sh 'printenv'
            }
        }
    }
}
```

## 记录和收集结果

为了收集我们的测试结果，我们将使用 `post` 部分。

```bash
Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh './gradlew check'
            }
        }
    }
    post {
        always {
            junit 'build/reports/**/*.xml'
        }
    }
}
```



## Why Pipeline?

https://jenkins.io/zh/doc/book/pipeline/

本质上，Jenkins 是一个自动化引擎，它支持许多自动模式。 流水线向Jenkins中添加了一组强大的工具, 支持用例 简单的持续集成到全面的CD流水线。通过对一系列的相关任务进行建模, 用户可以利用流水线的很多特性:

- **Code**: 流水线是在代码中实现的，通常会检查到源代码控制, 使团队有编辑, 审查和迭代他们的交付流水线的能力。
- **Durable**: 流水线可以从Jenkins的主分支的计划内和计划外的重启中存活下来。
- **Pausable**: 流水线可以有选择的停止或等待人工输入或批准，然后才能继续运行流水线。
- **Versatile**: 流水线支持复杂的现实世界的 CD 需求, 包括fork/join, 循环, 并行执行工作的能力。
- **Extensible**:流水线插件支持扩展到它的DSL [[1](https://jenkins.io/zh/doc/book/pipeline/#_footnotedef_1)]的惯例和与其他插件集成的多个选项。



## 切换语言

中文转English
安装插件：
系统管理 ／ 插件管理，打开“可选插件”，选择locale 插件，点击“下载待重启后安装“按钮安装。

勾选“安装完成后重启Jenkins“

设置语言
系统管理 ／ 系统设置，找到Locale

输入Default Language为en_US

勾选“Ignore browser preference and force this language to all users“

保存


## CI/CD

continuous integration: 持续集成

continuous delivery: 持续交付

## Usage

1. 点击左侧的“新建”