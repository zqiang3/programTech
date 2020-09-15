# 邮件MIME调研 实现texp/plain支持

## 定义

MIMI: **Multipurpose Internet Mail Extensions**

全称是多用途互联网邮件扩展

在MIME出台之前，使用RFC 822只能发送基本的ASCII码文本信息

实际上不仅仅是邮件编码，现在MIME经成为HTTP协议标准的一个部分。

## 组成

MIME消息由消息头和消息体两大部分组成。

### 1. 邮件头

MIME格式的邮件头包含了发件人、收件人、主题、时间、MIME版本、邮件内容的类型等重要信息。每条信息称为一个域，由域名后加“: ”和信息内容构成，可以是一行，较长的也可以占用多行。

域的首行必须“顶头”写，即左边不能有空白字符（空格和制表符）；续行则必须以空白字符打头，且第一个空白字符不是信息本身固有的，解码时要过滤掉。

常见的邮件头如下：

| 域名                      | 含义               | 添加者         |
| ------------------------- | ------------------ | -------------- |
| Received                  | 传输路径           | 各级邮件服务器 |
| Return-Path               | 回复地址           | 目标邮件服务器 |
| Delivered-To              | 发送地址           | 目标邮件服务器 |
| Reply-To                  | 回复地址           | 邮件的创建者   |
| From                      | 发件人地址         | 邮件的创建者   |
| To                        | 收件人地址         | 邮件的创建者   |
| Cc                        | 抄送地址           | 邮件的创建者   |
| Bcc                       | 暗送地址           | 邮件的创建者   |
| Date                      | 日期和时间         | 邮件的创建者   |
| Subject                   | 主题               | 邮件的创建者   |
| Message-ID                | 消息ID             | 邮件的创建者   |
| MIME-Version              | MIME版本           | 邮件的创建者   |
| Content-Type              | 内容的类型         | 邮件的创建者   |
| Content-Transfer-Encoding | 内容的传输编码方式 | 邮件的创建者   |

### 1.1 邮件类型（Content-Type）

content-type用来说明下面的邮件正文类型，一般以下面的形式出现。Content-Type: [type]/[subtype]; parameter。

type有以下几种可选：

- Text：用于标准化地表示的文本信息，文本消息可以是多种字符集和或者多种格式的；
- Multipart：用于连接消息体的多个部分构成一个消息，这些部分可以是不同类型的数据；
- Application：用于传输应用程序数据或者二进制数据；
- Message：用于包装一个E-mail消息；
- Image：用于传输静态图片数据；
- Audio：用于传输音频或者音声数据；
- Video：用于传输动态影像数据，可以是与音频编辑在一起的视频数据格式。

subtype用于指定type的详细形式。content-type/subtype配对的集合和与此相关的参数，将随着时间而增长。为了确保这些值在一个有序而且公开的状态下开发，MIME使用Internet Assigned Numbers Authority (IANA)作为中心的注册机制来管理这些值。

常用的subtype值如下所示：

- text/plain（纯文本）
- text/html（HTML文档）
- application/xhtml+xml（XHTML文档）
- image/gif（GIF图像）
- image/jpeg（JPEG图像）【PHP中为：image/pjpeg】
- image/png（PNG图像）【PHP中为：image/x-png】
- video/mpeg（MPEG动画）
- application/octet-stream（任意的二进制数据）
- application/pdf（PDF文档）
- application/msword（Microsoft Word文件）
- message/rfc822（[RFC 822](http://tools.ietf.org/html/rfc822)形式）
- multipart/alternative（HTML邮件的HTML形式和纯文本形式，相同内容使用不同形式表示）
- application/x-www-form-urlencoded（使用HTTP的POST方法提交的表单）
- multipart/form-data（同上，但主要用于表单提交时伴随文件上传的场合）

此外，尚未被接受为正式数据类型的subtype，可以使用x-开始的独立名称（例如application/x-gzip）。vnd-开始的固有名称也可以使用（例：application/vnd.ms-excel）。

**parameter可以用来指定附加的信息，更多情况下是用于指定text/plain和text/html等的文字编码方式的charset参数。**MIME根据type制定了默认的subtype，当客户端不能确定消息的subtype的情况下，消息被看作默认的subtype进行处理。Text默认是text/plain，Application默认是application/octet-stream而Multipart默认情况下被看作multipart/mixed。

### 1.2内容传输编码（Content-Transfer-Encoding），

　　这个区域使指定ASCII以外的字符编码方式成为可能。形式如下：Content-Transfer-Encoding: [mechanism]

其中，mechanism的值可以指定为“7bit”，“8bit”，“binary”，“quoted-printable”，“base64”。

　　7bit这里指的是7位的ASCII编码方式。

　　8位元ASCII码。

　　binary，quoted-printable，因为欧洲的一些文字和ASCII字符集中的某些字符有部分相同。如果邮件消息使用的是这些语言的话，于ASCII重叠的那些字符可以原样使用，ASCII字符集中不存在的字符采用形如“=??”的方法编码。这里“??”需要用将字符编码后的16进制数字来指定。采用quoted-printable编码的消息，长度不会变得太长，而且大部分都是ASCII中的字符，即使不通过解码也大致可以读懂消息的内容。

**base64是一种将二进制的01序列转化成ASCII字符的编码方法。编码后的文本或者二进制消息，就可以运用SMTP等只支持ASCII字符的协议传送了。Base64一般被认为会平均增加33%的报文长度，而且，经过编码的消息对于人类来说是不可读的。**

　　x-encodingname这个值是预留的扩展。



## 2.邮件体

　　邮件内容有各种各样的（既纯文本，超文本，内嵌资源（比如内嵌在超文本中的图片），附件的组合），服务器如何知道该邮件是哪些的混合呢？通过第一个content-type，如果是纯文本该头为：

Content-Type: text/plain; charset=GBK　如果包含了其他内容，邮件体被分为多个段，段中可包含段，每个段又包含段头和段体两部分。content-type为multipart类型。multipart类型分为三种，这三种的关系如下：

![mail_body](/Users/spark/Downloads/mail_body.png)

可以看出，如果在邮件中要添加附件，必须定义multipart/mixed段；如果存在内嵌资源，至少要定义multipart/related段；如果纯文本与超文本共存，至少要定义multipart/alternative段。什么是“至少”？举个例子说，如果只有纯文本与超文本正文，那么在邮件头中将类型扩大化，定义为multipart/related，甚至multipart/mixed，都是允许的。　　

　　multipart诸类型的共同特征是，在段头指定“boundary”参数字符串，段体内的每个子段以此串定界。所有的子段都以“--”+boundary行开始，父段则以“--”+boundary+“--”行结束。段与段之间也以空行分隔。在邮件体是multipart类型的情况下，邮件体的开始部分(第一个“--”+boundary行之前)可以有一些附加的文本行，相当于注释，解码时应忽略。



### Content-Disposition

Content-Disposition属性有两种类型：inline 和 attachment inline ：将文件内容直接显示在页面 attachment：弹出对话框让用户下载