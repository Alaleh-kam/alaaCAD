import shapes_interface as shi
import shapes_graphics as shg

shapes=[]
menu_choice=''
while menu_choice!='0':

    print("1) add shape")
    print("2) list shapes")
    print("3) draw shapes")
    print("0) exit")

    menu_choice=input("Select from the menu:")

    if menu_choice=='1':
        shapes.append(shi.getShape())
    elif menu_choice=='2':
        pass
    elif menu_choice=='3':
        shg.drawShape(shapes)


