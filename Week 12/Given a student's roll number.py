#Given a student's roll number in the following format rollNumber@institute.edu.in, 
#write a program to find the roll number and institute name of the student.

rollg=input()
print(rollg.split('@')[0],rollg.split('@')[1].split(".")[0],end="") 
