#coding=utf-8
import requests

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"}
python = {"kw":"李毅"}
url = "http://www.baidu.com/f?"

respone = requests.get(url,headers=headers,params=python)
#这个是断言，主要是看发送请求是否成功
# assert respone.status_code
# print(respone.status_code)
# print(respone.headers)
# print(respone.request.url)
# print(respone.url)
# print(respone.request.headers)
# print(respone.content.decode())
#字符串格式化方式
url = "http://www.baidu.com/s?wd={}".format("传智播客")
respone= requests.get(url,headers=headers)
# print(respone.text)

url = "https://tieba.baidu.com/f?kw=%E6%9D%8E%E6%AF%85&ie=utf-8&pn=50"
respone= requests.get(url,headers=headers)
print(respone.text)



