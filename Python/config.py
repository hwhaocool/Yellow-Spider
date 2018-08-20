#author: hwhaocool
#since: 2018-08-19

class Config:
    json = {}

    def __init__(self):
        pass

    def getLoginUrl(self):
        return json["login_url"]

    def getSignUrl(self):
        return json["sign_url"]

    def getIndexUrl(self):
        return json["index_url"]

    def getUserName(self):
        return json["user_name"]

    def getPassword(self):
        return json["password"]