#Take an integer N as an input, print all the indexes of numbers in that integer from left to right

n=int(input())
idp=dict()
for i in str(n):
  idp[i]=[]
  for j in range(len(str(n))):
    if i==str(n)[j]:
      idp[i]+=[j] 
for k in idp:
    print(k,*idp[k],"") 
