# coding: utf-8

# Условие
# 
# НОК (наименьшее общее кратное) множества целых чисел определяется как 
# наименьшее число, которое делится на каждое число из этого множества. 
# Интересно заметить, что любое натуральное число может быть выражено 
# как НОК некоторого множества натуральных чисел. Например, 12 можно 
# представить как НОК чисел 1, 12, или 12, 12, или 3, 4, или 4, 6, или 
# 1, 2, 3, 4 и так далее.
# 
# 
#    В задаче задано натуральное число n. Необходимо найти множество, 
#    содержащее как минимум два числа, НОК чисел которого равно n. 
#    Поскольку таких множеств может быть бесконечное количество, 
#    Вам следует найти такое, для которого сумма его элементов минимальна. 
#    Мы будем предельно счастливы, если Вы также напечатаете и указанную сумму. 
#    Например, для n = 12 необходимо вывести 4 + 3 = 7, так как НОК чисел 4 и 3 
#    равно 12, а 7 - наименьшее возможное значение суммы чисел множества.


# Сложность: 

from fractions import gcd

def isqrt(n):
    x = n
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def lcm(a, b):
    return (a * b) / gcd(a, b)


def my_algo(N, is_first=0):
    i = isqrt(N)
    while i > 1:
        if N % i == 0 and lcm(i, N / i) == N:
            return my_algo(i) + my_algo(N / i)
        i -= 1
    return N + is_first


examples = [105, 24, 48, 300, 17]

for example in examples:
    print 'example:', example,
    print 'result:', my_algo(example, 1)

