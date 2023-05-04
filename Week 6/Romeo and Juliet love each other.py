# Romeo and Juliet love each other. Romeo wants to send a message to Juliet and also don't want anyone to read it without his permission. 
# So, he shifted every lower-case letter in the sentence by -2 position and every upper-case letter by -3 position. 
# (If the letter is c, after shifting to by -2 position it changes to a, and for D new letter will be A).
# But the letter is too long, and Romeo does not have enough time to encrypt his whole letter. 
# Write a program to help Romeo that prints the encrypted message. You can assume there are no special characters except spaces and numeric value.

S = input()
import string
low = string.ascii_lowercase
cap = string.ascii_uppercase
ans  = ''
for i in S:
    if i in low:
        index = low.index(i)
        # 1-2 = -1+26 = 25
        index = ((index-2)+26)%26
        ans+=low[index]
    elif i in cap:
        index = cap.index(i)
        # 1-2 = -1+26 = 25
        index = ((index-3)+26)%26
        ans+=cap[index]
    else:
        ans+=i
print(ans,end="")
