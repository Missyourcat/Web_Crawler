# @Time: 2024/9/27 10:40
# @Author: Shen Hao
# @File: demo01_介绍.py
# @system: Win10
"""
爬虫:通过编写程序来获取到互联网上的资源
百度
需求:用程序模拟浏览器，输入一个网址，从该网址中获取到资源或内容
"""
from urllib.request import urlopen

url = 'http://www.baidu.com'
resp = urlopen(url)
# print(resp.read().decode('utf-8'))  # 解码
content  = resp.read().decode('utf-8')  # 读取网页源代码

with open('baidu.html', mode='w', encoding='utf-8') as f:
    f.write(content)
print('over')
