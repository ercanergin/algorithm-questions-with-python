from sympy import divisor_count

c = 1
for n in range(2,10**7):
    m=divisor_count(n)
    if(m==2):
        continue
    if(m==divisor_count(n+1)):
        c += 1
print(c)
