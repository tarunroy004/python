lst = [1, 8, 32, 45, 6, 7, -1089, -23, 789, 125, 53, 3, 9, 78]
srt = []
temp = 0
for i in range(1, len(lst)) :
    temp = lst[i-1]
    if lst[i] >= temp :
        temp = lst[i]
    srt.append(temp)
print(srt)