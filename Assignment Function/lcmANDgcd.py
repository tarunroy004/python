def islcm(n1, n2, lcm) :
    if lcm%n1==0 and lcm%n2==0 :
        return lcm
    else : return islcm(n1, n2, lcm+1)

def isgcd(a, b) :
    if a%b==0 :
        return b
    else :
        return  isgcd(b, a-b)

n1 = int(input("Enter a Number : "))
n2 = int(input("Enter another Number : "))

if n1 > n2 :
    lcm = n1
    gcd = isgcd(n1, n2)
else :
    lcm = n2
    gcd = isgcd(n2, n1)
lcm = islcm(n1, n2, lcm)
print(f"LCM of {n1} and {n2} is {lcm}")
print(f"GCD of {n1} and {n2} is {gcd}")