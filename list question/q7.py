# lst = [124, 78, 32, 21, 10, 4, 2, 0, 2, 4, 10, 21, 32, 78, 124]
# lst = [124, 78, 32, 21, 10, 4, 2, 0, 1, 3, 2, 4, 10, 21, 32, 78, 124]
lst = [124, 78, 32, 21, 10, 4, 2, 2, 4, 10, 21, 32, 78, 124]
sz = 0

j = -1
for i in range(0, int(len(lst)/2)) :
    if lst[i] != lst[j] :
        sz+=1
    j = j-1

if sz == 0 :
    print("The list is a Palindromic list")
else :
    print("The list is not a Palindromic list")
