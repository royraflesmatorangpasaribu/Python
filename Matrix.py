import random
matrix = []
numberOfRows = eval(input("Enter the number of row : "))
numberOfaColumns = eval(input("Enter the number of columns : "))

for row in range(numberOfRows):
    matrix.append([])
    for column in range(numberOfaColumns):
        value = eval(input("Enter an element and press Enter: "))
        matrix[row].append(value)

print("Matrix ",numberOfRows, "X", numberOfaColumns)
for baris in range(len(matrix)):
    for kolom in range(len(matrix[baris])):
        print(matrix[baris][kolom], end = "\t ")
    print()  
hasil = 0

for column in range(len(matrix[0])):
    total = 0
    for row in range(len(matrix)):
        total += matrix[row][column]
    hasil += total
    print("Total rata-rata pada kolom ", column, " = ", total/len(matrix))
    
print("Jumlah rata-rata kolom : ", hasil/len(matrix))
    
