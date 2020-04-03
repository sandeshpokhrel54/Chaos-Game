import matplotlib.pyplot as plt
import random

plt.plot([0,1,2,0],[0,1,0,0])
mx = 1.0
my = 0.5


for i in range(3000):

    
    a = random.randint(1,3)

    if (a== 1):

        nmx = (mx+0)/2
        nmy = (my+0)/2 
        plt.plot(nmx,nmy,'go')
        mx = nmx
        my = nmy


    elif (a== 2):
        nmx = (mx+1)/2
        nmy = (my+1)/2 
        plt.plot(nmx,nmy,'go')
        mx = nmx
        my = nmy


    else :
        nmx = (mx+2)/2
        nmy = (my+0)/2 
        plt.plot(nmx,nmy,'go')
        mx = nmx
        my = nmy
        

    
    plt.plot(mx,my,'go')
    print(i)
    

plt.show()



    


    


plt.show()

