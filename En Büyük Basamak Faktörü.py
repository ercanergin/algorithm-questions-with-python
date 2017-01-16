#600851475143 numaralı telefonun en önemli faktörü nedir?
from functions import allprimes

primes=allprimes(10000)
number,i=600851475143,1
while not (number%primes[-i]==0):
    i +=1
print(primes[-i])
