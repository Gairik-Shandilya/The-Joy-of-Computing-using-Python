#Given a sqaure matrix M, write a function DiagCalc that 
#calculates the sum of left and right diagonals and prints it respectively

def DiagCalc(mtr):
  lt, rt,k = 0,0,1
  for i in range (len(mtr)):
    lt= lt + mtr[i][i]
    rt= rt + mtr[i][-k]
    k= k+1
  return((lt, rt) )
M=int(input())
mtr=[]
for i in range(M):
 mtr.append([int(i) for i in input().split()])
print (DiagCalc(mtr)[0])
print (DiagCalc(mtr)[1],end="")
