import ssl
from urllib import request

import os
from lxml import etree
import settings
from db import DB
from item import UserItem


class QiuBaiSpider():
    def __init__(self):
        self.db = DB()
        ssl._create_default_https_context = ssl._create_unverified_context
        print('----sprider start....----')

    def __del__(self):
        print('---go back .....---')
        self.db.close()

    def run(self):
        next_url = settings.start_url
        while True:
            html = self.request(next_url)
            # 解析网页，并获取下一次请求的路径
            next_url = self.parse(html)
            if not next_url:
                break
    def request(self,url):
        #opener = request.build_opener(request.ProxyHandler(proxies=settings.proxies))
        req = request.Request(url,headers=settings.headers)
        resp = request.urlopen(req)
        if resp.status == 200:
            print('request success')
            html = resp.read().decode()
            print(html)
            return html

    def parse(self,html):
        et = etree.HTML(html)
        authors = et.xpath(settings.author_path)
        for author in authors:  # author _Element
            try:
                home = author.xpath(settings.home_path)[0]  # './a/@href'
                id = home.split('/')[-2]
                name = author.xpath(settings.name_path)[0]
                age = author.xpath(settings.age_path)[0]
                img = 'http:'+author.xpath(settings.src_path)[0].split('?')[0]
            except:
                pass
            else:
                item = UserItem(id,name,age,img,home)
                # 将数据存放到数据库中
                self.db.save(item)
                self.saveImg(img,id)

        # 读取下一页
        try:
            next_url =settings.start_url+et.xpath(settings.next_path_path)[0]
        except:
            pass
        else:
            return next_url
    def saveImg(self,url,id):
        filname = './head/{}.{}'.format(id,url.split('.')[-1])
        if os.path.exists(filname):
            return
        request.urlretrieve(url,filename=filname)
        print(filname,'图片保存成功')

if __name__ == '__main__':
    QiuBaiSpider().run()