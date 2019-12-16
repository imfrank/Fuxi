import json
from urllib import request

class HttpServer(object):
    def Post(self,params):
        return "666"
        
    @classmethod
    def Get(self,url):
        response =request.urlopen(url)
        print(response.read().decode('utf-8'))

print(HttpServer.Get("http://www.baidu.com")) 