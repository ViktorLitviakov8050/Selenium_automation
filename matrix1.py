# n = int(input('Введите размер таблицы: '))
# for row in range(1, n + 1):
#     for col in range(1, n + 1):
#         if row % 2 == 0:
#             print(row, end='\t')
#         else:
#             print(col, end='\t')
#     print()
#

size = int(input('Введите размер таблицы: '))
# for i in range(size): # 0 1 2 3 -> 4 iterations
#     for j in range(1, size+1): # 1 2 3 4 -> 4 iterations
#         print(i+j, end='-') # i is like an offset
#     print()

from pprint import pprint
matrix = [] # empty matrix (array of arrays)
for i in range(size): # 4 times
    matrix.append([]) # create new array in matrix
    for j in range(1, size + 1): # 4 times from 1 to 4
        if (i+j) % 2 == 0:
            matrix[i].append((i+j)**2) # append to row i+j
        else:
            matrix[i].append(i + j)
print("[")

for row in matrix:
    print(row)
print(']')
    # for element in row:
        # print(element, end=' ')
        # print(matrix)
