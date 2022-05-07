def sqr(a):  # additional function
    return a ** 2


def my_map(func, l):
    """
my_map - Experimental function-generator that works as function map()
This function takes iterable element and send it to additional function(func) as input argument, and yielding result.
func - additional function
l - list of integers
    """
    for item in l:
        yield func(item)


l = [1, 2, 3, 4, 6, 8]  # list of elements

c = my_map(sqr, l)

print(next(c))
print(next(c))
print(next(c))
print(next(c))

# for i in my_map(sqr, l):
#   print(i)
