a = int(input("Enter a Number : "))
org = a
sum = 0
while (a>0) :
    sum = (10*sum) + a%10
    a = a//10 
    
if (sum==org) :
    print(f"{org} is a Palindrom Number")
else :
    print(f"{org} is not a Palindrom Number")