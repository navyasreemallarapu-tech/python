#comparison operators
a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#login validation
correct_username = "admin"
correct_password = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

print(username == correct_username)
print(password == correct_password)

#logical operators
age = 25
citizen = True

print(age >= 18 and citizen == True)

age = 16
citizen = True

print(age >= 13 and citizen == True)

has_card = False
has_card = True

print(has_card or has_cash)

is_logged_in = True

print(not is_logged_in)



#atm eligibility checker
balance = 10000
withdraw = 5000

print(withdraw > 0 and withdraw <= balance)

#student scholarship eligibility checker
marks = float(input("Enter marks:" ))
attendance = float(input("Enter attendance:", ))

eligible = marks >= 85 and attendance >= 75

print("Scholarship Eligible:" , eligible)

#identity operators
a = None

print(a is None)
print(a is not None)

#bitwpeise orators
a = 5
b = 3
print(a & b)
print(a | b)
print(a ^ b)

print(a << b )
print(a >> b)


#electric city bill calculator
units = int(input("Enter electricity units: "))

rate = 6

bill = units * rate

print("Electricity Bill:", bill)

#travel expense calculator
travel = float(input("Travel expense: "))
food = float(input("Food expense: "))
hotel = float(input("Hotel expense: "))

total = travel + food + hotel

print("Total Expense:", total)

#list in python
#List is an ordered and changeable collection that can store
marks = [80, 90, 75, 85]

print(marks)

#accessing elements in a list
marks = [80, 90, 75, 85]

print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])

#change elements in a list
marks = [80, 90, 75]

marks[1] = 95

print(marks)

#add elements to a list
marks = [80, 90, 75]

marks.append(85)

print(marks)


#remove elements from a list
marks = [80, 90, 75]

marks.remove(90)

print(marks)
#insert method
numbers = [10, 20, 30]

numbers.insert(1,15)

print(numbers)
numbers = [10, 20, 30, 40]
numbers.insert(2,25)
print(numbers)

#extend method
a = [1, 2, 3]
b = [4, 5, 6]

a.extend(b)

print(a)
#clear method
numbers = [10,20,30]

numbers.clear()

print(numbers)

#index method
numbers = [10, 20, 30, 40]

print(numbers.index(30))

#count method
numbers = [10,20,20,30,20] 

print(numbers.count(20))

#sort method
numbers = [40, 10, 30,20]

numbers.sort()
print(numbers)

numbers.sort(reverse=True)

print(numbers)

#reverse method
numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)

#copy method
a = [1, 2, 3]

b = a.copy()

print(b)

#slicing
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])
print(numbers[1:7:2])
print(numbers[6:1:2])

#tuples in python
#Tuple is a collection of multiple values that is ordered and cannot be changed after creation
student = ("Navya sree", 98, "python")

print(student[0])

#access values in a tuple
student = ("Navya sree", 21, 85.5)

print(student[0])
print(student[1])
print(student[2])

#index
numbers = (10, 20, 30, 40)

print(numbers.index(30))

#
numbers = (10, 20, 30, 40)

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))


#sets in python
#Set is a collection of unique values that is unordered and mutable
numbers = {10, 20, 30, 20, 10}

print(numbers)

#why use set?

#Suppose students have selected subjects
subjects = {"python", "Java", "SQL", "Java"}

print(subjects)

#add values to a set
subjects = {"Python", "Java"}

subjects.add("SQL")

print(subjects)

#remove values from a set
subjects.remove("Java")

print(subjects)

#Sets do not allow duplicate values
numbers = {1, 2, 2, 3, 3, 4}

print(numbers)
