% cat > seqno  

^D  Ctrl+D is our terminal end-of-file character



## 几种用法

1. cat << EOF 以EOF输入字符为标准输入结束
2. cat > filename 创建文件，并把标准输入输出到filename文件中，以ctrl+d为输入结束
3. cat << EOF >> filename 追加文件，以EOF为结束符