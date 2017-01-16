bolmeyensayisi,n=0,3
while bolmeyensayisi<124:
    t1,t2,t3=1,1,3
    while t3>0 and (t1,t2,t3)!=(1,1,1):
        t1,t2,t3=t2,t3,(t1+t2+t3)%n
    if t3>0:
        bolmeyensayisi+=1
    n+=2
print(n-2)
