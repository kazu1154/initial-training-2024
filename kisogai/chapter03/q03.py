import numpy as np
#array3=np.array([0,0,0,0,0,0]).reshape(3,3)
array3=np.zeros((3,3))#指定した形状の全ての要素が0の配列
#array4=np.array([1,1,1,1,1,1]).reshape(3,3)
array4=np.ones((3,3))#全ての要素が1の配列
array5=np.random.uniform(-1,1,(3,3))#任意の範囲の連続一様分布から浮動小数点数の乱数を生成する関数
array6=np.eye(3)*2
#np.eyeは関数は単位行列を作成する関数です。単位行列とは、対角線の要素が1で、それ以外の要素は0で構成されている配列
print(array3)
print(array4)
print(array5)
print(array6)