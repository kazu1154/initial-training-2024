import numpy as np
import matplotlib.pyplot as plt #グラフを描画するライブラリ
x=np.linspace(-5,5,400)
y=x**3-6*(x**2)+9*x-3

x1=x-2
y1=y+2

plt.plot(x,y,label="x**3-6*(x**2)+9*x-3")
plt.plot(x1,y1,label="after")

plt.xlabel("x")
plt.ylabel("y")

plt.legend()
plt.show()