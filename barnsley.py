import matplotlib.pyplot as plt
import random

x = 0
y = 0
xn = 0
yn = 0



for i in range(10000):

    r = random.random() * 100
    plt.plot(xn,yn,'go',markersize = 0.8)
    print(i)

    if (r<1):
        xn = 0
        yn = 0.16 * y

    elif r < 86:
        xn = 0.85 * x + 0.04 * y
        yn = -0.04 * x + 0.85 * y + 1.6
    elif r < 93:
        xn = 0.20 * x - 0.26 * y
        yn = 0.23 * x + 0.22 * y + 1.6
    else:
        xn = -0.15 * x + 0.28 * y
        yn = 0.26 * x + 0.24 * y + 0.44 

    x = xn
    y = yn
    

    

plt.show()
