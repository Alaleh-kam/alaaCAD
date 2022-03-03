import matplotlib.pyplot as plt

def drawShape(shape):
    #assumes a rectangle
    x=shape["upper_left_x"]
    y=shape["upper_left_y"]
    points_x=[x, x+shape["width"], x+shape["width"], x, x]
    points_y=[y, y, y+shape["length"], y+shape["length"], y]

    plt.figure()
    plt.plot(points_x,points_y)
    plt.show()


