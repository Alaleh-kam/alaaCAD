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

def printList(shapes_listDT):
    shape_number=0
    for shape_dict in shapes_listDT:
        Final_listview="" 
        for key in shape_dict:
            temp_listview=""
            temp_listview= key +" "+":"+" "+str(shape_dict[key])
            final_listview=final_listview+temp_listview+" "+","
            
        shape_number=shape_number+1
        print("Shape"+" "+str(shape_number)+":"+" "+Final_listview[:-1]) #it means: it will omit the last element which is ","

