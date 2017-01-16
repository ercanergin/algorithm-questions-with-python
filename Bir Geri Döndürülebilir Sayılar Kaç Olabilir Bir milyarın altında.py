sayac=0
for n in range(1,10**9):
    if(n%10==0):
        continue
    reversen=n+int(str(n)[::-1])
    if(reversen%2==1):
        for m in ["0","2","4","6","8"]:
            if(list(str(reversen)).count(m)>0):
                break

        else:
            sayac+=1
print(sayac)
