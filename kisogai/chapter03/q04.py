import numpy as np
array7=np.arange(1,21).reshape((5,4))#reshapeで多次元配列に変換することができる
a=array7[2,3]
b=array7[:,2]
c=array7[1::2]#開始を1にして、2間隔で抽出
print(array7)
print(a)
print(b)
print(c)