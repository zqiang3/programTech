## BLOB

MySQL中，BLOB字段用于存储二进制数据，是一个可以存储大量数据的容器，它能容纳不同大小的数据



、

| 类型       | 大小（字节） |
| ---------- | ------------ |
| TinyBlob   | 最大255      |
| Blob       | 最大65K      |
| MediumBlob | 最大16M      |
| LongBlob   | 最大4G       |



## BLOB与TEXT的区别

一般在保存少量字符串的时候，我们会选择CHAR或者VARCHAR,而在保存较大文本时，通常会选择使用TEXT或者BLOB。二者之间的主要差别是BLOB能用来保存二进制数据，比如照片；而TEXT只能保存字符数据，比如一遍文章或日记。



## 介绍下Base64编码

所谓Base64，就是说选出64个字符----小写字母a-z、大写字母A-Z、数字0-9、符号"+"、"/"（再加上作为垫字的"="，实际上是65个字符）----作为一个基本字符集。然后，其他所有符号都转换成这个字符集中的字符。

```
第一步，将每三个字节作为一组，一共是24个二进制位。

第二步，将这24个二进制位分为四组，每个组有6个二进制位。

第三步，在每组前面加两个00，扩展成32个二进制位，即四个字节。

第四步，根据下表，得到扩展后的每个字节的对应符号，这就是Base64的编码值。

#如果字节数不足三
a）二个字节的情况：将这二个字节的一共16个二进制位，按照上面的规则，转成三组，最后一组除了前面加两个0以外，后面也要加两个0。这样得到一个三位的Base64编码，再在末尾补上一个"="号。

比如，"Ma"这个字符串是两个字节，可以转化成三组00010011、00010110、00010000以后，对应Base64值分别为T、W、E，再补上一个"="号，因此"Ma"的Base64编码就是TWE=。

b）一个字节的情况：将这一个字节的8个二进制位，按照上面的规则转成二组，最后一组除了前面加二个0以外，后面再加4个0。这样得到一个二位的Base64编码，再在末尾补上两个"="号。

比如，"M"这个字母是一个字节，可以转化为二组00010011、00010000，对应的Base64值分别为T、Q，再补上二个"="号，因此"M"的Base64编码就是TQ==。
```

Base64将三个字节转化成四个字节，因此Base64编码后的文本，会比原文本大出三分之一左右。



**中文如何转成base64?**

再举一个中文的例子，汉字"严"如何转化成Base64编码？

这里需要注意，汉字本身可以有多种编码，比如gb2312、utf-8、gbk等等，每一种编码的Base64对应值都不一样。下面的例子以utf-8为例。

首先，"严"的utf-8编码为E4B8A5，写成二进制就是三字节的"11100100 10111000 10100101"。将这个24位的二进制字符串，按照第3节中的规则，转换成四组一共32位的二进制值"00111001 00001011 00100010 00100101"，相应的十进制数为57、11、34、37，它们对应的Base64值就为5、L、i、l。

所以，汉字"严"（utf-8编码）的Base64值就是5Lil。



**base64编码实现**

```javascript
/* Copyright (C) 1999 Masanao Izumo <iz@onicos.co.jp>
* Version: 1.0
* LastModified: Dec 25 1999
* This library is free. You can redistribute it and/or modify it.
*/

/*
* Interfaces:
* b64 = base64encode(data);
* data = base64decode(b64);
*/


var base64EncodeChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
var base64DecodeChars = new Array(
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 62, -1, -1, -1, 63,
52, 53, 54, 55, 56, 57, 58, 59, 60, 61, -1, -1, -1, -1, -1, -1,
-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -1, -1, -1, -1, -1,
-1, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, -1, -1, -1, -1, -1);

function base64encode(str) {
var out, i, len;
var c1, c2, c3;

len = str.length;
i = 0;
out = "";
while(i < len) {
c1 = str.charCodeAt(i++) & 0xff;
if(i == len)
{
out += base64EncodeChars.charAt(c1 >> 2);
out += base64EncodeChars.charAt((c1 & 0x3) << 4);
out += "==";
break;
}
c2 = str.charCodeAt(i++);
if(i == len)
{
out += base64EncodeChars.charAt(c1 >> 2);
out += base64EncodeChars.charAt(((c1 & 0x3)<< 4) | ((c2 & 0xF0) >> 4));
out += base64EncodeChars.charAt((c2 & 0xF) << 2);
out += "=";
break;
}
c3 = str.charCodeAt(i++);
out += base64EncodeChars.charAt(c1 >> 2);
out += base64EncodeChars.charAt(((c1 & 0x3)<< 4) | ((c2 & 0xF0) >> 4));
out += base64EncodeChars.charAt(((c2 & 0xF) << 2) | ((c3 & 0xC0) >>6));
out += base64EncodeChars.charAt(c3 & 0x3F);
}
return out;
}

function base64decode(str) {
var c1, c2, c3, c4;
var i, len, out;

len = str.length;
i = 0;
out = "";
while(i < len) {
/* c1 */
do {
c1 = base64DecodeChars[str.charCodeAt(i++) & 0xff];
} while(i < len && c1 == -1);
if(c1 == -1)
break;

/* c2 */
do {
c2 = base64DecodeChars[str.charCodeAt(i++) & 0xff];
} while(i < len && c2 == -1);
if(c2 == -1)
break;

out += String.fromCharCode((c1 << 2) | ((c2 & 0x30) >> 4));

/* c3 */
do {
c3 = str.charCodeAt(i++) & 0xff;
if(c3 == 61)
return out;
c3 = base64DecodeChars[c3];
} while(i < len && c3 == -1);
if(c3 == -1)
break;

out += String.fromCharCode(((c2 & 0XF) << 4) | ((c3 & 0x3C) >> 2));

/* c4 */
do {
c4 = str.charCodeAt(i++) & 0xff;
if(c4 == 61)
return out;
c4 = base64DecodeChars[c4];
} while(i < len && c4 == -1);
if(c4 == -1)
break;
out += String.fromCharCode(((c3 & 0x03) << 6) | c4);
}
return out;
}
```

