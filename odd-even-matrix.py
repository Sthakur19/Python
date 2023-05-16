# write a function which tells us for a given 2D matrix if their elements are "odd" or "even"

# |1 2 3|
# |2 2121 2|

# |'odd' 'even' 'odd'|
# |'even' 'odd' 'even'|

def oddEvenMatrix(matrix):
    rowMatrix = len(matrix)
    colMatrix = len(matrix[0])
    oddorEvenMatrix = []
   
    for i in range(rowMatrix):
        evenOddRow = []
        for j in range(colMatrix):
            evenOddRow.append("")
        oddorEvenMatrix.append(evenOddRow)
       
    for i in range(rowMatrix):
        for j in range(colMatrix):

            cellValue = 'even'
            if matrix[i][j] % 2 == 1:
                cellValue = 'odd'
            oddorEvenMatrix[i][j] = cellValue
    
    return oddorEvenMatrix


myMatrix = [[1, 2], [21, 21], [2023, 2024]]
print(myMatrix)
print(oddEvenMatrix(myMatrix))