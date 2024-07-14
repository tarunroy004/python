def counter(str) :
    count = 0
    count2 = 0
    for i in str :
        if i in "AEIOUaeiou" :
            count+=1
        elif i == " " :
            continue
        else :
            count2+=1
    return f"In your name total number of vowels is {count} and consonant is {count2}."

str = input("Enter Your Name : ")
print(counter(str))
