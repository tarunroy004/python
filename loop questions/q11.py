num = int(input("Enter a Number : "))
sum = 0
temp = num
while(num>0) :
    i = 1
    fact = 1
    r = num%10
    while(i<=r) :
        fact = fact*i
        i+=1
    print(f"factorial of {r} is {fact}")
    sum += fact
    num = num//10
print(f"sum of factorials is {sum}")

if (temp == sum) :
    print(f"So {temp} is a Strong Number")
else :
    print(f"No {temp} is not a Strong Number")