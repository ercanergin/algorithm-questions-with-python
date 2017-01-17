def samedigits(n,p):
    for i in str(n*p):
        if(list(str(n)).count(i)==0):
            return(0)
            break
    else:
        return(1)

for n in range(1,1000000):
    same = 0
    for p in range(2,7):
        if(samedigits(n,p)==1):
            same += 1
    if(same==5):
        print(n)
        break
