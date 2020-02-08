### login shell和non-login shell



- login shell代表用户登入, 比如使用 “su -“ 命令, 或者用 ssh 连接到某一个服务器上, 都会使用该用户默认 shell 启动 login shell 模式。该模式下的 shell 会去自动执行 /etc/profile 和 ~/.profile 文件, 但不会执行任何的 bashrc 文件, 所以一般再 /etc/profile 或者 ~/.profile 里我们会手动去 source bashrc 文件。
- no-login shell 的情况是我们在终端下直接输入 bash 或者 bash -c “CMD” 来启动的 shell。该模式下是不会自动去运行任何的 profile 文件。





