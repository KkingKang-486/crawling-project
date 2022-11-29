import pandas as pd
import glob
import datetime

data_path = glob.glob('./crawling_data/*.csv')
print(data_path)
df = pd.DataFrame()
for path in data_path[:-4]:
    df_temp = pd.read_csv(path)
    df = pd.concat([df, df_temp], ignore_index=True)
df.drop_duplicates(inplace=True) #중복데이터 제거
df.reset_index(inplace=True) #중복데이터 제거
print(df.head(30))
df.dropna(inplace=True)
df.reset_index(inplace=True, drop=True)
del df['index'] # 중복데이터 제거 후 index 생겨서 index 삭제
print(df.head())
df.info()
df.to_csv('./crawling_data/laftel_crawling_data_{}.csv'.format(
    datetime.datetime.now().strftime('%Y%m%d')), index=False)