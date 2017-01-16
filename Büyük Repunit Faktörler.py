from sympy import primerange

primes = primerange(5,1000000)

bolen = []
L = 10**9

for n in primes:
    if(pow(10, L, n) == 1):
        bolen.append(n)
        if(len(bolen)==40):
            break
print(sum(bolen))
