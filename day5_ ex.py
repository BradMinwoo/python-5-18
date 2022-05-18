import json
import sqlite3

import requests
from bs4 import BeautifulSoup

from day5_s_3 import stock_list
stock_list1=[]
def fn_stock_list(i):
    url = 'https://m.stock.naver.com/api/stocks/marketValue/KOSPI?page='+str(i)+'&pageSize=50'

    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    jsonObj = json.loads(str(soup))
    stocks = jsonObj['stocks']

    for stock in stocks:
        # print(stock)

        stock_list1.append([stock['itemCode'], stock['stockName'], stock['closePrice']])

print(fn_stock_list(1))
# conn = sqlite3.connect('./stock.db')
# sql = """
#     INSERT INTO  stocks VALUES (?, ?, ?);
#      """
#
# cur = conn.cursor()
# cur.executemany(sql, stock_list)
# conn.commit()
# cur.close()
# conn.close()
