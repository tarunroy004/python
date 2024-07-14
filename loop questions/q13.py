num = int(input("Enter a Number : "))
count = 0
print(f"All the Prime Numbers Under {num}")
for i in range(1, num+1) : 
    for j in range(1, i+1) :
        if (i%j==0) :
            count+=1
    if (count==2) :
        print(f"{i}")
    count=0