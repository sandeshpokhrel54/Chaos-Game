from manim import *

class bif(GraphScene):
   # config.x_min = 2.4
   # config.x_max = 4
   # config.y_min = 0
   # config.y_max = 1
   # config.y_tick_frequency = 1
   # config.x_tick_frequency = 2 
    def construct(self):
        self.x_min = 2.4
        self.y_min = 0
        self.x_max = 4
        self.y_max = 1
        self.axes_color = BLUE
        self.setup_axes()
       # checkx = 2.5 
       # checky =  0.7
       # checkDot = Dot([checkx,checky,0])
       # checkDot.move_to(self.coords_to_point(checkx,checky))
       # self.add(checkDot)
        #compute
        r = 2.4 
        xn = 0.60
        xnext = r*xn * (1-xn);
        xn = xnext
        while(r<4):
            #first letting the result settle after 100 iterations
            for i in range(100):
                if(xnext == 0):
                    break;
                xnext = r * xn * (1-xn)
                xn = xnext
            #now the settled points are plotted
            for i in range(100):
                dot = Dot([r,xn,0], radius= 0.008)
                dot.move_to(self.coords_to_point(r,xn))
                xnext = r * xn *(1-xn)
                xn = xnext
               # print(xn)
                self.add(dot)
            r = r + 0.001
            #print("next")
        
        self.wait(3)
        #make larger
        #animate

