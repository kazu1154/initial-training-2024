import math
for x in range(0,361): #0から360までの整数値がxに代入
    sin=math.sin(math.radians(x))#math.radians(x) で角度をラジアンに変換
    cos=math.cos(math.radians(x))#math.cos(math.radians(x)) は x 度のコサイン値を計算
    tan=math.tan(math.radians(x))
    print(x,sin,cos,tan)