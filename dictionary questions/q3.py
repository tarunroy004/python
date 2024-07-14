list = [2,4,5,4,2,2,4,5,3,6,4,7,8,9,6,4,1,2,5,4,89,7,5,6,9,8,4,3,2,6]
# method 1
st = set(list)
dict = {}
for i in st :
    cnt = 0
    for j in list :
        if i == j :
            cnt+=1
    dict[i] = cnt

# method 2 
# dict = {}
# for i in list :
#     if i in dict.keys() :
#         dict[i] = dict[i]+1
#     else :
#         dict[i] = 1

print(dict)