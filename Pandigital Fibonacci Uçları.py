a, b, n = 1, 1, 2
rakamlar = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

while n<329000:
    a, b, n = b, a+b, n+1

while not (sorted(str(b)[:9])==rakamlar and sorted(str(b)[-9:])==rakamlar):
    a, b, n = b, a+b, n+1
print(n)
