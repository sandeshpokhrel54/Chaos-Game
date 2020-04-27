import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation

plt.plot([0,1,2,0],[0,1,0,0])
mx = 1.0
my = 0.5

def animate(i):
   
    a = random.randint(1,3)
    global mx
    global my

    if (a== 1):
        nmx = (mx+0)/2
        nmy = (my+0)/2        
        mx = nmx
        my = nmy
    elif (a== 2):
        nmx = (mx+1)/2
        nmy = (my+1)/2       
        mx = nmx
        my = nmy
    else :
        nmx = (mx+2)/2
        nmy = (my+0)/2         
        mx = nmx
        my = nmy
            
    plt.plot(mx,my,'go')
    print(i)
    
ani = FuncAnimation(plt.gcf(),animate,interval = 10)  #how often you want the function to be called interval in milliseconds
plt.show()
