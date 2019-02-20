## 函数说明

atoi() 函数会扫描参数 str 字符串，跳过前面的空白字符（例如空格，tab缩进等，可以通过 [isspace()](http://c.biancheng.net/cpp/html/120.html) 函数来检测），直到遇上数字或正负符号才开始做转换，而再遇到非数字或字符串结束时('\0')才结束转换，并将结果返回。



## 把字符串转换为数字

aoi() atol() 和 atof()函数分别把数字的字符串表示转换为int、long和double形式，strtol()、strtoul和 strtod() 分别把数字转换为long、unsigned long 和double 形式。