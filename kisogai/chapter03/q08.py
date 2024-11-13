import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0.01,5,100)
y1=np.log(x)
y2=np.log2(x)
y3=np.log10(x)

plt.plot(x,y1,label="log(x)")
plt.plot(x,y2,label="log2(x)")
plt.plot(x,y3,label="log10(x)")



plt.xlabel("x")
plt.ylabel("y")

plt.legend()
plt.show()