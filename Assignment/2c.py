n = int(input("Enter a Positive Number : "))
if n>0 :
    cnt = 0
    for i in range(1, n+1) :
        if n%i==0 :
            cnt+=1
    if cnt == 2 :
        print(n, "is a Prime Number.")
    else :
        print(n, "is not a Prime Number.")
else :
    print("Enter a Positive Number please...")
            