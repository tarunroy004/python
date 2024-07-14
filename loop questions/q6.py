n = int(input("Enter a Number : "))
print(f"All the factors of {n} is : ")
for i in range(1, n+1) :
    if (n%i==0) :
        print(i, end = " ")
    