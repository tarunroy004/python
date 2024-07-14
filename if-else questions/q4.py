name = input("Enter your name : ")
age = int(input("Enter your age : "))

if age >= 18 :
    print(f"{name}, you are eligible to give Vote")
elif age < 18 and age > 0 :
    print(f"{name}, you are not eligible to give Vote")