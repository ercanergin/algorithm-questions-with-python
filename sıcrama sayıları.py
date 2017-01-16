def comparison(i):
    increasing, decreasing="FALSE", "FALSE"
    for j in range(len(str(i))-1):
        if int(str(i)[j])>int(str(i)[j+1]):
            decreasing="TRUE"
        elif int(str(i)[j])==int(str(i)[j+1]):
            pass
        else:
            increasing="TRUE"
    if increasing=="TRUE" and decreasing=="TRUE":
        return 1
    else:
        return 0

bouncy,x=0,100
while (bouncy/x)<0.99:
    if(comparison(x)==1):
        bouncy +=1
    x +=1
print(x)
