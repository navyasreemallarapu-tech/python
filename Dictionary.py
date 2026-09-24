#Dictionary is a key value pair and it is unord"ered and mutable
student = {"Name" : "Navya sree", "marks" :"98", "subject" : "python"}
print(student)
print(student.keys())
print(student.values())
print(student.items())
#access the elements in the dictionary
student = {"Name" : "Navya sree","age" : "17","subject" : "python"}
print(student["Name"])
print(student["age"])
print(student["subject"])
#change the values in a dictonary
student["age"] = 11
print(student["age"])
#add new data to the dictionary
student["city"] = "somala"
print["student"]
#remove data
student.pop("city")
print(student)
student = {"name":"Navya sree","marks":"98","course":"python"}
print(student.get('name'))
print(student.get('marks'))
print(student.get('course'))
#update the values of specified key
student.update({"marks":18})
print(student)
#popitem()
student={"name":"Navya sree","marks":"98","subject":"python"}
student.popitem()
print(student)
#set default
student = {"name":"Navya sree"}
student.setdefault("age",17)
print(student)

#clear method
student.clear()
print(student)
student = {"name":"Navya sree","age":"17"}
new_student = student.copy()
print(new_student)
#order of evluation(bodmas)
result = 2+13*2
print(result)


