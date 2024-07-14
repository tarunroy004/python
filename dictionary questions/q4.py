dict1 = {
    1 : 50,
    2 : 60,
    3 : 80,
    4 : 40
}
dict2 = {
    3 : 10,
    5 : 20,
    4 : 70,
    6 : 30
}

for i in dict2.keys() :
    if i in dict1.keys() :
        dict1[i] += dict2[i]
    else :
        dict1[i] = dict2[i]

print(dict1)