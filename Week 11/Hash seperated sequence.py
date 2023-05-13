#Write a program that accepts a hash-separated sequence of words as input and 
#prints the words in a hash-separated sequence after sorting them alphabetically in reverse order.

LSG=sorted(input().split("#"),reverse=True)
print("#".join(LSG),end="")
