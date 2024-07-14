lst = [1, 8, 32, 45, 6, 7, -1089, -23, 789, 125, 53, 3, 9, 78]
grt = 0
ind = 0

for i in range(0, len(lst)) :
    if lst[i] >= grt :
        grt = lst[i]
        ind = i

print(f"Greater Element is : {grt}, and it's index is {ind}")