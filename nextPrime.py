'''
primes = next_prime()
[next(primes) for i in range(25)]
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
'''
def next_prime():
    n = 2
    while True:
        is_prime = True
        for x in range(2, n):
            if n % x == 0:
                is_prime = False
        if is_prime == True:
            yield n
        n += 1