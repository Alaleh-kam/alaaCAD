import shapes_interface as shi
import shapes_graphics as shg

shapes_listDT=[]
menu_choice=''
while menu_choice!=0:

    print("1) add rectangle")
    print("2) add triangle")
    print("3) list shapes")
    print("4) draw shapes")
    print("0) exit")

    menu_choice=input("Select from the menu:")

    if menu_choice==1:
        shapes_listDT.append(shi.getRectangle())
    elif menu_choice==2:
        shapes_listDT.append(shi.getTriangle())
    elif menu_choice==3:
        shi.printList(shapes_listDT)
    elif menu_choice==4:
        shg.drawShape(shapes_listDT)


