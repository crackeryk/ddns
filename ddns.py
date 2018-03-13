# coding=utf-8
import urllib
import urllib2
import re
url="https://ip.cn"
change_ddns="https://freedns.afraid.org/dynamic/update.php?cTFmS2NUWlNBNVFwc1dmY2Q1cW86MTc0NjY2NTA="
headers={
# ':authority':'ip.cn',
# ':method':'GET',
# ':path':'/',
# ':scheme':'https',
'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'accept-encoding':'',
'accept-language':'zh-CN,zh;q=0.8,en;q=0.6',
# 'cookie':'__cfduid=da44df01885710180458b4b60bb00aa061520825162; UM_distinctid=162183e665e2bc-07ecdd45f103df-791c30-2a3000-162183e665f204; CNZZDATA123770=cnzz_eid%3D525231623-1501641615-%26ntime%3D1520924610',
'upgrade-insecure-requests':'1',
'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Mobile Safari/537.36'

}
req=urllib2.Request(url=url,headers=headers)
response=urllib2.urlopen(req)
# ip=re.findall(r"((25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))",response.read())
ip=re.findall(r"(?:(?:2[0-4][0-9]\.)|(?:25[0-5]\.)|(?:1[0-9][0-9]\.)|(?:[1-9][0-9]\.)|(?:[0-9]\.)){3}(?:(?:2[0-5][0-5])|(?:25[0-5])|(?:1[0-9][0-9])|(?:[1-9][0-9])|(?:[0-9]))",response.read())
print(ip[0])