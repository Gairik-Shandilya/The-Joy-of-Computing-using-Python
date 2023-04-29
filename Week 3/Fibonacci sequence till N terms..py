n= int(input())
def fibb(n):
  if n==1:
    return 1
  elif n==0:
  	return 0
  else : 
    return fibb(n-1) + fibb(n-2)
for i in range(0,n,1):
  print(fibb(i))
