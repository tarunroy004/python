lst = []
sz = int(input("Enter List Size : "))
for i in range(0, sz) :
    lst.append(int(input(f"Enter eliment in Index Number {i} : ")))
print(f"The list :---")
for i in range(0, sz) :
    print(lst[i], end=" ")