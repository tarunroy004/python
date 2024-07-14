def isPrime(n) :
    flag = 0
    for i in range(2, n) :
        if n%i==0 :
            flag+=1
    if flag==0 :
        return 1
    else :
        return 0

num = int(input("Enter a Number to Check : "))
if isPrime(num) :
    print(f"{num} is a Prime Number.")
else :
    print(f"{num} is not a Prime Number.")