from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import util
url='https://www.msn.com/ko-kr/news'

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)
driver.get(url)

try:
    cnt = 30
    pagedowns = 1
    body = driver.find_element_by_tag_name('body')
    while pagedowns < cnt:
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        pagedowns+=1
except Exception as e:
    print(str(e))

# driver.get_screenshot_as_file('msn.png')
util.fullpage_screenshot(driver, 'full_msn.png')
html = driver.page_source

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())