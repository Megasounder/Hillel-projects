
def my_range(start, stop, step=1):
    '''
    Range generator that rerurns next value at next call
    start - first range element
    stop - last range element  

    function works only in increasing mode
    '''
    while start < stop:
        yield start
        start += step
            
x = my_range(2, 9)

try:
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
except StopIteration:
    print('____end of iteration___')


for i in range(2, 9, 1): # above simulate this simple function 
    print(i)
