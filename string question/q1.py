str = input("Enter a String : ")
res = ""

for i in range(len(str)-1, 0-1, -1) :
    res = res + str[i]

res = res.upper()
print(f"The Revers String is : {res}")