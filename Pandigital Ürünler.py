from functions import ispandigital

carpimlar=[]
for a in range(1,500):
    for b in range(1,2000):
        q=''.join([str(a),str(b),str(a*b)])
        if(len(str(q))==9 and ispandigital(q)==1):
            carpimlar.append(a*b)
carpimlar.sort()

for n in carpimlar:
    while not (carpimlar.count(n)==1):
        carpimlar.remove(n)
print(sum(carpimlar))
