#Write a Python program that calculates the dot product of two lists containing the same number of elements. 
#The program should take two lists of integers as input from the user, and then call a function named dot_product to find the dot product of the two lists. 
#The dot_product function should take two lists a and b as input, and should return the dot product of those two lists.

raja=[int(i) for i in input().split()]
rani=[int(i) for i in input().split()] 
def dot_product(Romio, Juliet ):
  return(sum([Romio[i]*Juliet[i]  for i in range(len(Romio))]))   
print(dot_product(raja,rani),end="")
