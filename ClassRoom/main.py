def count(string):
    temp = string.lower().split()
    dict = {}
    for item in temp:
        dict[item] = temp.count(item)
    print(dict)

sent = input("Enter a String : ")
count(sent)