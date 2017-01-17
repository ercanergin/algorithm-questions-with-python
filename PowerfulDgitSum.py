sonuc=1
for a in range(2,100):
    for b in range(2,100):
        c=a**b
        toplam=0
        for i in str(c):
            toplam+=int(i)
        if(toplam>sonuc):
            sonuc=toplam
print(sonuc)
