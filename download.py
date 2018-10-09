# -*- coding:utf-8 -*-
"""
@author = xijue
"""

import requests
import re
import os

def getHtmlMessage(url):
    try:
        #爬取歌曲主页面
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        html = r.text
        #正则提取歌曲信息
        pattern = re.compile(r'window.__DATA__.*?kg_nick":"(.*?)",".*?playurl":"(.*?)",".*?song_name":"(.*?)"', re.S)
        return pattern.search(html)
    except:
        return ("爬取网页失败")


def getmp3(url):
    """
    下载mp3
    """
    message = getHtmlMessage(url)
    #获取歌手名
    singer = message.group(1)
    #获取歌名
    song_name = message.group(3)
    #获取歌曲链接
    songurl = message.group(2)
    #设置下载路径(以歌手名做文件夹名称)  linux下请自行设置
    root = "E://quanminsongs//"+singer 
	
    path = root + "//" +song_name + "-" + singer + ".m4a"
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        print("正在下载" +"      "+ song_name)
        if not os.path.exists(path):
            rqt = requests.get(songurl)
            with open(path, 'wb') as f:
                f.write(rqt.content)
                f.close()
                print("下载成功")
        else:
            print("文件已存在，下载失败")
    except Exception as c:
        print("爬取失败")


