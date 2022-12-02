# 마지막 수정용
# 수정용
# 예측용 모델 크롤링
import re
import pandas as pd
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
category = ['판타지', '로맨스', 'sf', '개그', '액션', '모험']
pages = [239, 231, 56, 58, 42, 25]
pages_2 = [41, 40, 11, 11, 4, 5]
options = webdriver.ChromeOptions()
options.add_argument('lang=kr_KR')
driver = webdriver.Chrome('./chromedriver', options=options)
df_title = pd.DataFrame()
url = 'https://www.aniplustv.com/list'
for i in range(2, 8):   #
    titles = []
    summary = []
    driver.get(url)
    driver.maximize_window()        # 윈도우창 최대화
    time.sleep(2)
    category_xpath1 = '//*[@id="root"]/div[3]/div/div[1]/div/div/div/div[1]/div[2]/div/a'  # 더보기 클릭
    driver.find_element('xpath', category_xpath1).click()
    time.sleep(2)
    category_xpath2 = '//*[@id="root"]/div[3]/div/div[1]/div/div/div/div[1]/div[2]/dl/dd[{}]/div/label'.format(i)     # 카테고리 선택버튼
    driver.find_element('xpath', category_xpath2).click()
    time.sleep(2)
    prev_height = driver.execute_script("return document.body.scrollHeight")
    while True: # 무한스크롤 루프
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2) # 페이지가 완전히 내려갈때까지 대기 -> 페이지 길이가 길면 시간을 증가시킨다
        curr_height = driver.execute_script("return document.body.scrollHeight")
        if (curr_height == prev_height):
            break
        else:
            prev_height = driver.execute_script("return document.body.scrollHeight")
    for k in range(1, pages_2[i-2]):
        for j in range(1, 7):
            category_xpath4 = '//*[@id="root"]/div[3]/div/div[2]/div[1]/div[1]/div/div[{}]/div/div[{}]/div/div/p[1]'.format(k, j)     # 제목
            title = driver.find_element('xpath', category_xpath4).text
            title = re.compile('[^가-힣A-Za-z ]').sub(' ', title)
            titles.append(title)
            time.sleep(2)
            category_xpath3 = '//*[@id="root"]/div[3]/div/div[2]/div[1]/div[1]/div/div[{}]/div/div[{}]/div/div/div/img'.format(k, j)  # 카테고리 선택버튼
            driver.find_element('xpath', category_xpath3).click()
            time.sleep(2)

            # category_xpath4 = '//*[@id="root"]/div[4]/div/div[2]/div[2]/div[3]/div[2]/h1/text()'     # 제목
            # title = driver.find_element('xpath', category_xpath4).text
            # title = re.compile('[^가-힣A-Za-z ]').sub(' ', title)
            # titles.append(title)
            # time.sleep(3)

            category_xpath5 = '//*[@id="root"]/div[4]/div/div[2]/div[2]/div[3]/div[2]/div[1]/span/a' # 더보기 클릭 # 더보기 없는 것도 있음
            driver.find_element('xpath', category_xpath5).click()
            time.sleep(2)

            category_xpath6 = '//*[@id="root"]/div[4]/div/div[2]/div[2]/div[3]/div[2]/div[1]' # 줄거리
            driver.find_element('xpath', category_xpath6).click()
            summarys = driver.find_element('xpath', category_xpath6).text
            summarys = re.compile('[^가-힣 ]').sub(' ', summarys)
            summary.append(summarys)
            time.sleep(2)

            category_xpath7 = '//*[@id="root"]/div[4]/div/div[1]/img' # x클릭
            driver.find_element('xpath', category_xpath7).click()
            time.sleep(1)

            if j % 6 == 0:  # 6개마다 저장
                df_section_title = pd.DataFrame(titles, columns=['titles'])
                df_section_summary = pd.DataFrame(summary, columns=['summary'])
                df_section_title['category'] = category[i-2]
                temp = pd.concat([df_section_title, df_section_summary], axis=1)
                df_title = pd.concat([df_title, temp], ignore_index=True)
                df_title.to_csv('./crawling_data_4/aniplus_crawling_data_{}_{}.csv'.format(category[i-2], (k*6)), index=True)
                titles = []
                summary = []