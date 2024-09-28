# @Time: 2024/9/27 19:55
# @Author: Shen Hao
# @File: demo04_requests入门_01.py
# @system: Win10
"""
安装requests

地址栏里为get
"""
import requests
query = input("请输入要查询的内容：")
url = f'https://www.sogou.com/web?query={query}'
headers = {
    # F12 Network  web? 下的 User-Agent
    "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}
reps = requests.get(url, headers=headers)

print(reps)
print(reps.text)
