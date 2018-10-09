# Python3爬取全民k歌

##1.通过歌曲主页链接爬取
首先打开歌曲主页，打开开发者工具（F12）。
选择Network,点击播放，会发现有一个请求返回的资源是媒体类型，点击查看这个请求，发现是歌曲的链接地址，请求为get请求。
![Aaron Swartz](https://raw.githubusercontent.com/Mrliu8023/getquanmin/master/image/01.png)

现在查看网页源码发现这个链接隐藏在网页的JS脚本中，至此，我们只需要利用requests库爬取歌曲的主页，然后通过re模块将我们需要的歌曲连接提取出来即可。
![Aaron Swartz](https://raw.githubusercontent.com/Mrliu8023/getquanmin/master/image/02.png)


##2.通过用户主页爬取

首先我们观察用户首页，发现每次加载是8首歌曲，点击查看更多时地址栏并没有变化，可以判断歌单信息通过Ajax请求。

查看Network,找到歌单信息的请求，发现是GET方式，返回的是json，包含歌曲的主要信息。所以我们代码中通过修改get请求参数就可以获取所有的歌曲信息。
![Aaron Swartz](https://raw.githubusercontent.com/Mrliu8023/getquanmin/master/image/03.png)

![Aaron Swartz](https://raw.githubusercontent.com/Mrliu8023/getquanmin/master/image/04.png)

观察网页源码，发现歌曲链接是由https://node.kg.qq.com/play?s= + Shareid + &g_f=personal构成。
![Aaron Swartz](https://raw.githubusercontent.com/Mrliu8023/getquanmin/master/image/05.png)


![Aaron Swartz](https://raw.githubusercontent.com/Mrliu8023/getquanmin/master/image/06.png)

所以，我们通过歌曲首页，然后通过GET请求获取包含歌曲信息的json数据，链接为https://node.kg.qq.com/cgi/fcgi-bin/kg_ugc_get_homepage，请求中有个share_uid,这个参数是用户的ID，通过修改这个就可以获取不同的用户的歌曲了。
还有一个重要的参数是start，这个参数是用户的歌单的页数，依次+1就能获取所有的歌曲信息，当之后没有更多的歌曲时，可以发现返回的json数据中data内的参数has_more = 0,所以在代码中通过判断has_more来判断是否跳出循环。

![Aaron Swartz](https://raw.githubusercontent.com/Mrliu8023/getquanmin/master/image/07.png)


获取到数据后，我们通过re模块来获取我们需要的shareid以及歌曲的名字等等信息。

获取了shareid后，我们就可以组建链接来下载歌曲了。具体请看代码。
