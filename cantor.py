import matplotlib.pyplot as plt


x = [2,8]
y = [8,8]

def plot(x,y,counter):

    if (counter) > 1   :

        plt.plot(x,y,'b')

        plot([x[0],x[0]+(x[1]-x[0])/3] , [y[0]-0.5,y[1]-0.5],counter/3)
        plot([2/3*(x[1]-x[0])+x[0],x[1]] , [y[0]-0.5,y[1]-0.5],counter/3)
        print(counter)
        
    
    

plot(x,y,900)
plt.show()
