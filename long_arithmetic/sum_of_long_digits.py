# coding: utf-8

# Условие:
# Найти сумму двух целых неотрицательных чисел A и B (A, B <= 10 ** 10000)
# 

# сложность: log max(A, B)
# 

import random


def my_algo(A, B):
    A, B = str(A), str(B)
    R = ''
    if len(A) > len(B):
        B = '0' * (len(A) - len(B)) + B
    if len(A) < len(B):
        A = '0' * (len(B) - len(A)) + A
    additional = 0
    for a, b in zip(A[::-1], B[::-1]):
        a, b = int(a), int(b)
        r = a + b + additional
        additional = r / 10
        r = r % 10
        R = str(r) + R
    if additional:
        R = str(additional) + R
    return R


def real(A, B):
    return A + B


examples = []
for i in range(10):
    A = random.randint(10 ** 5, 10 ** 10)
    B = random.randint(10 ** 5, 10 ** 10)
    examples.append((A, B))

for A, B in examples:
    print 'A:', A, 'B:', B
    r = real(A, B)
    my = my_algo(A, B)
    print 'my  ', my
    print 'real', r
    assert my == str(r), 'Error'
