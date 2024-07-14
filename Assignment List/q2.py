lst = []
sz = int(input("Enter List Size : "))
odd = []
even = []
for i in range(0, sz) :
    lst.append(int(input(f"Enter Element in Index {i} : ")))
for i in range(0, sz) :
    if lst[i]%2==0 :
        even.append(lst[i])
    else :
        odd.append(lst[i])

print("\nOdd Elements :--")
for i in range(0, len(odd)) :
    print(odd[i], end=" ")

print("\nEven Elements :--")
for i in range(0, len(even)) :
    print(even[i], end=" ")
