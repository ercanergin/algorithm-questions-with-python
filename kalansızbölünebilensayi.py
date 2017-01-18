deger=0
for j in range(1,100000000):
    for i in range(1,21):
        if j%i==0:
            deger+=1
        else:
            break

    if deger==20:
        print (int(j))
        break
    else:
        deger=0
