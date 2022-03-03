def getShape():
    print("The only available shape is currently rectangle")
    newShape={}
    newShape["width"]=float(input("width:"))
    newShape["length"]=float(input("length:"))
    newShape["upper_left_x"]=float(input("upper left x:"))
    newShape["upper_left_y"]=float(input("upper left y:"))
    return newShape