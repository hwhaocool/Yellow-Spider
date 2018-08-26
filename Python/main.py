#coding:utf-8
import requests
from config import Config
import re
from bs4 import BeautifulSoup

#open session
my_session = requests.Session()

#load config
my_config = Config()

def login():
    """登录"""
    login_data  = {
        'fastloginfield' : 'username',
        'username' : my_config.getUserName(),
        'password' : my_config.getPassword(),
        'quickforward' : 'yes',
        'handlekey' : 'ls'
    }

    r = my_session.post(my_config.getLoginUrl(), data=login_data)

    if 200 == r.status_code:
        print "Login success"
    else:
        print "Login failed, code is %d" % r.status_code

def sign():
    """签到"""
    ##访问首页
    index_url = my_config.getIndexUrl()
    r = my_session.get(index_url)

    if 200 == r.status_code:
        print "Visit Index page success"
    else:
        print "Visit Index page failed, code is %d" % r.status_code
        return

    ##从首页reponse里取出 form_hash
    global form_hash
    form_hash = ''
    match_obj = re.search("dsu_paulsign:sign&([^']+)", r.text, re.M)
    if match_obj:
        print "find 1"
        form_hash = match_obj.group(1)
        print "formhash is %s" % form_hash

    ##签到
    sign_url = my_config.getSignUrl()
    sign_data = {
        'formhash' : form_hash,
        'qdxq' : 'kx',
        'qdmode' : '3',
        'todaysay' : '',
        'fastreply' : '0'
    }

    r = my_session.post(sign_url, data=sign_data)
    if 200 == r.status_code:
        print "Sign success"
    else:
        print "Sign failed, code is %d" % r.status_code

#spider
def spider():
    """爬"""
    sp_header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36"
    }

    r = my_session.get(sp_url, headers=sp_header)
    print r.content
    pass

def main():
    login()
    sign()
    # spider()
    pass

main()