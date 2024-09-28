# @Time: 2024/9/27 20:09
# @Author: Shen Hao
# @File: demo05_requests入门_02.py
# @system: Win10
import time

import requests

# F12 headers 查看url
url = "https://fanyi.sogou.com/reventondc/suggV3"

headers = {
    # F12 Network  web? 下的 User-Agent
    "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}
s = input("请输入要翻译的内容：")
dat = {
    # 用的搜狗翻译，百度翻译无法使用，记得带上其他参数
    # 查看sugg Preview 下的json代码可以知道是否为爬取的数据
    'text': s,
    'from': 'auto',
    'to': 'zh-CHS',
    'client': 'web',
    # 'text': 'apple',
    'uuid': '331a2c67-737a-42fa-9018-f055919a0904',
    'pid': 'sogou-dict-vr',
    'addSugg': 'on'
}
time.sleep(1)
# 发送post请求
resp = requests.post(url, data=dat, headers=headers)
data = resp.json()
print(data)
sugg_list = data.get('sugg', [])

for item in sugg_list:
    keyword = item['k']
    translation = item['v']
    print(f"Keyword: {keyword}, Translation: {translation}")
