m=int(input("sayi girin:"))

toplam=0
ucgen_sayi=0

for i in range(m+1):
    toplam+=i
    if toplam==m:
        print (m,"sayisi ucgen sayidir.")
        ucgen_sayi=1
if ucgen_sayi==0:
    print (m,"ucgen sayi degildir.")
