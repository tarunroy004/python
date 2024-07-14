n = int(input("Enter a number : "))
sum = 0
i = 2
while i <= n:
    is_prime = True
    j = 2
    while j <= i // 2:
        if i % j == 0:
            is_prime = False
            break
        j += 1
    if is_prime:
        sum += i
    i += 1
print("Sum of all Prime Numbers from 1 to", n, "is :", sum)