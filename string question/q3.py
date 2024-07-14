str = input("Enter a Big String : ")
# char = "abcdefghijklmnopqrstuvwxyz"
# num = "1234567890"
# sym = "`~!@#$%^&*()_-+=}{[];:""',./<>?"
charNO = 0
numNO = 0
symNO = 0
spshNO = 0

for i in str :
    # if (i in char.lower()) or (i in char.upper()) :
    if (i.isalpha()) :
        charNO+=1
    elif (i.isdigit()) :
        numNO+=1
    elif (i == " ") :
        spshNO+=1
    else :
        symNO+=1


print(f"Charecter : {charNO}")
print(f"Number : {numNO}")
print(f"Symbol : {symNO}")
print(f"Spash : {spshNO}")
