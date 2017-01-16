oplam=set()
for n in range(1,10001):
    karetoplami=n**2
    for m in range(n+1,10001):
        karetoplami+=m**2
        if(karetoplami>10**8):
            break
        if(str(karetoplami)==str(karetoplami)[::-1]):
            toplam.add(karetoplami)
print(sum(oplam))
