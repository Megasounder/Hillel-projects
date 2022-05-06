def su():
    return a + b


def mu():
    return a * b

# su and mu - additional functions, which returns input parameters to experimental function

list = [1,2,3,4,6,8]
a = 3
b = 4


def my_map(func, l):
    '''
	 my_map - Experimental function-generator that works as function map()
            This function sums first input argument (func) with next element in list by new iteration
	 func - result or return of additional function (mu-ltiply or su-mming) 
	 l - list of integers
	'''

    c = func()
    for item in l:    
        yield item + c

g = my_map(mu, list)  # Generator object 

for i in list:
    print(next(g))

