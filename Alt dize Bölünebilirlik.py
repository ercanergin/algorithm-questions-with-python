from itertools import permutations

sonuc = 0
sayilar = list(permutations([1,2,3,4,5,6,7,8,9,0], 10))
for n in range(len(sayilar)):
    q = int(''.join(map(str,sayilar[n])))
    if(int(str(q)[1:4])%2==0 and int(str(q)[2:5])%3==0 and int(str(q)[3:6])%5==0 and int(str(q)[4:7])%7==0 and int(str(q)[5:8])%11==0 and int(str(q)[6:9])%13==0 and int(str(q)[7:10])%17==0):
        sonuc += q
        print(q)
print(sonuc)
