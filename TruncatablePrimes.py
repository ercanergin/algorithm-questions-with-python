from functions import allprimes

primes=allprimes(750000)

rightprimes = []
for n in primes[4:]:
    temp = n
    n=list(str(n))
    for i in range(1,len(n)):
        n.pop()
        n=''.join(str(i) for i in n)
        if(primes.count(int(n))==0):
            break
        n=list(str(n))
    else:
        rightprimes.append(temp)

leftprimes =[]
for n in rightprimes:
    temp = n
    n=list(str(n))
    for i in range(1,len(n)):
        n.remove(n[0])
        n=''.join(str(i) for i in n)
        if(primes.count(int(n))==0):
            break
        n=list(str(n))
    else:
        leftprimes.append(temp)

print(sum(leftprimes))
