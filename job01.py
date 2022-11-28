from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np
from selenium import webdriver
import time
import datetime

category = ['음식', '음악', '이세계', '일상', '추리', '치유', '판타지']

url = 'https://laftel.net/finder'       # 반응형 웹사이트

options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('lang=kr_KR')
driver = webdriver.Chrome('./chromedriver', options=options)
df_title = pd.DataFrame()
url = 'https://laftel.net/finder'

for i in range(19, 23): #음식/음악/이세계/일상
    driver.get(url)
    driver.maximize_window()

    category_xpath1 = '//*[@id="root"]/div/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/section[1]/div[1]/div'  # 장르
    driver.find_element('xpath', category_xpath1).click()
    time.sleep(1)
    category_xpath2 = '//*[@id="modal-portal"]/div/div[2]/div[2]/div[{}]'.format(i)     # 카테고리
    driver.find_element('xpath', category_xpath2).click()
    time.sleep(1)

    category_xpath3 = '//*[@id="modal-portal"]/div/div[2]/div[1]/div[2]/button[2]'     # 카테고리
    driver.find_element('xpath', category_xpath3).click()
    time.sleep(1)

for i in range(24, 26): #추리 / 치유
    driver.get(url)
    driver.maximize_window()

    category_xpath1 = '//*[@id="root"]/div/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/section[1]/div[1]/div'  # 장르
    driver.find_element('xpath', category_xpath1).click()
    time.sleep(1)
    category_xpath2 = '//*[@id="modal-portal"]/div/div[2]/div[2]/div[{}]'.format(i)     # 카테고리
    driver.find_element('xpath', category_xpath2).click()
    time.sleep(1)

    category_xpath3 = '//*[@id="modal-portal"]/div/div[2]/div[1]/div[2]/button[2]'     # 카테고리
    driver.find_element('xpath', category_xpath3).click()
    time.sleep(1)

for i in range(27, 28): # 판타지
    driver.get(url)
    driver.maximize_window()

    category_xpath1 = '//*[@id="root"]/div/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/section[1]/div[1]/div'  # 장르
    driver.find_element('xpath', category_xpath1).click()
    time.sleep(1)
    category_xpath2 = '//*[@id="modal-portal"]/div/div[2]/div[2]/div[{}]'.format(i)     # 카테고리
    driver.find_element('xpath', category_xpath2).click()
    time.sleep(1)

    category_xpath3 = '//*[@id="modal-portal"]/div/div[2]/div[1]/div[2]/button[2]'     # 카테고리
    driver.find_element('xpath', category_xpath3).click()
    time.sleep(1)


