# дано 2 отсортированных массива, слей в 1 отсортированный


# Сложность O(длина большего массива)


import random


def my_algo(array1, array2):
    result = []
    while array1 and array2:
        a1 = array1[0]
        a2 = array2[0]
        if a1 < a2:
            result.append(array1.pop(0))
        else:
            result.append(array2.pop(0))
    if array1:
        result += array1
    if array2:
        result += array2
    return result


def real(array1, array2):
    return sorted(array1 + array2)


examples = []
for i in range(3):
    array1 = sorted([random.randint(0, 1000) for i in range(10)])
    array2 = sorted([random.randint(0, 1000) for i in range(10)])
    examples.append((array1, array2))


for array1, array2 in examples:
    print 'array1:', array1, 'array2:', array2
    r = real(array1, array2)
    my = my_algo(array1, array2)
    print 'my merge:', my
    print 'real:    ', r
    assert my == r, 'error with {0} and {1}'.format(array1, array2)
