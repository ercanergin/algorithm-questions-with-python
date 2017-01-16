from functions import allprimes

LIMIT = 10**8
primes = allprimes(LIMIT)

def kontrol(n):
    if n%4==0 : return 0
    r=int(n**0.5)+1
    for i in range(1,r+1):
        if(n%i==0):
            if i+n/i not in s:
                return 0
    return 1

s=set(primes)
toplam=sum(p-1 for p in primes if kontrol(p-1))

print(toplam)
