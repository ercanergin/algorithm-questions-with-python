from math import factorial

def nCr(n,r):
    return(factorial(n)/(factorial(r)*factorial(n-r)))

sonuc = 7*(1-(nCr(60,20)/nCr(70,20)))

print(sonuc)
