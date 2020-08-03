import random

import numpy as np
from matplotlib import pyplot as plt

x = list(range(1,100))
# random.shuffle(x)
y = list(range(1,100))
plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x,y,color="red")
random.shuffle(y)
plt.plot(x,y,color="blue")
plt.savefig("1.jpg")
plt.show()
