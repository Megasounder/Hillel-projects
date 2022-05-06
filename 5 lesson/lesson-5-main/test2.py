from test import add, create_list

def make_some_of_two_lists(items=10):
    list_1 = create_list(items)
    list_2 = create_list(items)
    list_3 = []
    for i in range(items):
        list_3.append(add(list_1[i], list_2[i]))
    return list_3

if __name__ == '__main__':
    print(make_some_of_two_lists(5))