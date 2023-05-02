#Write a Python function that takes a string s as input and returns the length of the largest streak of 0s in the string. 
#For example, if the input string is "10001000110000000001", the function should return 6.

def largest_zero_streak(mystring):
    return(len(max(mystring.split('1'))))
s=input()
print(largest_zero_streak(s),end="")
