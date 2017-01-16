def ispalindrome(n):
        if(str(n)==str(n)[::-1]):
            return(1)
        else:
            return(0)

sonuc = 0
for n in range(1,1000000):
    if(ispalindrome(n)==1 and ispalindrome(int(bin(n)[2:]))==1):
        sonuc += n
print(sonuc)
