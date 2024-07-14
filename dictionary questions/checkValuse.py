dict = {
    1 : 18,
    2 : 18,
    3 : 18,
    4 : 18,
    5 : 18,
    6 : 18,
    7 : 18,
    8 : 18,
    9 : 18,
    10 : 18 
}
flag = 0
for i in range(1, 11) :
    if dict[1] == dict[i] :
        flag += 1

if flag == 10 :
    print("All values are same in the Dictionary")
