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

i = int(input("Enter a key to check : "))

if i in dict.keys() :
    print(f"{i} is exists in the Dictionary")
else :
    print(f"{i} is not exists in the Dictionary")

