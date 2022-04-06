from cmath import sqrt
import matplotlib.pyplot as plt
import math

def drawShape(shapes_listDT):
    
    plt.figure()
    for shape in shapes_listDT:

        #rectangle
        if shape['type']=='rectangle':
            x=shape["upper_left_x"]
            y=shape["upper_left_y"]
            points_x=[x, x+shape["width"], x+shape["width"], x, x]
            points_y=[y, y, y+shape["length"], y+shape["length"], y]
        
            plt.plot(points_x,points_y)

        #triangle
        if shape['type']=='triangle':
           c=shape['edge'] 
           x=shape["lower_left_x"]
           y=shape["lower_left_y"]
           points_x=[x, x+c/2, x+c, x]
           points_y=[y, y+c/2*sqrt(5), y, y] 

           plt.plot(points_x,points_y)

        

    plt.show()


