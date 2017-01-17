sonuc=0
for p in range(1,10):
    for q in range(1,22):
        if(len(str(p**q))==q):
            sonuc+=1
print(sonuc)
