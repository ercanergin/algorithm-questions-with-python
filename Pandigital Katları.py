from functions import ispandigital

largest = 1
for p in range(1,10000):
    n=''
    q=1
    while(len(n)<9):
        n=n+''.join(str(p*q))
        q += 1
    if(len(n)==9 and ispandigital(int(n))==1):
        largest=max(largest,int(n))
print(largest)
