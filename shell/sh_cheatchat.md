```bash
# 注释
# 以#开头的行就是注释
# echo
echo "hello world"
# 变量
NAME="ZQ"      # 等号两边不能有空格
echo ${NAME}   # 大括号是可选的
readonly NAME  # 只读
unset NAME     # 删除变量，不能删除只读变量
# 变量类型
局部变量、环境变量、shell变量
# 字符串
str='this is a string'
str="hello, I know you are \"$your_name\"!"  # 双引号里可以有变量，可以出现转义字符
greeting="hello, "$your_name" !"             # 字符串拼接
echo ${#str}  # 输出字符串长度
# 数组
数组名=(值1 值2 ... 值n)  # 定义数组
echo ${数组名[下标]}      # 读取数组
echo ${array_name[@]}   # 读取数组所有元素
length=${#array_name[@]}  # 获取数组长度
length=${#array_name[*]}
```

