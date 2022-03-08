def getShape():
    print("The only available shape is currently rectangle")
    newShape={}
    newShape["width"]=input("width:")
    newShape["length"]=input("length:")
    newShape["upper_left_x"]=input("upper left x:")
    newShape["upper_left_y"]=input("upper left y:")
    return newShape