import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

rate = 2
xn = 0.6
iters = 1
xnl = [0.6,0.48]

def animate(i):

    global rate
    plt.cla()
    allxnn()
    rate += 0.01
    print(rate)
    if (rate > 4):
        rate = 2


def allxnn():

    global rate,xn,xnl

    for i in range(65):
    
        xnn = xn * rate * (1-xn)
        xn = xnn
        xnl.append(xnn)
        plt.plot([i+1,i],[xnl[len(xnl)-1],xnl[len(xnl)-2]],'b-')
        plt.title('Dependence on rate')
        plt.ylabel('as rate changes by 0.01')
        plt.xlabel('iterations')
        plt.text(0,0,rate)
        
        
anime = FuncAnimation(plt.gcf(),animate, interval = 100)

plt.show()
