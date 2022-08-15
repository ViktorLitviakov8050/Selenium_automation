# size = int(input('Введите размер таблицы: '))
#
#
#
# matrix = [] # empty matrix (array of arrays)
# for i in range(size): # 4 times
#     matrix.append([]) # create new array in matrix
#
#     print(matrix)

# n = int(input('Введите размер таблицы: '))
# matrix = [[x for x in range(1 + i, n + i + 1)] for i in range(n)]
#
# print(matrix)

n = int(input('Введите размер таблицы: '))
matrix1 = [[x for x in range(1 + i, n + i + 1)] for i in range(n)]
print(matrix1)

matrix1 = []
for x in