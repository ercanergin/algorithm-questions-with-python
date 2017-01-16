def digitsum(n):
    return (sum(map(int,str(n))))

cozum=[]
for n in range(2,100):
    for m in range(2,10):
        p=n**m
        if(n==digitsum(p)):
            cozum.append(p)

cozum.sort()
print(cozum[29])
