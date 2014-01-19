import math

def main(A, B, M):

    result = 1

    def B_bits():
        bits_count = int(math.log(B, 2)) + 1
        for i in range(bits_count):
            yield B >> i & 1

    for index, bit in enumerate(B_bits()):
        A = A ** 2 % M if index != 0 else A % M
        if bit:
            result *= A

    return result % M


def real(A, B, M):
    return (A ** B) % M

from random import randint

for i in range(10):
    input = [randint(10, 10 ** 5), randint(10, 10 ** 5), randint(3, 100)]

    print 'input', input, 'my', main(*input), 'real', real(*input)
