from functools import wraps
from datetime import datetime

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__}')
        return func(*args, **kwargs)
    return wrapper

@decorator
def gd(a, b):
    return a + b


def logger_custom(logname: str):
    def logger(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with open(logname, 'a') as f:
                f.write(f'called function {func.__name__} in {datetime.now()}\n')
            return func(*args, **kwargs)
        return wrapper
    return  logger       


@logger_custom('test2.txt')
def div(a,b):
    return a/b 

div(5,7)