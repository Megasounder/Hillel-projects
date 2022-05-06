from typing import List

list_1 = [1, 2, 3, 4]
sum_list_1 = 0
# Non pythonic
for i in list_1:
    sum_list_1 += i

# pythonic
sum_list_1 = sum(list_1)

list_2 = [-1, 2, -5, 3, 5, 0]
filtered_list_2 = []

# Non pythonic
for i in list_2:
    if i >=0:
        filtered_list_2.append(i)

# Very non pythonic
filtered_list_2 = sorted(list_2)
index = filtered_list_2.index(0)
filtered_list_2 = filtered_list_2[index:]
def filter_negative(item: int):
    """This function returns true if item is positive"""
    return item > 0
# Pythonic Comprehantion
filtered_list_2 = [i for i in list_2 if filter_negative(i)]
print(filtered_list_2)
# Pythonic filter

filtered_list_2 = list(filter(filter_negative, list_2))
print(filtered_list_2)

for item in filter(filter_negative, list_2):
    print(item)

for i in list_2:
    print(f'Initital: {i}')
    if filter_negative(i):
        print(f'Filtered: {i}')

filtered_list_2 = filter(lambda i: i > 0, list_2)
print(filtered_list_2)
filtered_list_2 = list(filter(lambda i: i > 0, list_2))
print(filtered_list_2)

# Non pythonic. Shown as an example. DON'T do it.
is_item_positive = lambda i: i > 0
filtered_list_2 = list(filter(is_item_positive, list_2))
print(filtered_list_2)




def sqr(list_of_int: List[int]):
    for item in list_of_int:
        yield item ** 2


for sqr_item in sqr([1, 2, 3, 4]):
    print(sqr_item)


sqr_geneartor = sqr([1, 2, 3, 4])
print(sqr_geneartor)
print(next(sqr_geneartor))
print(next(sqr_geneartor))
print(next(sqr_geneartor))
print(next(sqr_geneartor))

f = iter([1, 2, 3, 4])
try:
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
except StopIteration as e:
    print(e)

list_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_3 = list(range(1, 11))
print(list_3[:5])
print(list_3[1:5])
print(list_3[5:])
print(list_3[-1])
print(list_3[-5:])
print(list_3[:-5])
print(list_3[1:101])
print(list_3[100:101])
print(list_3[1::2])
print(list_3[:])
print(list_3[::-1])
print(list(reversed(list_3)))

a = [1,2,3,4]
b = a
b.append(5)
print(b)
print(a)
print(id(a))
print(id(b))
print('Equal:')
print(a == b)
print(a is b)

a = [1,2,3,4]
b = a[:]
c = list(b)
b.append(5)
c.append(5)
print(c)
print(b)
print(a)
print(id(a))
print(id(b))
print(id(c))
print('b == c')
print(b == c)
print('b is c')
print(b is c)

if (1 == 1) is True: # => True is True => True
    print('1 does equal 1')

if 1 == 1 and 2 == 2:
    print('1 does equal 1')

print(1 == 1)
print(1 == 1 and 2 == 2)
print(1 and 2)
print(0 and 2)
print(1 and 0)
print(bool(1 and 0))
print(bool(0))
print(bool([]))
print(bool({}))
print(bool(None))
print(bool(False))
if 2 and 4: # bool(2 and 4) => True
    print('ok')

if not (1 == 2):
    print("Not Ok. And it's ok")
print(not [])
print(not None)
print(bool(None))
g = None
if g is None:
    print('g is None')

some_object = [1, 2]
if some_object is not None:
    print('Not a None')


if some_object: # => bool([1,2]) => True
    print('if some_object')

if some_object is True: # [1,2] is True
    print('if some_object is True')


class Iterator:
    def __init__(self, items):
        self.items = items
        self.index = 0

    def __next__(self):
        item = self.items[self.index]
        self.index += 1
        return item

iter = Iterator([1, 2, 3, 4])
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))

class Number:
    def __init__(self, a):
        self.a = a
    def __add__(self, other):
        return Number(self.a + other.a)
    def __str__(self):
        return f'Number: {self.a}'

a = Number(1)
b = Number(2)
c = a + b
print(c)

def sqr_2(item):
    return item ** 2

for sqr_item in map(sqr_2, [1,2,3,4,5]):
    print(sqr_item)

for sqr_item in map(lambda i: -i, [1,2,3,4,5]):
    print(sqr_item)

print(', '.join(['a', 'b', 'c']))
print(', '.join(map(str, [1,2,3])))
print(list(map(lambda i: i % 2, [1,2,3,4,5,6])))

a,b,c,d = 1,2,3,4

