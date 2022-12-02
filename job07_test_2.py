test_data = "내전의 시대이다. 비밀기지에서 공습을 감행한 반란군 함대는 사악한 은하 제국을 상대로 첫 번째 승리를 거두었다. 전투 도중, 반란군 첩보원은 제국의 절대적인 무기로, 행성 전체를 파괴할 위력을 지닌 무장된 우주 기지 죽음의 별의 기밀 설계도를 탈취하는 데 성공했다."
test_data = okt.morphs(test_data, stem=True)
print(test_data[:10])
words = []
for i in test_data:
    if len(i) > 1:
        if i not in stopwords['stopword']:
            words.append(i)
test_data = ' '.join(words)
print(test_data)
tokened_X = token.texts_to_sequences([test_data])
print(tokened_X)
for i in range(len(tokened_X)):
    if len(tokened_X[i]) > 459:      # 모델이 입력을 20개만 줌
        tokened_X[i] = tokened_X[i][:459]    # 형태소가 20자 보다 많다면 버려라
X_pad = pad_sequences(tokened_X, 459)        # 모델링 할때 데이터 정보가 없으면 0으로 나타냄
#print(X_pad)
pred = model.predict(X_pad)
print(pred)
print(label[np.argmax(pred)])
print(label)