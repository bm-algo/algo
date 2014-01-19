# coding: utf-8

# # Найти медиану

#    Медиана играет важную роль в мире статистики. По определению это число,
#    которое делит массив на две равные части. В этой задаче Вам необходимо 
#    найти значение медианы для текущего набора целых чисел. 
#    Например, рассмотрим последовательность {1, 3, 6, 2, 7}. Число 3 является 
#    медианой, так как по обе стороны от него находится в точности по два целых 
#    числа: {1, 2} и {6, 7}. 

#    Если последовательность содержит четное количество чисел, как например 
#    {1, 3, 6, 2, 7, 8}, то одно число не может разбить массив на две равные 
#    части, поэтому в качестве медианы будем рассматривать среднее 
#    арифметическое центральных чисел {3, 6}. То есть медиана равна 
#    (3 + 6) / 2 = 4.5. В задаче Вам следует выводить только целую часть медианы,
#    без дробной. То есть для данного примера ответом будет 4.


# Технические условия

#    Входные данные

#    Состоит из набора целых чисел x ( 0 ≤ x < 231), их количество не более 30000.

#    Выходные данные

#    Для каждого входного числа в отдельной строке вывести медиану текущей последовательности. 
#    Для каждого значения медианы выводить только ее целую часть.


# Сложность O(N)

import random
import copy

def partition(array, l, e, g):
    while array != []:
        head = array.pop(0)
        if head < e[0]:
            l = [head] + l
        elif head > e[0]:
            g = [head] + g
        else:
            e = [head] + e
    return (l, e, g)


def element_by_index(array, index, l_count=0):
    chosen_index = random.randint(0, len(array)-1)
    chosen = array.pop(chosen_index)
    l, e, g = partition(array, [], [chosen], [])
    if l_count + len(l) > index:
        return element_by_index(l, index, l_count)
    else:
        if l_count + len(l) + len(e) > index:
            return e[0]
        else:
            return element_by_index(g, index, l_count + len(l) + len(e))


def my_algo(array):
    if len(array) % 2:
        return element_by_index(array, (len(array) - 1) / 2)
    else:
        c = copy.deepcopy(array)
        first = element_by_index(array, (len(array) - 2) / 2)
        second = element_by_index(c, len(c) / 2)
        return (second + first) / 2


def real(array):
    ''' Just for tests '''
    sarray = sorted(array);
    if len(sarray) % 2:
        return sarray[len(sarray) / 2]
    else:
        return (sarray[len(sarray) / 2] + sarray[len(sarray) / 2 - 1]) / 2

examples = []
for i in range(10):
    examples.append([random.randint(1, 100) for k in range(5 + i)])

for example in examples:
    print 'example:', example
    r = real(example)
    my = my_algo(example)
    print 'real:', r, 'my:', my
    assert r == my, 'Error!'
