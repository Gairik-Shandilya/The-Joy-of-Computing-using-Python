n = int(input()) 
L = list(map(int, input().split()))
fav=L[int(input())-1]
newarr=sorted(L)
pos=(newarr.index(fav)+1)
print(pos)
