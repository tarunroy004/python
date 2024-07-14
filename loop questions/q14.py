num = int(input("Enter a Number : "))
a = 0
b = 1
print(a)
print(b)
# while(b<=num) :
#     c = a+b
#     if c <= num :
#         print(c)
#     a = b
#     b = c
for i in range(1, num-1) :
    c = a+b
    print(c)
    a = b
    b = c