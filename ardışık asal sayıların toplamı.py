from functions import isprime
maks=1
primes=[]
for i in range(2,1000000):
    if isprime(i)==1:
        primes.append(i)
for p in range(100,600):
    for i in range(len(primes)-p-1):
        sums = 0
        for j in range(p):
            sums += primes[i+j]
        if (i==1) and sums>primes[-1]:
            break
        if(primes.count(sums)==1):
            maks=sums
print(maks)
