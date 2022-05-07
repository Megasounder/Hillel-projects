# Написать декоратор,который печатает имя функции и аргументы которые в неё передали


def show_attributes(func):
    """
    :param func: function, that name was printed
    :return:the same functuion
    """
    name = func.__name__

    def wrapper(*args, **kwargs):
        print(f'\n>>>was called {name} with arguments  {*args, kwargs}')
        return func(*args, **kwargs)
    return wrapper


@show_attributes
def simple_function(a, b, c=5, d=3):
    return a + b * c + d


@show_attributes
def another_function(a, b, c, d=2):
    return a + b * c + d


another_function(4, 3, 4, d=3)

