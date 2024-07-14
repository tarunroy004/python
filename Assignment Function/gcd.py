def gcd(a, b):
    while b:
        a, b = b, a % b
        return a
num1 = int(input("value1"))
num2 = int(input("Value2"))
gcd = gcd(num1, num2)
print(f"GCD of {num1} and {num2} is {gcd}")
