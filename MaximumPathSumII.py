dosya=open("p067_triangle.txt")
triangle = []

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    triangle.append(line)

for n in range(len(triangle)-2,-1,-1):
    for m in range(len(triangle[n])):
        triangle[n][m] = int(triangle[n][m]) +  max(int(triangle[n+1][m]),int(triangle[n+1][m+1]))

print(triangle[0][0])
