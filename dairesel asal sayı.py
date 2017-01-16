from functions import isprime

sonuc = 13
for n in range(101,1000000,2):
    if(isprime(n)==0):
        continue
    for p in range(len(str(n))):
        if(isprime(int(n))==0):
            break
        n=list(str(n))
        n.append(n[0])
        n.remove(n[0])
        n=''.join(str(i) for i in n)
    else:
        sonuc +=1
print(sonuc)
