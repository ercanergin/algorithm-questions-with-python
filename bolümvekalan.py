a=int(input("a degerini gir: "))
b=int(input("b degerini gir:"))

x=a
y=0
while True:
    if x<b:
        print(x,y)
        break
    else:
        x=x-b
        y=y+1
