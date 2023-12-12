#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import urllib.request
import urllib.parse
import json
import hashlib
import base64
#接口地址
url ="http://ltpapi.xfyun.cn/v1/ke"
#开放平台应用ID
x_appid = "c973bdcc"
#开放平台应用接口秘钥
api_key = "ac8cf13d2b69e41d2132f1704c20153e"
#语言文本
TEXT="广汽集团总经理冯兴亚今日在2023广州车展上表示，将固态电池、无钴电池、低钴电池、钠离子电池等列入广汽自研电池关键技术攻关。其中，固态电池已经取得突破性进展，在电芯能量密度达到400Wh/Kg时，能够满足电池在极端环境下的安全性与可靠性要求。“我们的目标是，在2026年实现全固态电池装车搭载。”冯兴亚透露。此外，投资109亿元36GWh的因湃电池首个工厂将于本月底批量生产。"


def main():
    body = urllib.parse.urlencode({'text': TEXT}).encode('utf-8')
    param = {"type": "dependent"}
    x_param = base64.b64encode(json.dumps(param).replace(' ', '').encode('utf-8'))
    x_time = str(int(time.time()))
    x_checksum = hashlib.md5(api_key.encode('utf-8') + str(x_time).encode('utf-8') + x_param).hexdigest()
    x_header = {'X-Appid': x_appid,
                'X-CurTime': x_time,
                'X-Param': x_param,
                'X-CheckSum': x_checksum}
    req = urllib.request.Request(url, body, x_header)
    result = urllib.request.urlopen(req)
    result = result.read()
    #print(result.decode('utf-8'))

    json_data = json.loads(result)
    keywords = json_data["data"]["ke"]
    top_three_keywords = keywords[:3]
    top_three_words = [keyword["word"] for keyword in top_three_keywords]
    print(top_three_words)

    return


if __name__ == '__main__':
    main()
