# -*- coding:utf-8 -*-
"""
@author = xijue
"""

import requests
import json
import download
import re

def getPlayList(id):
    """
    time:歌单的页面，每页最多八首歌
    id：用户的id
    获取全民K歌好友全部歌曲链接
    """
    url = "http://node.kg.qq.com/cgi/fcgi-bin/kg_ugc_get_homepage?"
    time = 1
	#获取歌单中歌曲信息
    song_info = []
	#获取歌单中歌曲的shareid
    playlist = []
    while True:
        params = {
            "outCharset": "utf - 8",
            "format": "jsonp",
            "type" : "get_ugc",
            "start": str(time),
            "num": "8",
            "share_uid":id,
        }
        try:
            rqt = requests.get(url, params= params)
            rqt.raise_for_status()
            info = rqt.text
            info = info[18:]
            info = info[:-1]
            info_dict = json.loads(info)
            song_info += info_dict['data']['ugclist']
            time += 1
            if info_dict['data']['has_more'] == 0:
                break
        except:
            print("爬取失败")

    for list in song_info:
        playlist.append(list['shareid'])

    return playlist

def getMusic(user_id):
    playlist = getPlayList(user_id)
    for shareid in playlist:
        url = "http://node.kg.qq.com/play?s=" + shareid + "&g_f=personal"
        download.getmp3(url)




if __name__=='__main__':
    url = input("请输入您要下载的用户主页：")
    id = re.search(r'\w{10,}', url).group()

    getMusic(id)