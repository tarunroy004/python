dict = {
    1 : 53,
    3 : 14,
    5 : 18,
    7 : 24,
    9 : 199,
}
dict2 = {
    2 : 25,
    4 : 54,
    6 : 12,
    8 : 42,
    10 : 449 
}
dict3 = {}
dict3.update(dict)
dict3.update(dict2)

print(dict3)