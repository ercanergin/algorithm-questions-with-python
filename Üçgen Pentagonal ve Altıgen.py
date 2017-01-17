def T(n):
    return(n*(n+1)/2)

def P(n):
    return(n*(3*n-1)/2)

def H(n):
    return(n*(2*n-1))
triangle=[]
pentagonal=[]
hexagonal=[]
for i in range(144,60000):
    triangle.append(T(i))
    pentagonal.append(P(i))
    hexagonal.append(H(i))
for i in hexagonal:
    if (pentagonal.count(i)==1 and triangle.count(i)==1):
        print(i)
        break
