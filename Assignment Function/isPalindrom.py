def isPalindrom(n) :
    sum = 0
    cpy = n
    while cpy > 0 :
        sum = sum*10 + cpy%10
        cpy //= 10
    if sum == n : return 1 
    else : return 0

num = int(input("Enter a Number : "))

if isPalindrom(num) :
    print(f"{num} is a Palindrom Number.")
else :
    print(f"{num} is not a Palindrom Number.")
