import json
import requests
from bs4 import BeautifulSoup
import parser

stock_list = []


for i in range(36):
    url = 'https://m.stock.naver.com/api/stocks/marketValue/KOSPI?page='+str(i+1)+'&pageSize=50'
    # url = 'https://m.stock.naver.com/api/stocks/marketValue/KOSPI?page={0}&pageSize=50'.format(i)

    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    jsonObj = json.loads(str(soup))
    stocks = jsonObj['stocks']
    for stock in stocks:
        # print(stock)

        stock_list.append([stock['itemCode'], stock['stockName'], stock['closePrice']])

print(str(len(stock_list)) + ' 건')
for i in stock_list:
    print(i)

