import matplotlib.pyplot as plt
import random


n = int(input('Enter number of sides of the shape you want to create a gasket for i.e. 3 or 4 :'))

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
    bouncer1 = True
    bouncer2 = True
    bouncer3 = True
    bouncer4 = True

    for i in range(10000):
        
        a = random.randint(1,4)

        if (a== 1 and bouncer1):
            
            nmx = (mx+0)/2
            nmy = (my+0)/2 
            plt.plot(nmx,nmy,'go',markersize = 0.4)
            mx = nmx
            my = nmy
            bouncer1 = False
            bouncer2 = True
            bouncer3 = True
            bouncer4 = True
            
           

        elif (a== 2 and bouncer2):
            nmx = (mx+1)/2
            nmy = (my+0)/2 
            plt.plot(nmx,nmy,'go',markersize = 0.4)
            mx = nmx
            my = nmy
            bouncer1 = True
            bouncer2 = False
            bouncer3 = True
            bouncer4 = True
            
              
        elif (a== 3 and bouncer3):
            nmx = (mx+1)/2
            nmy = (my+1)/2 
            plt.plot(nmx,nmy,'go',markersize = 0.4)
            mx = nmx
            my = nmy
            bouncer1 = True
            bouncer2 = True
            bouncer3 = False
            bouncer4 = True
            
        
        elif (a== 4 and bouncer4):
            nmx = (mx+0)/2
            nmy = (my+1)/2 
            plt.plot(nmx,nmy,'go',markersize = 0.4)
            mx = nmx
            my = nmy
            bouncer1 = True
            bouncer2 = True
            bouncer3 = True
            bouncer4 = False
           

        print(i) 

plt.show()



    


    




