# coding=utf-8
import urllib2
import re

# 获取ip地址的网站
url="https://ip.cn"
# 这个不需要用正则表达式来抓取
url="http://ipecho.net/plain"
# afraid.org动态域名解析

while True:
    pass

my_afraid_ddns="https://freedns.afraid.org/dynamic/update.php?cTFmS2NUWlNBNVFwc1dmY2Q1cW86MTc0NjY2NTA="
headers={
'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'accept-encoding':'',
'accept-language':'zh-CN,zh;q=0.8,en;q=0.6',
'upgrade-insecure-requests':'1',
'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Mobile Safari/537.36'
}
req=urllib2.Request(url=url,headers=headers)
response=urllib2.urlopen(req)
# ip=re.findall(r"((25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))",response.read())
ip=re.findall(r"(?:(?:2[0-4][0-9]\.)|(?:25[0-5]\.)|(?:1[0-9][0-9]\.)|(?:[1-9][0-9]\.)|(?:[0-9]\.)){3}(?:(?:2[0-5][0-5])|(?:25[0-5])|(?:1[0-9][0-9])|(?:[1-9][0-9])|(?:[0-9]))",response.read())
print(ip[0])