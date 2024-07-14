n = 1
fac = 1
while n>=0 :
    n = int(input("Enter a Number : "))
    if n>=0 :
        for i in range(1, n+1) :
            fac*=i
        print("Factorial of", n, "is :", fac)
    else :
        print("Enter a Positive Number...")
    fac = 1