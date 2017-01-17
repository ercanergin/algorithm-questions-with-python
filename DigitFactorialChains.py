from math import factorial

def factop(n):
    toplam = 0
    for i in str(n):
        toplam += factorial(int(i))
    return(toplam)
sonuc=0
for n in range(3,1000000):
    norg = n
    liste=[n]
    while(liste.count(factop(norg))!=1):
        faktoriyel=factop(norg)
        liste.append(faktoriyel)
        norg=faktoriyel
    if(len(liste)==60):
        sonuc += 1
print(sonuc)
