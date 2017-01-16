from gmpy import is_square

def solve(a,b,c,d,e,f):
    x = (a+b)/2
    y = (e+f)/2
    z = (c-d)/2
    if(x>y and y>z and z>0 and x==int(x) and y==int(y) and z==int(z)):
        return(int(x+y+z))
    else:
        return(0)

for a in range(2,1000):
    a2 = a**2
    for c in range(2,1000):
        c2 = c**2
        for d in range(2,1000):
            d2 = d**2
            f2 = a2-c2
            if(f2>0 and is_square(f2)):
                e2 = a2-d2
                if(e2>0 and is_square(e2)):
                    b2 = c2-e2
                    if(b2>0 and is_square(b2)):
                        if(solve(a2,b2,c2,d2,e2,f2)!=0):
                            print(solve(a2,b2,c2,d2,e2,f2))
                            break
