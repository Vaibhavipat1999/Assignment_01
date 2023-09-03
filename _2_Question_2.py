# Question no. 2
#Write a Python program that accepts a word from the user and reverse it.

#Sample Test Case

#Input : Edyoda

#output: adoydE


my_string=("Edyoda")
str=""

for i in my_string:
    str=i+str
    
print("Orignal string:",my_string)
print("Reversed string:",str)
