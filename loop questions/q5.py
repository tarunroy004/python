n = int(input("Enter a Number : "))
fact = 1
for i in range(n, 1-1, -1) :
    fact  = fact*i
print(f"Factorial of {n} is {fact}")