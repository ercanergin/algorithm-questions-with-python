powers=[]
for a in range(2,101):
    for b in range(2,101):
        powers.append(a**b)

powers.sort()

for n in powers:
    while powers.count(n)>1:
        powers.remove(n)

print(len(powers))
