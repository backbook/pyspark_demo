# coding=utf-8
import requests


class TiebaSpider:
    def __init__(self,tieba_name):
        self.tieba_name = tieba_name
        self.url = "https://tieba.baidu.com/f?wd="+tieba_name+"&ie=utf-8&pn={}"
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"}
    def parse_url(self,url):
        print(url)
        respone = requests.get(url,headers=self.headers)
        return respone.content.decode()

    def get_url_list(self):
        url_list = []
        for i in range(100):
            url_list.append(self.url.format(i*50))
        return url_list

    def save_html(self,html_str,page_num):
        file_path = "{}-第{}页面.html".format(self.tieba_name,page_num)
        with open(file_path,"w",encoding="utf-8") as f:
            f.write(html_str)

    def run(self):
        url_list = self.get_url_list()
        for url in url_list:
            html_url = self.parse_url(url)
            page_num = url_list.index(url)+1
            self.save_html(html_url,page_num)

if __name__ == '__main__':
    liyi = TiebaSpider("lol")
    liyi.run()

    #https://tieba.baidu.com/f?kw=%E6%9D%8E%E6%AF%85&ie=utf-8&pn=50
    #https://tieba.baidu.com/f?wd=李毅&ie=utf-8&pn=50