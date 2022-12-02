import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from konlpy.tag import Okt
from keras_preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
import pickle
from keras.models import load_model

pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', 15)
df = pd.read_csv('./crawling_data_4/aniplus_crawling_data_20221201.csv')
print(df.head())
df.info()

X = df['summary']
# for i in range(len(X)):
#     if len(X[i].split()) > 50:
#         temp = X[i].split()[:50]
#         X[i] = ' '.join(temp)

Y = df['category']

with open('./models/label_encoder.pickle', 'rb') as f:
    encoder = pickle.load(f)
labeled_Y = encoder.transform(Y)
onehot_Y = to_categorical(labeled_Y)

okt = Okt()
for i in range(len(X)):
    X[i] = okt.morphs(X[i], stem=True)
stopwords = pd.read_csv('./stopwords.csv', index_col=0)
for j in range(len(X)): # 2글자 이상만 출력
    words = []
    for i in range(len(X[j])):
        if len(X[j][i]) > 1:
            if X[j][i] not in stopwords['stopword']: #불용어에 없으면 words에 추가
                words.append(X[j][i])
    X[j] = ' '.join(words) #불용어 사전에 없는 단어만 출력

with open('./models/laftel_token.pickle', 'rb') as f:
    token = pickle.load(f)
tokened_X = token.texts_to_sequences(X) # 순서대로 할때는 시퀀스를 사용한다
for i in range(len(tokened_X)):
    if len(tokened_X[i]) > 64:
        tokened_X[i] = tokened_X[i][:64] #50글자보다 크면 삭제한다
X_pad = pad_sequences(tokened_X, 64)

model = load_model('./models/laftel_category_calssfication_model_0.644.h5')
preds = model.predict(X_pad)
label = encoder.classes_
category_preds = []
for pred in preds:
    category_pred = label[np.argmax(pred)]
    category_preds.append(category_pred)
df['predict'] = category_preds

print(df.head(30))

df['OX'] = False
for i in range(len(df)):
    if df.loc[i, 'category'] == df.loc[i, 'predict']:
        df.loc[i, 'OX'] = True

df.info()
print(df.head(30))
print(df['OX'].value_counts())
print(df['OX'].mean()) # 평균값을 보면 정답률이 된다
print(df.loc[df['OX']==False])