#Given a matrix M write a function snake that accepts a matrix M and
#returns a list which contain elements in snake pattern of matrix M.
#(See explanation to know what is a snake pattern)
def  snake(M):
  s=[]
  for i in range(len(M)):
    if i%2==0:
      s+=M[i]
    else:
      s+=M[i][::-1]
  return(s) 
n = int(input())
M = []
for i in range(n):
    L = list(map(int, input().split()))
    M.append(L)

print(snake(M))
