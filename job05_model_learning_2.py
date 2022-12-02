import numpy as np
import matplotlib.pyplot as plt
from keras.models import *
from keras.layers import *
from sklearn.decomposition import PCA

X_train, X_test, Y_train, Y_test = np.load(
    'models/laftel_titles_data_max_64_wordsize_10792.npy', allow_pickle=True
)
print(X_train.shape, Y_train.shape)
print(X_test.shape, Y_test.shape)

# GRU(Gated Recurrent Unit) LSTM에서의 셀 상태 역할 c가 없다 -> Update Gate, Reset Gate 두가지만 존재
# 임베딩 레이어(Embedding Layer) 임베딩 레이어는 주로 자연어 처리에서 사용되며, 자연어를 수치화된 정보로 바꾸기 위한 레이어
# 임베딩은 값, 텍스트 내의 단어들을 밀집 벡터(dense vector)로 만드는 것
model = Sequential()
model.add(Embedding(10792, 300, input_length=64)) # 의미에 대한 형태소 개수만큼 학습
# padding 출력크기를 보정하기 위해 사용하며 입력데이터의 사방을 특정값으로 채우는 것을 말한다
# padding='same' 출력크기를 입력크기와 동일하게 유지
model.add(Conv1D(32, kernel_size=5, padding='same', activation='relu')) # 글자는 1차원 벡터-> Conv1D 사용
model.add(MaxPool1D(pool_size=1)) #1이면 달라지는게 없다
model.add(GRU(64, activation='tanh', return_sequences=True)) #결과값을 리턴시켜 입력으로 사용 -> return_sequences
model.add(Dropout(0.3))
model.add(GRU(32, activation='tanh', return_sequences=True))
model.add(Dropout(0.3))
model.add(GRU(32, activation='tanh'))
model.add(Dropout(0.3))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(6, activation='softmax'))
model.summary()

model.compile(loss='categorical_crossentropy', optimizer='adam',
              metrics=['accuracy'])
fit_hist = model.fit(X_train, Y_train, batch_size=128,
                     epochs=10, validation_data=(X_test, Y_test))
model.save('./models/laftel_category_calssfication_model_{}.h5'.format(
    np.round(fit_hist.history['val_accuracy'][-1], 3)))

plt.plot(fit_hist.history['accuracy'], label = 'accuracy')
plt.plot(fit_hist.history['val_accuracy'], label = 'val_accuracy')
plt.legend()
plt.show()