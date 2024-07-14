n = int(input("Enter a Number : "))
sum = 0
for i in range(1, n) :
    if (n%i==0) :
        sum+=i
if (n==sum) :
    print(f"{n} is a Perfect Number")
else :
    print(f"{n} is not a Perfect Number")
