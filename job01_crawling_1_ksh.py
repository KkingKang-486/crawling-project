import re
import pandas as pd
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

#category = ['sf', '개그']   # 제외장르 제외하고     # category[i-n]     # n은 페이지 번호 # 주석
#category = ['드라마', '로맨스', '모험']   # 제외장르 제외하고
category = ['미스터리', '범죄']   # 제외장르 제외하고

#pages = [271, 687]     # sf, 개그         # 실제 보이는 +1씩해야 마지막 페이지까지됨            # pages[i-n]        # n은 페이지 번호
#pages = [124, 310, 561] # 드라마, 로맨스, 모험
pages = [132, 98]      # 미스터리, 범죄


options = webdriver.ChromeOptions()
options.add_argument('lang=kr_KR')
driver = webdriver.Chrome('./chromedriver', options=options)
df_title = pd.DataFrame()
url = 'https://laftel.net/finder'   # 반응형 웹사이트


for i in range(10, 12):   # SF(세번째),개그(네번째) # 6, 7 , 8     # 10, 11
    titles = []
    driver.get(url)
    driver.maximize_window()        # 윈도우창 최대화

    category_xpath1 = '//*[@id="root"]/div/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/section[1]/div[1]/div'  # 장르 # 글씨를 선택한 것
    driver.find_element('xpath', category_xpath1).click()
    time.sleep(1)

    category_xpath2 = '//*[@id="modal-portal"]/div/div[2]/div[2]/div[{}]'.format(i)     # 카테고리 선택버튼
    driver.find_element('xpath', category_xpath2).click()
    time.sleep(1)

    category_xpath3 = '//*[@id="modal-portal"]/div/div[2]/div[1]/div[2]/button[2]'     # 확인버튼
    driver.find_element('xpath', category_xpath3).click()
    time.sleep(1)


    driver.maximize_window()
    prev_height = driver.execute_script("return document.body.scrollHeight")

    while True: # 무한스크롤 루프
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1) # 페이지가 완전히 내려갈때까지 대기 -> 페이지 길이가 길면 시간을 증가시킨다
        curr_height = driver.execute_script("return document.body.scrollHeight")
        if (curr_height == prev_height):
            break
        else:
            prev_height = driver.execute_script("return document.body.scrollHeight")
    for j in range(1, pages[i-12]):
        category_xpath4 = '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[3]/div[{}]/a'.format(j)     # 제목

        title = driver.find_element('xpath', category_xpath4).text
        title = re.compile('[^가-힣,A-Z,a-z ]').sub(' ', title)
        titles.append(title)

        if j % 10 == 0:
            df_section_title = pd.DataFrame(titles, columns=['titles'])
            df_section_title['category'] = category[i-12]
            df_title = pd.concat([df_title, df_section_title], ignore_index=True)
            df_title.to_csv('./crawling_data/crawling_data_{}_{}.csv'.format(category[i-12], j), index=False)      # crawling_data 폴더(디렉토리) 만들어야함
            titles = []
