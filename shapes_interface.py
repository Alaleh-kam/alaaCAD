def getRectangle():
    #Rectangle
    newShape={}
    newShape["width"]=input("width:")
    newShape["length"]=input("length:")
    newShape["upper_left_x"]=input("upper left x:")
    newShape["upper_left_y"]=input("upper left y:")
    newShape["type"]="rectangle"
    return newShape

def getTriangle():
    #Triangle
    newShape={}
    newShape["edge"]=input("edge:")
    newShape["lower_left_x"]=input("lower left x:")
    newShape["lower_left_y"]=input("lower left y:")
    newShape["type"]="triangle"
    return newShape

def printList(shapes):
    c=0
    for i in shapes:
        a=""
        for key in i:
            m=""
            m= key +" "+":"+" "+str(i[key])
            a=a+m+" "+","
            
        c=c+1
        print("Shape"+" "+str(c)+":"+" "+a[:-1]) #it means: it will omit the last element which is ","

