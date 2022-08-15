
a = [1, 3, 4, 5, 7, 8,9]

b = [ x for x in a if x % 2 == 0]

c = lambda a: [ x for x in a if x % 2 == 0]

def even_numbers(a):
    return [ x for x in a if x % 2 == 0]

print(even_numbers(a))


print(b)

print(c(a))


d = (x for x in a if x % 2 == 0)

print(next(d))
print(next(d))
print(type(d))

print(next(d))