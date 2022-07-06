from pprint import pprint
from main import Human
import json


def list_to_json(list_of_objects) -> None:
    with open('humans.json', 'w') as f:
        json.dump(list_of_objects, f, indent=2)
    return print('write json successful')


def list_from_objects(*args) -> list:
    """
    Function recive objects, and collect them to list of dictionaries
    :param args: objects of class Human
    :return:list of dicts
    """
    list_of_elements = []
    for arg in args:
        list_of_elements.append(arg.__dict__)
    return list_of_elements


person2 = Human('Eva', 'female', '25', 'Spain')
person = Human('Nick', 'male', '30', 'England')
person3 = Human('Max', 'male', '28', 'Italy')
person4 = Human('Mike', 'male', '26', 'France')


main_list = list_from_objects(person, person2, person3, person4)
pprint(main_list)
list_to_json(main_list)
pprint(main_list)


