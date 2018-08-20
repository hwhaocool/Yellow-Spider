#coding:utf-8

import requests
import datetime
import time
import re

s = requests.Session()

login_url = 'http://smingyue.com/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1'
login_data  = {
    'fastloginfield' : 'username',
    'username' : 'xxx',
    'password' : 'xxx',
    'quickforward' : 'yes',
    'handlekey' : 'ls'
}

r = s.post(login_url, data=login_data)
print r.status_code

index_url = 'http://smingyue.com/forum.php'
r = s.get(index_url)
print r.status_code
print r.encoding

form_hash = ''
match_obj = re.search("dsu_paulsign:sign&([^']+)", r.text, re.M)
if match_obj:
    print "find 1"
    form_hash = match_obj.group(1)
    print "formhash is %s" % form_hash

sign_url = 'http://smingyue.com/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&sign_as=1&inajax=1'
sign_data = {
    'formhash' : form_hash,
    'qdxq' : 'kx',
    'qdmode' : '3',
    'todaysay' : '',
    'fastreply' : '0'
}

time.sleep(50)

oldtime = datetime.datetime.now()
count = 20
while count > 0:
    r = s.post(sign_url, data=sign_data)
    print r.status_code
    count = count - 1

newtime = datetime.datetime.now() 
print u'cost: %s microseconds' % (newtime-oldtime).microseconds
print u'cost: %s seconds' % (newtime-oldtime).seconds 