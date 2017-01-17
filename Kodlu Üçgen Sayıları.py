dosya=open("p042_words.txt")
for line in dosya.readlines():
        words = line.rstrip('\n').split('","')

sonuc = 0
triangle = []
alfabe=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for n in range(1,20):
    triangle.append(n*(n+1))
for p in words:
    toplam = 0
    for i in p:
        toplam += alfabe.index(i)+1
    if(triangle.count(toplam*2)==1):
        sonuc += 1
print(sonuc)
