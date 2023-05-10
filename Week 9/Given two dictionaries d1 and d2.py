#Given two dictionaries d1 and d2, write a function mergeDic that accepts two dictionaries d1 and d2 and return a new dictionary by merging d1 and d2. 
#Note: Contents of d1 should be appear before contents of d2 in the new dictionary and in same order. In case of duplicate value retain the value present in d1.

def mergeDic(d1,d2):
  for i in d2.keys():
    if i not in d1.keys():
      d1[i]=d2[i]
  return(d1)  
key = list(map(int, input().split()))
val = list(map(int, input().split()))

d1 = {}
for i in range(len(key)):
    d1[key[i]] = val[i]
    
d2 = {}
key = list(map(int, input().split()))
val = list(map(int, input().split()))
for i in range(len(key)):
    d2[key[i]] = val[i]

print(mergeDic(d1, d2))
