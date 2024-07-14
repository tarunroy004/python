string = 'Tarun Kumar Roy'
stringWordsFreequency = {}
string2 = string.lower()
for i in range(0, len(string2)) :
    stringWordsFreequency[string2[i]] = 0

for i in range(0, len(string2)) :
    if string2[i] in stringWordsFreequency.keys() :
        stringWordsFreequency[string2[i]] += 1

print(stringWordsFreequency)