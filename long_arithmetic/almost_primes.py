# coding: utf-8

# Условие:
# Натуральное число называется почти простым, если оно не простое и имеет 
# только один простой делитель. Найти количество почти простых чисел в 
# заданном интервале натуральных чисел(0 < low ≤ high ≤ 10 ** 12).
# 
# 
# Сложность: 


def isqrt(n):
    x = n
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def eratosfen(N):
    array = [True] * N
    array[0] = array[1] = False
    for i in range(2, len(array) - 1):
        if array[i]:
            if (i * 2 <= N):
                for j in range(i**2, N, i):
                    array[j] = False
    return [index for index, value in enumerate(array) if value]


def my_algo(array):
    highest = max([a[1] for a in array])
    primes = eratosfen(isqrt(highest))
    all_results = []
    for prime in primes:
        result = prime ** 2
        while result <= highest:
            all_results.append(result)
            result *= prime
    print len(all_results)
    for low, high in array:
        print 'between {} and {}:'.format(low, high),
        for result in all_results:
            if low <= result <= high:
                print result,
        print


example = [(10, 1000), (200, 10 ** 5), (5, 100), (10 ** 3, 10 ** 12)]

print 'example', example
my_algo(example)




