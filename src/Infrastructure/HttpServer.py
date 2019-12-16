import json
from urllib import request

def Post(params):
    return "666"

def Get(url):
    response = request.urlopen(url)
    print(response.read().decode('utf-8'))

print(Get("http://localhost:51140/weatherforecast")) 