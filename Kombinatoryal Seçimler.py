from sympy import binomial
sayi = 0
for n in range(1,101):
    for r in range(1,101):
        if binomial(n,r)>1000000:
            sayi += 1
print(sayi)
