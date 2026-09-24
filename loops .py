#use while when repetition depends on a condition.
# Looping through numbers 1 to 5 using while loop
i = 1

while i <= 5:
    print(i)
    i = i+1

#use for when you know how many times
# Looping through numbers 1 to 5
for i in range(1, 6):
        print(i) 

#Print numbers from 1 to 10
for i in range(1, 11):
      print(i)

#Print numbers from 10 to 1
for i in range(10,0,-1):
      print(i)
#Print numbers from odd to 50
for i in range(0,51):
      print(i)
#Print even numbers 2 to 50
for i in range(2,51,2):
      print(i)
#Print odd numbers 2 to 50
for i in range(2,51,3):
      print(i)
#Print odd numbers from 1 to 50
for i in range(1,51,2):
      print(i)
#print ("Multiples of 5 from 5 to 50:")
for i in range(5,51,5):
      print(i)
#Multiplication table
number = int(input("Enter number"))

for i in range(1, 11):
      print(number, "X", i, "=", number * i)

# Sum of numbers from 1 to n
n = int(input("Enter n: "))

total = 0

for i in range(1, n+1):
      total = total + i

print("Sum:", total)
# factorial of a number
n = int(input("Enter number: "))

factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i


print("Factorial:",factorial) 
#sum of numbers from 2 to n
n = int(input("Enter n: "))

total = 0

for i in range(2, n + 1, 2):
      total = total + i

print("Sum:", total)

# count of multiples of 3
n = int(input("Enter n: "))

count = 0

for i in range(1, n + 1):
      if i % 3 == 0:
            count = count + 1

print("count:", count)            

#count of multiples of 5
n = int(input("Enter n: "))

count = 0

for i in range(1, n + 1):
      if i % 5 == 0:
            count = count + 1

print("count:", count)
# Sum of multiples of 5
n = int(input("Enter n: "))

total = 0

for i in range(1, n + 1):
    if i % 5 == 0:
          total = total + i

print("Sum:", total)

#print all even numbers from 2 to 50
i = 2

while i <= 50:
      print(i)
      i = i + 2

#print  = 1

while i <= 50:
      print(i)
      i = i + 1

      
# print total of numbers enter by 0 until 0 is entered all odd numbers from 2 to 50
total = 0

number = int(input("Enter number: "))

while number != 0:
      total = total + number
      number = int(input("Enter number: "))

print("Total:", total) 

#password check
password = ""

while password != "python123":
      password = input("Enter password: ")

print("Login successful")      

# Count the number of digits in a number
number = int(input("Enter number"))


count = 0

while number > 0:
      number = number//10
      count = count + 1

print("Number of digits:",count) 

# sum of digits in a number
number = int(input("Enter number: "))

total = 0

while number > 0:
      digit = number % 10
      number = number // 10
      total = total + digit

print("Sum of digits:", total)

#Reverse a number
number = int(input("Enter number: "))

reverse = 0

while number > 0:
      digit = number % 10
      number = number // 10
      reverse = reverse * 10 + digit

print("Reverse:", reverse)

# Palindrome
number = int(input("Enter number:"))

original = number
reverse = 0

while number > 0:
      digit = number % 10
      reverse = reverse * 10 + digit
      number = number //10

if original == reverse:
      print("Palindrome")
else:
      print("Not Palindrome") 

# check the number is prime or not
number = int(input("Enter number: "))

count = 0

for i in range(1, number + 1):
    if number % i == 0:
          count = count + 1

if count == 2:
      print("Prime number")
else:
      print("Not a prime number")

# Print all prime number between 2 and 100
for number in range(2, 101):

    count = 0

    for i in range(1,number + 1):
        if number % i == 0:
            count = count + 1

    if count == 2:
        print(number)
# break statement
for i in range(1, 11):

    if i == 5:
          break #exit the loop
    print(i)

#pass keyword
for i in range(1, 6):

      if i == 3:
            pass

      print(i)

for i in range(1,11):
      if i == 7:
            print("Number found")
            break

      print(i)

# print odd numbers from 1 to 10
for i in range(1, 11):

      if i % 2 == 0:
            continue

      print(i)            

#print numbers until user enters 0
while True:

      number = int(input("Enter number: "))

      if number == 0:
            break

      print("You entered:", number)

# print numbers from 1 to 100, but skip multiples of 3 and stop at 50
for i in range(1, 101):

      if i == 50:
            break
      if i % 3 == 0:
            continue

      print(i)

# calculate the sum of positive numbers entered by the user
total = 0

while True:

      number = int(input("Enter number: "))

      if number < 0:
            continue

      if number == 0:
            break

      total = total + number

print("Total:", total)

# Find the first number between 1 and 100 that is divisible
for i in range(1,101):

      if i % 3 == 0 and i % 5 == 0:
            print("First number:", i)
            break

# calculate the sum of positive numbers entered by the user ignoring negativity
total = 0

for i in range(10):

      number = int(input("Enter number: "))

      if number < 0:
            continue

      total = total + number

#password checked with limited attempts
correct_password = "Python123"

for attempt in range(1,4):

      password = input("Enter password: ")

      if password == correct_password:
            print("Login successful")
            break

      print("Wrong password")

else:
      print("Account locked")


# Find the largest number among 5 numbers entered by the user
largest = None

for i in range(5):

      number = int(input("Enter number: "))

      if largest is None or number > largest:
            largest = number

print("Largest:", largest)

# Find the largest number among 5 numbers entered by the user
largest = None

for i in range(5):

      number = int(input("Enter number: "))

      if largest is None or number < smallest:
            smallest = number

print("Smallest:", smallest)

