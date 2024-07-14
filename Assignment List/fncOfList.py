list = [10, 20, 30, 40]
print("The list is : ", list)

# Add items
list.append(50)
list.insert(2, 100)

# Accesing
print("20 is in the index no. of ", list.index(20))

# Copy
copy1 = list.pop(3)
copy2 = list.copy()

# Delete
copy2.remove(10)
list.clear()

# sort
copy2.sort()

# reverse
copy2.reverse()

print(list)
print(copy1)
print(copy2)