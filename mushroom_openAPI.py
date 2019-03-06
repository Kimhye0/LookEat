from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
from bs4 import BeautifulSoup

import urllib.request
import pandas as pd
import requests

mushroomImage = {}

url = 'http://api.nature.go.kr/openapi/service/rest/KpniService/authorInfo'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : 'Z1S6KMJSzp5OyfcsP3ndEKd2eWf5bu1RuHu7EX%2F3%2FNdGSWk8YdqEsPd2aaUCMXOFGRCxHBcbDhWBEF%2FNdLsxmw%3D%3D', quote_plus('q1') : '6' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print (response_body)
