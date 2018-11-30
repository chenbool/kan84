#!/usr/bin/python3
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup as bs
from urllib import request
import re

__author__ = 'bool'

class App(object):
    soup = ''
    page = [0, 0]
    # init
    def __init__(self):
        pass

    # 获取内容
    def setUrl(self, url):
        # resp = request.urlopen(url).read().decode("utf-8")
        resp = request.urlopen(url).read().decode("gbk")
        self.soup = bs(resp, "html.parser")
        # print(self.soup)

    # 获取电影框列表
    def getList(self):
        res = self.soup.find("div", {"id": "listBox"})
        page = res.find("div", {"id": "tpage"}).find("label").getText()

        # 页数 [ 当前页,总页数 ]
        self.page = re.findall(r"\d{1,}", page)
        # print(self.page)
        # 上一页
        prev_page = res.find("div", {"id": "tpage"}).findAll("a", {"class": "prev"})[0]['href']
        # 下一页
        next_page = res.find("div", {"id": "tpage"}).findAll("a", {"class": "next"})[0]['href']
        content = self.soup.find("ul", {"id": "contents"}).findAll("li")
        self.listToDict(content)

    # 把列表转为dict保存
    def listToDict(self, content):
        # 临时保存
        tepList = []

        # 遍历数据
        for item in content:
            temp = {
                'title': item.find("a").find("img")['alt'],
                'logo': item.find("a").find("img")['src'],
                'urls': item.find("a")['href'],
                'actor': re.sub(".+[：|:]", "", item.find("p", {"class": "actor"}).getText()).split(","),
                'type': re.sub(".+[：|:]", "", item.find("p", {"class": "type"}).getText()),
                'plot': re.sub(".+[：|:]", "", item.find("p", {"class": "plot"}).getText())
            }
            tepList.append(temp)

        print(tepList)
        pass


if __name__ == '__main__':
    api = App()
    api.setUrl('http://www.kan84.net/vod/newscary.html')
    api.getList()

