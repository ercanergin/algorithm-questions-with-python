from itertools import permutations

sayilar = list(permutations([0,1,2,3,4,5,6,7,8,9], 10))
print(int(''.join(map(str,sayilar[999999]))))
