num = int(input("Enter a Number : "))
print(f"Strong suner under {num}")
for i in range(1, num+1) :
    sum = 0
    temp = i
    while(temp>0) :
        j = 1
        fact = 1
        r = temp%10
        while(j<=r) :
            fact = fact*j
            j = j+1
        sum = sum+fact
        temp = temp//10
    if (sum==i) :
        print(i)
