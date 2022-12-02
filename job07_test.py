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
test_data = "오래 전, 물의 부족, 흙의 왕국, 불의 제국, 공기의 유목민은 균형을 지키며 평화로운 세상을 유지했지만 불의 제국이 전쟁을 선포하며 평화가 깨졌다. 모든 원소를 다루는 힘을 가진 '아바타'(모든 원소를 다룰 수 있는 벤더)가 있었다면 균형을 유지할 수 있었겠지만, 아바타는 갑자기 사라지고, 세상은 혼돈에 빠졌다. 100년 후, 물의 부족의 두 남매 카타라와 소카가 빙하 속에 백 년 동안 얼어붙어 있던 새로운 아바타이자 마지막 에어벤더인 '아앙' 이라는 12살 소년을 발견하고, 함께 아바타의 숙명인 세상의 균형을 되찾기 위하여 백년전쟁을 끝내기 위해 여정"
okt = Okt()
test_data = okt.morphs(test_data, stem=True)
print(test_data[:10])
stopwords = pd.read_csv('./stopwords.csv', index_col=0)
words = []
for i in test_data:
    if len(i) > 1:
        if i not in stopwords['stopword']:
            words.append(i)
test_data = ' '.join(words)
print(test_data)
with open('./models/laftel_token.pickle', 'rb') as f:
    token = pickle.load(f)
tokened_X = token.texts_to_sequences([test_data])
print(tokened_X)
for i in range(len(tokened_X)):
    if len(tokened_X[i]) > 459:      # 모델이 입력을 20개만 줌
        tokened_X[i] = tokened_X[i][:459]    # 형태소가 20자 보다 많다면 버려라
X_pad = pad_sequences(tokened_X, 459)        # 모델링 할때 데이터 정보가 없으면 0으로 나타냄
#print(X_pad)
model = load_model('./models/laftel_category_classfication_model_0.647.h5')
preds = model.predict(X_pad)
label = encoder.classes_
pred = model.predict(X_pad)
print(pred)
with open('./models/label_encoder.pickle', 'rb') as f:
    encoder = pickle.load(f)
labeled_Y = encoder.transform(Y)
onehot_Y = to_categorical(labeled_Y)
print(label)    # 전체 리스트 출력
print(label[np.argmax(pred)])   # 리스트 속의 예측한 결과를 출력한 것
















