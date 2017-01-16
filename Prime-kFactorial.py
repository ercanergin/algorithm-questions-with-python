from functions import allprimes

def s(p):
    return(((p-3)*pow(8,p-2,p))%p)

primes = allprimes(10**8)[2:]
cozum = 0

for p in primes:
    cozum += s(p)

print(cozum)
