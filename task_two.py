# Есть три кортежа целых чисел. 
# Необходимо найти элементы, 
# которые уникальны для каждого списка.

from random import randint

def rand_tuple():
    '''Return random list with numbers'''
    list_tup = []
    step = 0
    tup_len = 5
    while step < tup_len:
        rand_num = randint(0, 10)
        list_tup.append(rand_num)
        step += 1
    return list_tup

def dif_number(t_one, t_two, t_three):
    '''Compare different elements in tuples'''
    list_dif = []
    for i in t_one + t_two + t_three:
        if not (i in t_one and i in t_two and i in t_three) and (i in t_one) ^ (i in t_two) ^ (i in t_three):
            list_dif.append(i)
    return list_dif

tuple_one = tuple(rand_tuple())
tuple_two = tuple(rand_tuple())
tuple_three = tuple(rand_tuple())

if len(dif_number(tuple_one, tuple_two, tuple_three)) == 0:
    print('In tuples:', '\n', tuple_one, '\n', tuple_two, '\n', tuple_three, '\n', 'no different elements')
else:
    print('In tuples:', '\n', tuple_one, '\n', tuple_two, '\n', tuple_three)
    print('Different elements is', *set(dif_number(tuple_one, tuple_two, tuple_three)))
