toplam,n=1,1
while n<1001*1001:
    for p in range(2,1001,2):
        for m in range(1,5):
            n+=p
            if(n>1001*1001):
                break
            toplam+=n
print(toplam)
