def createList(list) :
    n = int(input("Enter how many item in the List : "))
    for i in range(0, n) :
        list.append(int(input("Enter Data : ")))
def addItem(list) :
    print("Where you want to Add Item > \n 1) At First\n 2) At Last \n 3) At any Position")
    flag = int(input("Where you want : "))
    if flag==1 :
        list.insert(0, int(input("Enter Data : ")))
    elif flag==2 : 
        list.append(int(input("Enter Data : ")))
    elif flag==3 : 
        list.insert(int(input("Enter the position(Index) : ")), int(input("Enter Data : ")))
def deleteItem(list) :
    item = int(input("Which element you want to Delete : "))
    list.remove(item)

list = []
key = 1
while key :
    print("1 : Create a List")
    print("2 : Add Items in the List")
    print("3 : Delete items from the List") 

    flag = int(input("Enter what you want : "))

    if flag==1 :
        createList(list)
        print("--List Created--")
    elif flag==2 :
        addItem(list)
        print("--Item Added--")
    elif flag==3 :
        deleteItem(list)
        print("--Item Deleted--")
    else :
        print("Enter a valid request...")

    print("The List is = ", list)
    key = int(input("Do you want More(1-yes/0-no) : "))
