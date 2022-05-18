#pip install selenium
from builtins import print

from selenium import webdriver
import time
from bs4 import BeautifulSoup

url = 'http://tour.interpark.com/'
driver = webdriver.Chrome('./chromedriver')
# wating 3s for web date loading
driver.implicitly_wait(3)
driver.get(url)

driver.find_element_by_id('SearchGNBText').send_keys('하와이')
driver.find_element_by_css_selector('button.search-btn').click()
time.sleep(2)
# soup  = BeautifulSoup(driver.page_source,'html.parser')
# print(soup.prettify())
# lis = soup.select('.searchAllBox.overseaTravel.col1 li')
# for li in lis:
#     print(li)
lis = driver.find_element_by_css_selector('ul.boxList li.boxItem ')
for li in lis:
    print(li.get_attribute('innerHTML'))
    print(li.find_element_by_selector('h5.infoTile'))
    print(li.find_element_by_selector('strong').text)
driver.stop_client()
driver.close()