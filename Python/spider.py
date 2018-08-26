#coding:utf-8
from requests import Session
from config import Config
from bs4 import BeautifulSoup

class Spider:
    my_session = None
    my_config = None
    sp_header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36"
    }

    def __init__(self, Session s, Config c):
        my_session = s
        my_config = c
        pass

    def spider(self):
        """开始爬"""
        pass

    def retrieveList(self):
        """得到第一页列表"""
        r = self.my_session.get(self.my_config.getQmIndexUrl(), headers=self.sp_header)
        soup = BeautifulSoup(r.content, "html.parser")
        
        pass

    def saveOne(self):
        """保存"""
        pass
