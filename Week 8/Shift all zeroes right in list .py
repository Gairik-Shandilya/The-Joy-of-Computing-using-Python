#Write a program that take list L as an input and shifts all zeroes in list L 
#towards the right by maintaining the order of the list. Also print the new list.

L=[int(i) for i in input().split()]
A=[]
B=[]
for i in L:  
  if i==0:
    A.append(0)
  else:
    B.append(i)
print(B+A,end="")
