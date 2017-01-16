from functions import divisors
toplam=0
for i in range(220,10000):
    if(i!=sum(divisors(i)) and i==sum(divisors(sum(divisors(i))))):
        toplam += i
print(toplam)
