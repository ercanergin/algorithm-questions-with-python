dizi = '0'
i = 1

while len(dizi)<1000005:
    dizi = dizi+str(i)
    i += 1
print(int(dizi[1])*int(dizi[10])*int(dizi[100])*int(dizi[1000])*
      int(dizi[10000])*int(dizi[100000])*int(dizi[1000000]))

