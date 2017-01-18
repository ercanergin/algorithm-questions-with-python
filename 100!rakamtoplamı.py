def bas_deg_topla(sayi):
    deger=0
    while sayi:
        basamak=sayi%10
        sayi=sayi/10
        deger+=basamak
    print (int(deger))

m=int(input("faktoriyeli alanacak sayi: "))

fak=1
for i in range(1,m+1):
    fak=fak*i
print (fak)
bas_deg_topla(fak)
