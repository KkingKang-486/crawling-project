from selenium import webdriver      # pip install selenium
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import re
import time
import datetime

category =['성인', '스릴러', '스포츠', '시대물', '아동', '아이돌', '액션']


url = 'https://laftel.net/finder'       # 반응형 웹사이트

options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('lang=kr_KR')
driver = webdriver.Chrome('./chromedriver', options=options)
df_title = pd.DataFrame()
url = 'https://laftel.net/finder'
driver.get(url)
category_xpath1 = '//*[@id="root"]/div/div[2]/div[1]/div[3]/button/div'     # 필터
driver.find_element('xpath', category_xpath1).click()

category_xpath2 = '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div'     # 장르
driver.find_element('xpath', category_xpath2).click()

for i in range(12, 20):
    category_xpath3 = '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[2]/ul/li[{}]/div/div'.format(i)     # 카테고리
    driver.find_element('xpath', category_xpath3).click()

category_xpath4 = '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/button'  # 적용
driver.find_element('xpath', category_xpath4).click()

category_xpath5 = '//*[@id="root"]/div/div[2]/div[2]/button'    # 적용
driver.find_element('xpath', category_xpath5).click()

time.sleep(10)
