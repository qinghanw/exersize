import urllib.request
import re
import requests
from time import sleep

s = input("主题：")

while True:
    resp = requests.get("http://api.qingyunke.com/api.php", {'key': 'free', 'appid': 0, 'msg': s})
    resp.encoding = 'utf8'
    x = resp.json()["content"]
    sleep(1)
    if not x:
        x = 'sb'
    print('菲菲：', x)


    x = urllib.parse.quote(x)
    link = urllib.request.urlopen(
        "http://nlp.xiaoi.com/robot/webrobot?&callback=__webrobot_processMsg&data=%7B%22sessionId%22%3A%22ff725c236e5245a3ac825b2dd88a7501%22%2C%22robotId%22%3A%22webbot%22%2C%22userId%22%3A%227cd29df3450745fbbdcf1a462e6c58e6%22%2C%22body%22%3A%7B%22content%22%3A%22" + x + "%22%7D%2C%22type%22%3A%22txt%22%7D")
    html_doc = link.read().decode()
    reply_list = re.findall(r'\"content\":\"(.+?)\\r\\n\"', html_doc)
    sleep(1)
    print('小i:', reply_list[-1])
    s = reply_list[-1]

    '''resp = requests.post("http://www.tuling123.com/openapi/api",
                         data={"key": "0754ea9ae03545ec8d9598daa0060d8c", "info": s, })
    resp = resp.json()
    sleep(1)
    print('小鱼：', resp['text'])
    s = resp['text']'''

