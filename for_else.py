
# for i in range(10):
#     print(i)
#     if i == 3:
#         break
# else:
#     print("Hello Python")

_list = [1, 3 ,4 , 6, 7, 8, 10]

a = _list[::]

_set = frozenset(range(1000000))
print(_list[::])
print(id(a))
print(id(_list))
print(a is _list)
a[0] = 5
print(a)
print((_list))

_int = 1000
_intF = 10.003
_str = 'asdflkjadfl;'

print(type(_int))
print(type(_intF))
print(type(_str))

#if else
#elif

#in or not and is - #logic operator


a = 2 if 'y' in 'python' else 4  # ternary operator


print(a)

abc = {"v": 23, "asd": 33, True: "adf"}
print(abc.items())

