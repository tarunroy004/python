def sortDict(dict1, n) :
    for i in range(1, n) :
        for j in range (i+1, n+1) :
            if dict1[i] > dict1[j] :
                temp = dict1[j]
                dict1[j] = dict1[i]
                dict1[i] = temp

def sortDictDicn(dict1, n) :
    for i in range(1, n) :
        for j in range (i+1, n+1) :
            if dict1[i] < dict1[j] :
                temp = dict1[j]
                dict1[j] = dict1[i]
                dict1[i] = temp


dict = {
    1 : 53,
    2 : 85,
    3 : 14,
    4 : 125,
    5 : 18,
    6 : 22,
    7 : 24,
    8 : 4,
    9 : 199,
    10 : 49 
}

sortDict(dict, 10)
print(dict)
sortDictDicn(dict, 10)
print(dict)

