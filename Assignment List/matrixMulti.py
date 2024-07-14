
matrix1 = []
matrix2 = []
res = []
Row = 3
Column = 3
print("Enter first matrix elements row wise :")
for row in range(Row):    
    list1 = []
    for column in range(Column):   
        list1.append(int(input()))
    matrix1.append(list1)

print("Enter second matrix elements row wise :")
for row in range(Row):    
    list1 = []
    for column in range(Column):   
        list1.append(int(input()))
    matrix2.append(list1)

for row in range(Row):    
    list1 = []
    for column in range(Column):   
        list1.append(int(0))
    res.append(list1)

for i in range(Row):
    for j in range(Column):   
        for k in range(Column) :
            res[i][j] += matrix1[i][k] * matrix2[k][j]




print()
for row in range(Row):
    for column in range(Column):
        print(matrix1[row][column], end=" ")
    print()
print("Multiplide by ")
for row in range(Row):
    for column in range(Column):
        print(matrix2[row][column], end=" ")
    print()
print("Is -- ")
for row in range(Row):
    for column in range(Column):
        print(res[row][column], end=" ")
    print()