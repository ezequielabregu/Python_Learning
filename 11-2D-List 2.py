matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:   # --> en el primer loop me da solo la primera fila [1,2,3]
    for index in row: # --> me da el valor de cada índice de la fila
        print(index)

"""
1er loop = row [0] index [0][1][2]
2do loop = row [1] index [0][1][2]
3er loop = row [2] index [0][1][2]
"""
