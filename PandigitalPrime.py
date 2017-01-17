from functions import allprimes
from functions import ispandigital

primes=allprimes(10000000)[::-1]

for n in primes:
    if(ispandigital(n)==1):
        print(n)
        break
