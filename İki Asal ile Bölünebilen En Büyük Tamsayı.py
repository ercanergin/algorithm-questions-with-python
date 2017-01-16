from functions import allprimes

LIMIT = 10**7
primes = allprimes(LIMIT)
sonuc = 0

for i in range(1, len(primes)):
    p = primes[i]
    for j in range(i):
        q = primes[j]
        l = int(LIMIT/q)
        if l < p:
            break
        r = p
        liste = []
        while r <= l:
            s = r*q
            while(s <= LIMIT):
                s *= q
            liste += [int(s/q)]
            r *= p
        sonuc += max(liste)

print(sonuc)
