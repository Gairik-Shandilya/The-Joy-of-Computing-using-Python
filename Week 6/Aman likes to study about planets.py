# Aman likes to study about planets. Every night he goes outside and observe some planets with his telescope. 
# Then he guesses the distance of each planet and pen it down. In this process he also pen down his favourite planet position. 
# Given the distance of each planet to be unique you need to return position of Aman's favourite planet after sorting all the distances.

n = int(input()) 
L = list(map(int, input().split()))
fav=L[int(input())-1]
newarr=sorted(L)
pos=(newarr.index(fav)+1)
print(pos)
