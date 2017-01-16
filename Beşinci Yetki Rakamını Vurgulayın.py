toplam=0
for i in range(1000,354294):
    control=0
    for j in str(i):
        control +=int(j)**5
    if i==control:
        toplam +=control
print(toplam)
