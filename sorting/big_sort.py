# Большая сортировка

#    Отсортируйте N заданных чисел в неубывающем порядке.


#    Входные данные

#    Дано число N (1 ≤ N ≤ 100000), а затем в одной или нескольких строках N 
#    натуральных чисел из диапазона от 1 до 100.


#    Выходные данные

#    Выведите в одной строке N чисел в неубывающем порядке.
#    
#    
#    
#    Сложность алгоритма: O(N)

import random


def my_algo(array):
    count_array = [0]*100
    for a in array:
        count_array[a] += 1
    result = []
    for index, el in enumerate(count_array):
        result += [index]*el
    return result

def real(array):
    return sorted(array)


examples = []
for i in range(3):
    examples.append([random.randint(1, 99) for k in range(20)])


for example in examples:
    my = my_algo(example)
    r = real(example)
    print 'example', example
    print 'sorted by my algo:', my
    print 'sorted by default sort:', r
    assert my == r,'error with example {0}'.format(example)