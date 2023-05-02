#write a Python program that finds the Greatest Common Divisor (GCD) of two numbers. 
#Your program should take two input numbers from the user, 
#and use a function named 'gcd' to find the GCD of those two numbers. 
#Your program should then print out the GCD of the two numbers as the output.

n1 = int (input ()) 
n2 = int (input ())
if n1==0 :
    print(n2)
elif n2==0 :
    print(n1)
elif n1 > n2:
    for i in range (1,n2):
        if n1 % i == 0 and n2 % i == 0:
            hcf = i 
elif n2 > n1:
    for i in range (1, n1):
        if n1%i == 0 and n2 % i == 0:
            hcf = i 
print (hcf)
