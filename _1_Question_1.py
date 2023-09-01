# Question no. 1
#Write a Python program to get the Fibonacci series between 0 to 50

#Note : The Fibonacci Sequence is the series of numbers :

#0, 1, 1, 2, 3, 5, 8, 13, 21, ....

#Every next number is found by adding up the two numbers before it.

#Expected Output : 1 1 2 3 5 8 13 21 34

no1 = 0
no2 = 1

while no1 <50:
    print(no1,end=', ')
    no1,no2 = no2,no1+no2
    