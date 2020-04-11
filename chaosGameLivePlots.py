import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation


n = int(input('Enter number of sides of the polygon  i.e. 3,4 and 5 : '))

if (n == 3): 
    plt.plot([0,1,2,0],[0,1,0,0])  #initial triangle
    plt.title("Serpenski's Gasket")
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
        
        plt.plot(mx,my,'go',markersize = 0.4)
        print(i)


elif (n==4):

    plt.plot([0,0,1,1,0],[0,1,1,0,0]) #initial square
    plt.title("Chaos game with square")
    mx = 0.5
    my = 0.5
    ran = 5

    def animate(i):
        
        a = random.randint(1,4)
        global mx
        global my

        global ran

        if (a== 1 and ran != a):
            
            nmx = (mx+0)/2
            nmy = (my+0)/2 
            mx = nmx
            my = nmy
            ran = a
            
        elif (a== 2 and ran !=a):
            nmx = (mx+1)/2
            nmy = (my+0)/2 
            mx = nmx
            my = nmy
            ran = a 
                        
        elif (a== 3 and ran !=a):
            nmx = (mx+1)/2
            nmy = (my+1)/2 
            mx = nmx
            my = nmy
            ran = a
 
        elif (a== 4 and ran != a):
            nmx = (mx+0)/2
            nmy = (my+1)/2 
            mx = nmx
            my = nmy
            ran = a
            
        print(i) 
        plt.plot(mx,my,'go',markersize = 0.4)


elif( n == 5):
    
    plt.plot([0,-0.61,-0.5,0.5,0.61,0],[1.22,0.61,0,0,0.61,1.22]) # surrounding pentagon
    plt.title("Chaos game with pentagon")
    mx = 0.5
    my = 0.5
    ran = 6

    def animate(i):
        
        a = random.randint(1,5)
        global mx
        global my

        global ran

        if (a== 1 and ran != a):
            
            nmx = (mx+0)/2
            nmy = (my+1.22)/2 
            mx = nmx
            my = nmy
            ran = a
            
        elif (a== 2 and ran !=a):
            nmx = (mx-0.61)/2
            nmy = (my+0.61)/2 
            mx = nmx
            my = nmy
            ran = a 
                        
        elif (a== 3 and ran !=a):
            nmx = (mx-0.5)/2
            nmy = (my+0)/2 
            mx = nmx
            my = nmy
            ran = a
 
        elif (a== 4 and ran != a):
            nmx = (mx+0.5)/2
            nmy = (my+0)/2 
            mx = nmx
            my = nmy
            ran = a
        
        elif(a==5 and ran!= a):
            nmx = (mx+0.61)/2
            nmy = (my+0.61)/2 
            mx = nmx
            my = nmy
            ran = a

            
        print(i) 
        plt.plot(mx,my,'go',markersize = 0.4)


else:
    print('PICK 3,4 or 5')

ani = FuncAnimation(plt.gcf(),animate,interval = 0.0001)
plt.show()

