from itertools import count
import os
import sqlite3

from typing import Dict, List, Set


def execute_query(query_sql: str) -> List:
    '''
    Функция для выполнения запроса
    :param query_sql: запрос
    :return: результат выполнения запроса
    '''
    db_pass = os.path.join(os.getcwd(),'chinook.db')
    connection = sqlite3.connect(db_pass)
    cur = connection.cursor()
    result = cur.execute(query_sql)
    return result


def get_overall_profit() -> float:
    '''
    Выдаёт общую сумму дохода из кол-ва единиц в таблице invoice_items
    :return: Произведение всех элементов UnitPrice на Quantity
    '''
    query_sql = f'''
        SELECT UnitPrice * Quantity 
          FROM invoice_items
    '''
    records = execute_query(query_sql)
    list = []
    for record in records:
        list.append(record[0])
    profit = sum(list)
    
    return profit

print(get_overall_profit())


def get_names_list() -> List:
    '''
    Функция для получения списка всех значений FirstName из таблицы customers
    :return: список имён
    '''
    query_sql = f'''
        SELECT FirstName 
        FROM customers   
    '''
    records = execute_query(query_sql)
    result = []
    for record in records:
        result.append(record[0])
    return result


def get_duplicates_from_list() -> Dict:
    '''
    Функция для нахождения повторяющихся значений из списка
    :List: Запрос на получение списка
    :return: {'имя_повторяющегося_элемента': число_повторов}
    '''
    List = get_names_list()
    counter = {}
    for element in List:
        counter[element] = counter.get(element, 0) + 1
    duplicates = {element: count for element, count in counter.items() if count > 1} 
    return duplicates


print(get_duplicates_from_list())