from main import Human
import json
from pprint import pprint


def object_from_list_of_dicts(data) -> list:
    '''
    Function create class object from json string
    :param data: list of dictionaries
    :return: list of objects class Human
    '''
    li = []
    for i in data:
        person = Human(**i)
        li.append(person)
    return li


def read_file() -> list:
    with open('humans.json') as f:
        result = (json.load(f))
    return result


data = read_file()
pprint(object_from_list_of_dicts(data))   #uses magic method __str__()