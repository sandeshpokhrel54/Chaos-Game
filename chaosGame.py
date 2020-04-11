import matplotlib.pyplot as plt
import random


n = int(input('Enter number of sides of the shape you want to create a gasket for i.e. 3,4 or 5 : '))

if (n == 3): 
    plt.plot([0,1,2,0],[0,1,0,0])
    plt.title("Serpenski's Gasket")
    mx = 1.0
    my = 0.5


    for i in range(10000):

    
        a = random.randint(1,3)

        if (a== 1):

            nmx = (mx+0)/2
            nmy = (my+0)/2 
            plt.plot(nmx,nmy,'go',markersize = 0.4)
            mx = nmx
            my = nmy


        elif (a== 2):
            nmx = (mx+1)/2
            nmy = (my+1)/2 
            plt.plot(nmx,nmy,'go',markersize = 0.4)
            mx = nmx
            my = nmy


        else :
            nmx = (mx+2)/2
            nmy = (my+0)/2 
            plt.plot(nmx,nmy,'go',markersize = 0.4)
            mx = nmx
            my = nmy
            
        print(i)


if (n==4):
    plt.plot([0,0,1,1,0],[0,1,1,0,0])
    plt.title("Chaos game with square")
    mx = 0.5
    my = 0.5
    ran = 5

    for i in range(10000):
        
        a = random.randint(1,4)

        if (a== 1 and ran != a):
            
            nmx = (mx+0)/2
            nmy = (my+0)/2 
            mx = nmx
            my = nmy
            ran = a
            
           

        elif (a== 2 and ran != a):
            nmx = (mx+1)/2
            nmy = (my+0)/2 
            mx = nmx
            my = nmy
            ran = a
            
              
        elif (a== 3 and ran!= a):
            nmx = (mx+1)/2
            nmy = (my+1)/2 
            mx = nmx
            my = nmy
            ran = a
            
        
        elif (a== 4 and bouncer4):
            nmx = (mx+0)/2
            nmy = (my+1)/2 
            mx = nmx
            my = nmy
            ran = a
           
        plt.show(mx,my,'go',markersize = 0.4)
        print(i) 
        
if (n == 5):
    plt.plot([0,-0.61,-0.5,0.5,0.61,0],[1.22,0.61,0,0,0.61,1.22])
    plt.title("Chaos game with pentagon")
    mx = 0.5
    my = 0.5
    ran = 6

    for i in range(50000):
        
        a = random.randint(1,5)

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
        
        
        
plt.show()
