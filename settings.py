#配置
#配置请求头
from urllib import request

headers = {
    'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}

proxies = {
    "http":'',
    "https":''
}

#配置爬虫起始位置
start_url = 'https://www.qiushibaike.com'

#配置xpat路径
author_path = '//div[starts-with(@class,"author")]'
home_path = './a/@href'
src_path = './a/img/@src'
name_path = './a/h2/text()'
age_path = './div/text()'
next_path_path = '//ul[@class="pagination"]/li[last()]/a/@href'

#配置数据库
DATABASE = {
    'default':{
        'host':'10.35.163.32',
        'port':3306,
        'user':'root',
        'password':'root',
        'charset':'utf8',
        'db':'qiubai',
    }
}
