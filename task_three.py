# Есть три кортежа целых чисел. 
# Необходимо найти элементы, 
#  1. которые есть в каждом из кортежей и 
#  2. находятся в каждом из кортежей на той же позиции.

from random import randint

def rand_tuple():
    '''Return random list with numbers'''
    list_tup = []
    step = 0
    tup_len = 10
    while step < tup_len:
        rand_num = randint(0, 2)
        list_tup.append(rand_num)
        step += 1
    return list_tup

def same_elem(t_one, t_two, t_three):
    '''Compare same elements in tuples'''
    elem = 0
    tup_len = 10
    list_elem = []
    while elem < tup_len:
        if t_one[elem] == t_two[elem] == t_three[elem]:
            list_elem.append(t_one[elem])
        elem += 1
    return list_elem

tuple_one = tuple(rand_tuple())
tuple_two = tuple(rand_tuple())
tuple_three = tuple(rand_tuple())
element = same_elem(tuple_one, tuple_two, tuple_three)

if len(element) != 0:
    print('In tuples:', '\n', tuple_one, '\n', tuple_two, '\n', tuple_three)
    print('Same elem is', *element)
else:
    print('In tuples:', '\n', tuple_one, '\n', tuple_two, '\n', tuple_three)
    print('No same elemets')
