import shapes_interface as shi
import shapes_graphics as shg

shapes_listDT=[]
menu_choice=''
while menu_choice!=0:

    print("1) add shape")
    print("2) list shapes")
    print("3) draw shapes")
    print("0) exit")

    menu_choice1=input("Select from the menu:")


    if menu_choice1==1:

        print("1) rectangle")
        print("2) triangle")
        menu_choice2=input("Select from the menu:")

        if menu_choice2==1:
            shapes_listDT.append(shi.getRectangle())
        elif menu_choice2==2:
            shapes_listDT.append(shi.getTriangle())
            
    elif menu_choice1==2:
        shi.printList(shapes_listDT)
    elif menu_choice1==3:
        shg.drawShape(shapes_listDT)


