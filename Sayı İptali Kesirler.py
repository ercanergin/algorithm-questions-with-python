sonuc=1
for a in range(11,100):
    if(a%10!=0):
        for n in range(1,10):
            c=a%10*10+n
            if(c%11!=0):
                if(a/c==int(a/10)/n):
                    sonuc*=c/a
print(int(sonuc))
