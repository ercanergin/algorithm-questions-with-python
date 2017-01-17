from math import sqrt
from decimal import *

getcontext().prec = 110
toplam = 0
for m in range(2,100):
    if(int(sqrt(m))**2!=m):
        toplam += int(str(Decimal(m).sqrt()).split(".")[0])
        n = str(Decimal(m).sqrt()).split(".")[1][:99]
        for i in n:
            toplam += int(i)
print(toplam)
