def plndrm(str) :
    sm = ""
    for i in range(len(str)-1, 0-1, -1) :
        sm+=str[i]
    if str == sm :
        return f"{str} is a Pallindrome String"
    else :
        return f"{str} is not a Pallindrome String"


string = input("Enter a String : ")
print(plndrm(string))