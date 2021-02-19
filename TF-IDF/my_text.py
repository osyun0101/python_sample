import tfidf
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop


text1 = """
野球を観るのは楽しいものです。
試合だけでなくインタビューも楽しみです。
"""
text2 = """
常にiPhoneとiPadを持っているので、
二口あるモバイルバッテリがあると便利。
"""
text3 = """
幸せな結婚の秘訣は何でしょうか。
夫には敬意を、妻には愛情を示すことが大切。
"""

tfidf.load_dic('./text/genre-tfidf.dic')
in_size = len(tfidf.dt_dic)
out_size = 4

model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(in_size,)))
model.add(Dropout(0.2))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(out_size, activation='softmax'))
model.compile(
    loss='categorical_crossentropy',
    optimizer=RMSprop(),
    metrics=['accuracy']
)
model.load_weights('./text/genre-model.hdf5')

def check_tf(text):
    LABELS = ['スポーツ', 'IT', '映画', 'ライフ']
    data = tfidf.calc_text(text)
    pre = model.predict(np.array([data]))[0]
    n = pre.argmax()
    print(LABELS[n], pre[n])
    return LABELS[n], float(pre[n]), int(n)


if __name__=='__main__':
    check_tf(text1)
    check_tf(text2)
    check_tf(text3)
