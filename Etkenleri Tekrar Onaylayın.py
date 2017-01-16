from sympy import primerange

primes = primerange(2,100000)

bolen = 3
L = 10**20

for n in primes:
    if(pow(10, L, n) != 1):
        bolen += n
print(bolen)
