enfazla=3
for p in range(120,1001):
    cozumsayisi=0
    for a in range(20,401):
        for b in range(40,401):
            c=p-a-b
            if(c>0 or c>(a+b)):
                continue
            if(c>0 and a**2+b**2==c**2):
                cozumsayisi+=1
            if(cozumsayisi<enfazla):
                enfazla=cozumsayisi
                pmax=p
print(pmax)
