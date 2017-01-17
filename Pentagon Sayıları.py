def P(n):
    return(int(n*(3*n-1)/2))

pentagons = []
for n in range(1,10000):
    pentagons.append(P(n))

for p in pentagons:
    for q in pentagons[(pentagons.index(p)+1):]:
        if(pentagons.count(p+q)==1):
            if(pentagons.count(q-p)==1):
                print(q-p)
