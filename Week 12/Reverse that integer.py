#Write a program to an integer as an input and reverse that integer 
n=int(input())
print(int("".join(list(str(n))[::-1])),end="")   
                  
