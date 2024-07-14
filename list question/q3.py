lst = [7, -8, 0, 9, -12, -58, 3, 154, -92, 2, 5, 3, -1]
pos = []
neg = []

for i in range(0, len(lst)) :
    if lst[i]>=0 :
        pos.append(lst[i])
    else :
        neg.append(lst[i])

print("Positive List :---")
print(pos)
print("Negetive List :---")
print(neg)

