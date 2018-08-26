#coding=utf-8
#author: hwhaocool
#since: 2018-08-19

import json

class Config:
    """配置项"""

    conf = {}

    def __init__(self):
        f = open("config.json", 'rb')
        self.conf = json.load(f )
        f.close()
        
        print "Config load completed"

    def getLoginUrl(self):
        """登录地址"""
        return self.conf["login_url"]

    def getSignUrl(self):
        """签到地址"""
        return self.conf["sign_url"]

    def getIndexUrl(self):
        """首页地址"""
        return self.conf["index_url"]

    def getUserName(self):
        return self.conf["user_name"]

    def getPassword(self):
        return self.conf["password"]

    def getQmIndexUrl(self):
        return self.conf["qm_index_url"]
