# Есть три кортежа целых чисел.
# Необходимо найти элементы, 
# которые есть во всех кортежах.

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

def same_number(t_one, t_two, t_three):
    '''Compare same elements in tuples'''
    same_elem = []
    for i in t_one + t_two + t_three:
        if not i in same_elem:
            if i in t_one and i in t_two and i in t_three:
                same_elem.append(i)
    return same_elem

tuple_one = tuple(rand_tuple())
tuple_two = tuple(rand_tuple())
tuple_three = tuple(rand_tuple())

if len(same_number(tuple_one, tuple_two, tuple_three)) == 0:
    print('In tuples:', '\n', tuple_one, '\n', tuple_two, '\n', tuple_three, '\n', 'no same elements')
else:
    print('In tuples:', '\n', tuple_one, '\n', tuple_two, '\n', tuple_three)
    print('The same is', *same_number(tuple_one, tuple_two, tuple_three))
