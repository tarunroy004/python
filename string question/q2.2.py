str = input("Enter a String : ")
spl = str.split()
res = ""
for i in spl : 
    for j in i :
        if j.islower() :
            res+=j
    for k in i :
        if k.isupper() :
            res+=k
    for l in str :
        if l == " " :
            res+=l

print(f"After Sorting : {res}")