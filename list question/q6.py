lst = [1, 8, 32, 45, 6, 7, -1089, -23, 789, 125, 53, 3, 9, 78]
# lst = [1254, 789, 356, 124, 78, 32, 26, 21, 10, 4, 2, 0, -1, -10]
srt = True

for i in range(1, len(lst)) :
    if lst[i] > lst[i-1] :
        srt = False
if srt == True :
    print("The List is Sorted")
else :
    print("The List is not sorted")