"""
HTTP响应报文

web服务器程序发送给浏览器的http协议的数据



---从服务器拷贝的http相应报文————
--解析--

--相应行（状态行）  由   "协议版本   状态码   状态描述"  组成--
HTTP/1.1 200 OK

--相应头--
Server: nginx

--服务器发送给浏览器的内容类型及编码格式
Content-Type: text/html; charset=UTF-8

--服务器发送给浏览器（客户端程序）的内容长度不确定，
--数据发送结束的接收标识：0\r\n， Content-Length：200（字节）， 服务器发送给客户端的数据确定长度
内容和长度这两个选项只能二选一， 即Transfer-Encoding和Content-Length只能用一个--
Transfer-Encoding: chunked

————和客户端保持长连接————
Connection: keep-alive

————以下都是自定义响应头信息，自己定义相应头的名字和值，如：is_Login：True
Vary: Accept-Encoding
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: *
Content-Encoding: gzip
————空行————
\r\n
----相应体  即真正意义上给浏览器解析使用的数据----
网页数据

# 对于请求头和响应头信息程序员都可以自定义，按照客户端和服务器约定好的方式来制定即可




--http 相应原始报文解析--
--相应行（状态行）  由   "协议版本   状态码   状态描述"  组成--
HTTP/1.1 200 OK\r\n
Server: nginx\r\n
Content-Type: text/html; charset=UTF-8\r\n
Transfer-Encoding: chunked\r\n
Connection: keep-alive\r\n
Vary: Accept-Encoding\r\n
Access-Control-Allow-Credentials: true\r\n
Access-Control-Allow-Methods: GET, POST, PUT, DELETE\r\n
Access-Control-Allow-Headers: *\r\n
Content-Encoding: gzip\r\n
————空行————
\r\n



总结：http相应报文的格式
响应行\r\n
响应头\r\n
空行\r\n
响应体\r\n

提示：每项信息之间必须以\r\n分割


"""