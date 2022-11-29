import re
import pandas as pd
import time
from selenium import webdriver


category = ['음식', '음악', '이세계', '일상', '추리', '치유', '판타지']
pages = [50, 124, 138, 417, 101, 130, 1072]

url = 'https://laftel.net/finder'       # 반응형 웹사이트

options = webdriver.ChromeOptions()
options.add_argument('lang=kr_KR')
driver = webdriver.Chrome('./chromedriver', options=options)
df_title = pd.DataFrame()
url = 'https://laftel.net/finder'

for k in range(0, 7):

    for i in range(19, 23): #음식/음악/이세계/일상
        titles = []
        driver.get(url)
        driver.maximize_window()

        category_xpath1 = '//*[@id="root"]/div/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/section[1]/div[1]/div'  # 장르
        driver.find_element('xpath', category_xpath1).click()
        time.sleep(1)
        category_xpath2 = '//*[@id="modal-portal"]/div/div[2]/div[2]/div[{}]'.format(i)     # 카테고리 선택버튼
        driver.find_element('xpath', category_xpath2).click()
        time.sleep(1)

        category_xpath3 = '//*[@id="modal-portal"]/div/div[2]/div[1]/div[2]/button[2]'     # 확인버튼
        driver.find_element('xpath', category_xpath3).click()

        driver.maximize_window()
        prev_height = driver.execute_script("return document.body.scrollHeight")

        while True: # 무한스크롤 루프
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(20) # 페이지가 완전히 내려갈때까지 대기 -> 페이지 길이가 길면 시간을 증가시킨다
            curr_height = driver.execute_script("return document.body.scrollHeight")
            if (curr_height == prev_height):
                break
            else:
                prev_height = driver.execute_script("return document.body.scrollHeight")
        for j in range(1, pages[k]):
            category_xpath4 = '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[3]/div[{}]/a'.format(j)     # 제목

            time.sleep(2)
            title = driver.find_element('xpath', category_xpath4).text
            title = re.compile('[^가-힣 ]').sub(' ', title)
            titles.append(title)
            if j % 10 == 0:
                df_section_title = pd.DataFrame(titles, columns=['titles'])
                df_section_title['category'] = category[k]
                df_title = pd.concat([df_title, df_section_title], ignore_index=True)
                df_title.to_csv('./crawling_data/crawling_data_{}_{}.csv'.format(category[k], j), index=False)
                titles = []

    for i in range(24, 26): #추리/치유
        titles = []
        driver.get(url)
        driver.maximize_window()

        category_xpath1 = '//*[@id="root"]/div/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/section[1]/div[1]/div'  # 장르
        driver.find_element('xpath', category_xpath1).click()
        time.sleep(1)
        category_xpath2 = '//*[@id="modal-portal"]/div/div[2]/div[2]/div[{}]'.format(i)     # 카테고리 선택버튼
        driver.find_element('xpath', category_xpath2).click()
        time.sleep(1)

        category_xpath3 = '//*[@id="modal-portal"]/div/div[2]/div[1]/div[2]/button[2]'     # 확인버튼
        driver.find_element('xpath', category_xpath3).click()

        driver.maximize_window()
        prev_height = driver.execute_script("return document.body.scrollHeight")

    while True:  # 무한스크롤 루프
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(20)  # 페이지가 완전히 내려갈때까지 대기 -> 페이지 길이가 길면 시간을 증가시킨다
        curr_height = driver.execute_script("return document.body.scrollHeight")
        if (curr_height == prev_height):
            break
        else:
            prev_height = driver.execute_script("return document.body.scrollHeight")
        for j in range(1, pages[k]):
            category_xpath4 = '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[3]/div[{}]/a'.format(j)     # 제목

            time.sleep(2)
            title = driver.find_element('xpath', category_xpath4).text
            title = re.compile('[^가-힣 ]').sub(' ', title)
            titles.append(title)

            if j % 10 == 0: # 10개마다 저장
                df_section_title = pd.DataFrame(titles, columns=['titles'])
                df_section_title['category'] = category[k]
                df_title = pd.concat([df_title, df_section_title], ignore_index=True)
                df_title.to_csv('./crawling_data/crawling_data_{}_{}.csv'.format(category[k], j), index=False)
                titles = []

    for i in range(27, 28): # 판타지
        titles = []
        driver.get(url)
        driver.maximize_window()

        category_xpath1 = '//*[@id="root"]/div/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/section[1]/div[1]/div'  # 장르
        driver.find_element('xpath', category_xpath1).click()
        time.sleep(1)
        category_xpath2 = '//*[@id="modal-portal"]/div/div[2]/div[2]/div[{}]'.format(i)     # 카테고리 선택버튼
        driver.find_element('xpath', category_xpath2).click()
        time.sleep(1)

        category_xpath3 = '//*[@id="modal-portal"]/div/div[2]/div[1]/div[2]/button[2]'     # 확인버튼
        driver.find_element('xpath', category_xpath3).click()

        driver.maximize_window()
        prev_height = driver.execute_script("return document.body.scrollHeight")

    while True:  # 무한스크롤 루프
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(20)
        curr_height = driver.execute_script("return document.body.scrollHeight")
        if (curr_height == prev_height):
            break
        else:
            prev_height = driver.execute_script("return document.body.scrollHeight")
        for j in range(1, pages[k]):
            category_xpath4 = '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[3]/div[{}]/a'.format(j)     # 제목

            time.sleep(2)
            title = driver.find_element('xpath', category_xpath4).text
            title = re.compile('[^가-힣 ]').sub(' ', title)
            titles.append(title)

            if j % 100 == 0: # 100개마다 저장 -> 판타지는 개수가 1000개 이상이여서 100개로 설정
                df_section_title = pd.DataFrame(titles, columns=['titles'])
                df_section_title['category'] = category[k]
                df_title = pd.concat([df_title, df_section_title], ignore_index=True)
                df_title.to_csv('./crawling_data/crawling_data_{}_{}.csv'.format(category[k], j), index=False)
                titles = []