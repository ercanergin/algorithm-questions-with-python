from sympy import primerange

LIMIT = 50000000
primes = list(primerange(2,int(LIMIT**0.5)))
sonuc = set()

for a in primes:
    for b in primes:
        for c in primes:
            if(a**2+b**3+c**4<LIMIT):
                sonuc.add(a**2+b**3+c**4)
            else:
                break
print(len(sonuc))
