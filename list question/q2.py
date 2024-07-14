lst = []
sz = int(input("Enter List Size : "))
for i in range(0, sz) :
    lst.append(input("Enter eliment : "))
print(f"The list :---")
for i in range(sz-1, 0-1, -1) :
    print(lst[i])