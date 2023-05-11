#Given a list L write a program to make a new list and match the numbers inside list L to its respective index in the new list. 
#Put 0 at remaining indexes. Also print the elements of the new list in the single line. (See explanation for more clarity.)

L=[int(i) for i in input().split()]
ans=[0]*(max(L)+1)
for i in range(len(ans)):
  if i in L:
    ans[i]=i
print(*ans,end="")
