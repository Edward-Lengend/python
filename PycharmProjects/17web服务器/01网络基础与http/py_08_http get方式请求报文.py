"""
HTTP 请求报文(浏览器发送给web服务器程序的数据)


学习目标
·能够知道HTTP请求报文的结构
1.HTTP 请求报文介绍
HTTP最常见的请求报文有两种：
1.GET方式的请求报文
2.POST方式的请求报文

说明：
·GET：获取web服务器数据(比如获取新闻列表数据)
·POST：向web服务器提交数据（例如登录，把用户名和密码发送给服务器）
    （post也可以提交数据，并且post比get安全）


在浏览器中，按f12进入控制台，network，点击第一个网址
request header为请求头，请求头是get请求报文中的一部分数据
点击view source，数据如下


---http请求报文---

GET / HTTP/1.1   # --该行为请求行， get为请求方法，/ 默认请求访问首页数据，1.1是http协议版本--



# --以下为请求头--
Host: www.itcast.cn  # Host：服务器主机ip地址和端口号，端口号默认为80，不显示

Connection: keep-alive  # 和服务端保持长连接，当服务端和客户端有一段时间（3-5min）没有通信，
                          服务端程序会主动向客户端断开连接
Cache-Control: max-age=0
sec-ch-ua: "Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Linux"


Upgrade-Insecure-Requests: 1
--让客户端升级不安全请求， 以后要使用https


User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)
    Chrome/94.0.4606.61 Safari/537.36
    --用户代理， 客户端程序的名称， 以后讲爬虫的时候可以根据是否有User-Agent进行反爬--


Accept: text/html,application/xhtml+xml,application/xml;
           q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;
               v=b3;q=0.9
           --告诉服务端程序可以接收的数据类型--

Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document



Accept-Encoding: gzip, deflate, br
--告诉服务端程序支持的压缩算法--

Accept-Language: en-US,en;q=0.9
--告诉服务端程序可以支持的语言--


-- cookie客户端用户身份的标识--
Cookie: UM_distinctid=17c1c795d4141d-02106d60e90101-142f1c08-19e7b6-17c1c795d42bcf;
CNZZDATA4617777=cnzz_eid%3D686435521-1632562518-%26ntime%3D1632562518;
Hm_lvt_0cb375a2e834821b74efffa6c71ee607=1632565288;
Hm_lvt_5781a15780e8f638873598472befe1e9=1632565289;
qimo_seosource_b2f10070-624e-11e8-917f-9fb8db4dc43c=%E7%AB%99%E5%86%85;
qimo_seokeywords_b2f10070-624e-11e8-917f-9fb8db4dc43c=;
qimo_xstKeywords_b2f10070-624e-11e8-917f-9fb8db4dc43c=;
href=https%3A%2F%2Fwww.itcast.cn%2F; accessId=b2f10070-624e-11e8-917f-9fb8db4dc43c;
bad_idb2f10070-624e-11e8-917f-9fb8db4dc43c=5a0ee0c1-1dea-11ec-aa43-b7af697e44fe;
nice_idb2f10070-624e-11e8-917f-9fb8db4dc43c=5a0ee0c2-1dea-11ec-aa43-b7af697e44fe;
openChatb2f10070-624e-11e8-917f-9fb8db4dc43c=true;
parent_qimo_sid_b2f10070-624e-11e8-917f-9fb8db4dc43c=5e215bc0-1
dea-11ec-b6d9-9597c0e925cf;
qimo_talking_b2f10070-624e-11e8-917f-9fb8db4dc43c=false; status=agentClose;
Hm_lpvt_0cb375a2e834821b74efffa6c71ee607=1632566083; H
m_lpvt_5781a15780e8f638873598472befe1e9=1632566083;
pageViewNum=3

----空行----



----http  get请求的原始报文数据,每一行都要加上\r\n----

--请求行--
GET / HTTP/1.1\r\n
# --请求头--
Host: www.itcast.cn\r\n
Connection: keep-alive\r\n
Upgrade-Insecure-Requests: 1\r\n
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)
    Chrome/94.0.4606.61 Safari/537.36\r\n
Accept: text/html,application/xhtml+xml,application/xml;
           q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;
               v=b3;q=0.9\r\n
Accept-Encoding: gzip, deflate, br\r\n
Accept-Language: en-US,en;q=0.9\r\n
-- cookie客户端用户身份的标识--
Cookie: UM_distinctid=17c1c795d4141d-02106d60e90101-142f1c08-19e7b6-17c1c795d42bcf;
CNZZDATA4617777=cnzz_eid%3D686435521-1632562518-%26ntime%3D1632562518;
Hm_lvt_0cb375a2e834821b74efffa6c71ee607=1632565288;
Hm_lvt_5781a15780e8f638873598472befe1e9=1632565289;
qimo_seosource_b2f10070-624e-11e8-917f-9fb8db4dc43c=%E7%AB%99%E5%86%85;
qimo_seokeywords_b2f10070-624e-11e8-917f-9fb8db4dc43c=;
qimo_xstKeywords_b2f10070-624e-11e8-917f-9fb8db4dc43c=;
href=https%3A%2F%2Fwww.itcast.cn%2F; accessId=b2f10070-624e-11e8-917f-9fb8db4dc43c;
bad_idb2f10070-624e-11e8-917f-9fb8db4dc43c=5a0ee0c1-1dea-11ec-aa43-b7af697e44fe;
nice_idb2f10070-624e-11e8-917f-9fb8db4dc43c=5a0ee0c2-1dea-11ec-aa43-b7af697e44fe;
openChatb2f10070-624e-11e8-917f-9fb8db4dc43c=true;
parent_qimo_sid_b2f10070-624e-11e8-917f-9fb8db4dc43c=5e215bc0-1
dea-11ec-b6d9-9597c0e925cf;
qimo_talking_b2f10070-624e-11e8-917f-9fb8db4dc43c=false; status=agentClose;
Hm_lpvt_0cb375a2e834821b74efffa6c71ee607=1632566083; H
m_lpvt_5781a15780e8f638873598472befe1e9=1632566083;
pageViewNum=3\r\n
----空行----
\r\n


总结
--http请求报文的格式--
请求头\r\n
请求行\r\n
空行（\r\n）

提示：每一项信息之间都需要加上\r\n， 这是由http协议规定的
"""