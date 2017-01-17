from math import log10

dosya=open("p099_base_exp.txt")

enbuyuk = 0
satir = 1

for line in dosya.readlines():
    [a, b] = line.rsplit(',')
    sayi = int(b)*log10(int(a))

    if(sayi>enbuyuk):
        enbuyuk = sayi
        sonuc = satir

    satir += 1
print(sonuc)
