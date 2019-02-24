# coding:utf-8
import requests
import json
from selenium import webdriver
from lxml import etree

query = '王祖贤'

def download(src, id):
    print(id)
    dir = './'+id+'.jpg'
    try:
        pic = requests.get(src, timeout=10)
        fp = open(dir,'wb')
        fp.write(pic.content)
        fp.close()
    except:
        print("can't sotre file===="+str(id))

def request_save_pic():
    ''' for 循环 请求全部的url'''
    for index in range(0,10,5):
        url="https://www.douban.com/j/search_photo?q=王祖贤&limit=20&start="+str(index)
        json_info = requests.get(url).text
        print(json_info)
        print(requests.get(url).json())
        response = json.loads(json_info,encoding='utf-8') #将json 格式转化成python格式
        for image in response['images']:
            print(image['src']) ###查看当前下载的图片网址
            download(image['src'], image['id']) ###下载一张图片
def request_save_pic_xpath():
    src_xpath =  "//div[@class='item-root']/a[@class='cover-link']/img[@class='cover']/@src"
    title_xpath = "//div[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']"
    url = "https://movie.douban.com/subject_search?search_text=王祖贤&cat=1002"
    driver = webdriver.Chrome(executable_path="D:\DataAnalysis\chromedriver_win32\chromedriver.exe")
    html = driver.get(url)
    html = etree.HTML(driver.page_source)
    srcs = html.xpath(src_xpath)
    titles = html.xpath(title_xpath)
    for src, title in zip(srcs, titles):
        download(src, title.text)
    driver.close()

if __name__ == '__main__':
    print(__name__)
    request_save_pic_xpath()
