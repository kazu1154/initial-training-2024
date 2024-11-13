import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-2,2,400)
y1=2**x
y2=2**-x
plt.plot(x,y1,label="2**x")
plt.plot(x,y2,label="2**-x")

plt.xlabel("x")
plt.ylabel("y")

plt.legend()
plt.show()