str = input("Enter a String : ")
uppRes = ""
lowRes = ""
res = ""
spsh = ""
for i in str :
    if (i.isupper()) :
        uppRes = uppRes + i
    elif (i.islower()) :
        lowRes = lowRes + i
    elif (i == " ") :
        spsh = spsh + i
res = lowRes+spsh+uppRes
print(f"After sorting the string : {res}")
