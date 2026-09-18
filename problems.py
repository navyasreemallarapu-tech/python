#Program 1:Display Personal Details Using Variables
#Getting the input from user
name = input()
age = int(input())
height = float(input())
#Printing the values
print(name)
print(age)
print(height)

#Program 2 : Personalized Greeting
name = input()
print(f"Hello,{name}!")

#program 3:Add Two Numbers Read as String
#taken the input as a string
a = int(input())
b = int(input())
#converting the string into integer
a = int(a)
b = int(b)
#find the sum
total = a+b
#print a+b
print(total)

#program 4:float to integer conversion
#float:Numbers with decimal value
#int:whole numbers without any decimal or fractional value
#reading a float value from the user
n = float(input())
#print the float value
print(n)
#convert the float into integer:Decimal points values will be removed
new = int(n)
#print the value
print(new)

#program 5:Sum using Arithmetic operator
#reading 2 integers from the user
a = int(input())
b = int(input())
#Finding the sum and printing the result
print(a+b)

#Program 6:Area of a rectangle
#Reading input from the user
length = float(input())
breadth = float(input())
#calculating the area of a rectangle
area = length*breadth
#print the result
print(area)

#program 7:Quotient and Remainder
#user inputs
a = int(input())
b = int(input())
#find the Quotient
q = a/b
#find the remainder
r = a%b
#print the result
print(q)
print(r)

#Program 8:Power calculation
#reading user input
base = int(input())
exponent = int(input())
#calculate the power of and print the result
print(base**exponent)

#Program 9:Average of three numbers
#Taking 3 integer numbers from the user
n1 = int(input())
n2 = int(input())
n3 = int(input())
#Find the total
total = n1+n2+n3
#Find the Average
avg = total/3 #Division operator /--> always gives the result as a float
#Print the Average
print(avg)

#Program 10:Greater than comparison
#read 2 integer numbers from user
a = int(input())
b = int(input())
#check whether the 1st number is greater than the 2nd number
print(a>b)

#Program 11:Equality check
#check whether both the numbers are same or not
#If the numbers are same  - true
#If the numbers are different - false
#Reading the input from the user
n1 = int(input())
n2 = int(input())
print(n1==n2)

#Program 12:Both numbers Positive check
#If the number is greater than 0
#logical and --> If all the combining conditions are True , result is true
#Reading the input from the user
n1 = int(input())
n2 = int(input())
print(n1>0 and n2>0)

#Program 13: Logical NOT on a condition
#Logical not -->reverse the result
#True --> False
#False --> True
#Reading the input from the user
num = int(input())
print(not(num>0))

#Program 14:Augmented Assignment Operations
#Read a number from the user
a = int(input()) #20
a = a+5 # a = 20+5 -->25
a = a*2 # a = 25*2 -->50
a = a-3 # a = 50-3 -->47
print(a)

#Program 15:Exchange Values of Two variables
#Reading the input from the user
a = int(input())
b = int(input())
#Logic 1 - using temp variable
temp = a
a = b
b = temp
print(a)
print(b)
#Logic 2 : Without using temp (3rd variable)
a=a+b
b=a-b
a=a-b
print(a)
print(b)
#Logic 3: Without using temp (3rd variable)
a = a^b
b = a^b
a = a^b
print(a)
print(b)
#Logic 4: Without using temp(3rd variable)
#problem: It cannot handle 0
a = a*b
b = a/b
a = a/b
print(a)
print(b)
#Logic 5:Using Python's special
# simplest way
# a,b = b,a
print(a)
print(b) 

#program 16:calculate simple interest
#Formula:(principle*Rate*Time)/100
#User Inputs
principle = float (input()) #Loan amount
rate = float(input()) #rate of interest
time = float(input()) #repayment time
#calculate interest
si = (principle*rate*time)/100
#print the result
print(si)

#Program 17:Temperature conversion (celsius to fahrenheit)
#formula:f = (c*9/5)+32
#read the temperature in celsius
c = float(input())
#convert the celsius into fahrenheit
f = (c*9/5)+32
print(f)

#program 18:Check Divisibility by 3 and 5
n = int(input())
print(n%3==0 and n%5==0)

#Program 19:Sum of digits of a two digit number
num = int(input()) #num = 48
tens = num//10     #tens = 48//10=4
units = num%10     #units = 48%10 = 8
total = tens + units #total = 4+8 = 12
print(total)

#Program 20: At least one even number
#Even Number:If the number is divisible by 2(Without any reminder)
#Logical or --> If any one of the combining condition is true,then the result is true.
#Arithmetic operators
#/ --> Division - result is in form of decimal value
Example: 13/2 = 6.5
#// --> Floor Division - result is in form of integer
Example: 13/2 = 6
#% --> Module - result is the remainder of the division operation
Example : 13/2 = 1
#Reading the input from the user
#n1 = int(input())
#n2 = int(input())
print(n1%2==0 or n2%2==0)