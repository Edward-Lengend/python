"""
1.URL的概念
URL的英文全拼是（Uniform Resoure Locator），表达的意思是统一资源定位符，
通俗理解就是网络资源地址，也就是我们常说的网址。
2.URL的组成
URL的样子：
https://news.163.com/18/1122/10/E178J204000189FH.html URL的组成部分：
1.协议部分：https://、http://、ftp:/∥
 https是加密的http
 http默认端口号为80，https默认端口号为443
2.域名部分：news.163.com
3.资源路径部分：/18/1122/10/E178J204000189FH.html域名：
     域名就是IP地址的别名，它是用点进行分割使用英文字母和数字组成的名字，
     使用域名目的就是方便的记住某台主机IP地址。

     URL的扩展：
https://news.163.com/hello.html？page=1&count=10
·查询参数部分：？page=1&count=10参数说明：
·？后面的page表示第一个参数，后面的参数都使用&进行连接



3.小结
·URL就是网络资源的地址，简称网址，通过URL能够找到网络中对应的资源数据。
·URL组成部分
1.协议部分2.域名部分
3.资源路径部分
4.查询参数部分[可选]

·谷歌浏览器的开发者工具是查看http协议的通信过程利器，通过Network标签选项可以查看每一次的请求和响应的通信过程，调出开发者工具的通用方法是在网页右击选择检查。
·开发者工具的Headers选项总共有三部分组成：
1.General：主要信息
2.Response Headers：响应头
3.Request Headers：请求头
·Response选项是查看响应体信息的
"""