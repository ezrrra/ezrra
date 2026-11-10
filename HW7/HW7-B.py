
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


L, R = map(int, input().split())

primes = []

for num in range(L, R + 1):
    if is_prime(num):
        primes.append(num)

if len(primes) == 0:
    print("NONE")
else:
    print(*primes)

print(len(primes), sum(primes))
