"""
post请求比get请求多一个请求体（form data）

总结
--http请求报文的格式--
请求头\r\n
请求行\r\n
空行（\r\n）
请求体

提示：请求体就是浏览器发送给服务器的数据（如账号密码）



4.小结
·一个HTTP请求报文可以由请求行、请求头、空行和请求体4个部分组成。
·请求行是由三部分组成：
1.请求方式
2.请求资源路径
3.HTTP协议版本
·GET方式的请求报文没有请求体，只有请求行、请求头、空行组成。
·POST方式的请求报文可以有请求行、请求头、空行、请求体四部分组成，注意：POST方式可以允许没有请求体，但是这种格式很少见。
GET和POST请求对比效果图：

"""