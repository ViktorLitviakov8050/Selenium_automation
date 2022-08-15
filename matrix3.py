size = 40

array = []
# for i in range(1, size + 1):
#     if not i % 3 == 0:
#         array.append(i ** i)
# print(array)



for i in range(1, size + 1):
    if i % 2 ==0 and (i**2) % 4== 0:
        array.append(i)
print(array)
