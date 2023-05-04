#write a function whole(N) which takes a number N and 
#return the sum of first N whole number. Write the program using recursion.
def whole(N):
  sum=0
  for i in range(0,N+1):
    sum=sum+i
  return sum
N=int(input())
print(whole(N))
