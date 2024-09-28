# @Time: 2024/9/27 20:42
# @Author: Shen Hao
# @File: demo06_requests入门_03.py
# @system: Win10
import requests



url = 'https://movie.douban.com/j/chart/top_list'
# 重新封装参数
param = {
    'type': '24',
    'interval_id': '100:90',
    'action':'',
    'start': 0,
    'limit': 20
}
reqs = requests.get(url=url, params=param)
# 反扒机制导致无数据
print(reqs.text)
# 查看headers
print(reqs.request.headers)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

reqs = requests.get(url=url, params=param, headers=headers)
# print(reqs.text)
print(reqs.json())