info = {
    "name" : "dipanshu",
    "age" : 40,
    "location" : "pune"
}

print(info)

students = info 
print(students)

students["surname"] = "chawde"
print(students)

print(info)

#-------------------------------------------------

students2 = info.copy()
print(info)
print(students2)

students2["skills"] = "python"
print(students2)

print(info)


