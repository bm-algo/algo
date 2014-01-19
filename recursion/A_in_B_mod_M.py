import datetime
from random import randint
from optparse import OptionParser
from numb import eulerphi


def rec_func(C, A, B, M):
    A = A % M
    k = 2
    while k <= B:
        if A ** k < M:
            k += 1
        else:
            C, A, B, M = rec_func(C * (A ** (B % k)), (A ** k) % M, B / k, M)
    return C, A, B, M


def main_func(A, B, M):
    C, A, B, M = rec_func(1, A, B, M)
    return (C * A ** B) % M


def real(A, B, M):
    return (A ** B) % M


if __name__ == '__main__':
    parser = OptionParser()
    (options, args) = parser.parse_args()
    if args:
        time = datetime.datetime.now()
        print 'result', main_func(*[int(a) for a in args])
        print 'time', datetime.datetime.now()-time
    else:
        print 'Testing'
        for i in range(10):
            args = [randint(10 ** 3, 10 ** 5), randint(10 ** 4, 10 ** 5), randint(200, 2000)]
            print 'A =', args[0], 'B =', args[1], 'C =', args[2]
            print 'my result', main_func(*args)
            print 'real', real(*args)
