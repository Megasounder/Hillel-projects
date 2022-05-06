    # ДЗ 5. Математика
    # Добавлено: 25.04.2022 20:02
    # Сдать до 9 мая 00:00
  
# Контекстні менеджери, Декоратори, Класи

"""

Использовать тайп хинты

-Написать класс Калькулятор, содержащий метод add без реализации, который принимает 2 аргумента
-Написать классы, которые будут наследоваться от класса Калькулятор:
класс IntegerCalculator который реализует метод add (сумма двух чисел и вернуть результат int )
класс FloatCalculator который реализует метод add (cумма двух чисел и вернуть результат float)
-функцию make_add принимающую экземпляр класса IntegerCalculator или FloatCalculator
и выполняет метод виконує метод add. Функція make_add и: екземпляр класу та два числа.

в конце файла проверочный код

        
"""
    # Приклад функції без реалізації


 
    # Написати класи які будуть успадковуватися від класу Calculator :
    # Пошукайте як перевести число у відповідний тип



class Calculator:
    def __init__(self, a, b) -> None:
        self.a = 0
        self.b = 0
        
        
    def add(self, *args, **kwargs) -> None:
        pass


class IntegerCalculator(Calculator):
    def __init__(self) -> None:
            pass   

    def addissimo(self, a, b):
        a = self.a
        b = self.b
        return a + b

class FloatCalculator(Calculator):
    def __init__(self) -> None:
        pass    


def make_add(obj, a, b):
    res = obj.add(a,b)
    return res



int_calc = IntegerCalculator()
result = make_add(int_calc, 1.0, 2.0)
print(result) #результат має бути 3
    # float_calc = FloatCalculator ()
    # result = make_add(float_calc, 1, 2)
    # print(result) #результат має бути 3.0