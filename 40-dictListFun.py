students = [
    {
        "firstName":"neel",
        "lastName":"nitin",
        "age":36,
        "skills":["python","sql"],
        "marks":{"maths":95,"science":97,"english":77}
    },
    {
        "firstName":"virat",
        "lastName":"koholi",
        "age":37,
        "skills":["python","sql","c"],
        "marks":{"maths":95,"science":92,"english":70}
    },
    {
        "firstName":"anand",
        "lastName":"raj",
        "age":35,
        "skills":["python","sql","django"],
        "marks":{"maths":55,"science":92,"english":75}
    },
    {
        "firstName":"kavita",
        "lastName":"godbole",
        "age":32,
        "skills":["python"],
        "marks":{"maths":92,"science":44,"english":76}
    }

]

print(students[0]["skills"])

for x in students:
    e = len(x["skills"])
    print(f'{x["firstName"]} : {e} : {x["skills"]}')

#fn + total marks
total=0
for x in students:
    total =   x["marks"]["maths"]+x["marks"]["science"]+x["marks"]["english"]
    print(f"{x['firstName']} : {total}")

result = [ f'{x["firstName"]} : {x["marks"]["maths"]+x["marks"]["science"]+x["marks"]["english"]}'
    for x in students
]    
print(result)

#-------------------------------------------------------------------------------------------------------------------------------

employees = [
    {"id": 1, "name": "John",   "age": 28, "salary": 45000, "department": "IT"},
    {"id":2,  "name":"Alice",    "age": 34, "salary": 72000, "department": "HR"},
    {"id": 3, "name": "Bob",    "age": 25, "salary": 38000, "department": "IT"},
    {"id": 4, "name": "David",  "age": 42, "salary": 96000, "department": "Finance"},
    {"id": 5, "name": "Sara",   "age": 30, "salary": 55000, "department": "HR"}
]

#first name of all employee
fn1 = list(map(lambda x :x['name'],employees))
print(fn1)

fn2 = [x['name'] for x in employees]
print(fn2)

#make a new list of salayr incresed with 10%

s1 = list(map(lambda x : x['salary'] * 1.10 , employees))
print(s1)

s2 = [x['salary'] * 1.10 for x in employees ]
print(s2)
print([x['salary'] for x in employees])

#update  of salary  of each employee incresed with 10%

# for x in employees:
#     x['salary'] = x['salary'] * 1.10

# print([x['salary'] for x in employees])

#employees having salary > 5000

print(list(filter(lambda x : x['salary']>=50000, employees)))

print([x for x in employees if x['salary']<=50000])

print([x['name'] for x in employees if x['salary']<=50000])

#total salary of all employees 

from functools import reduce
tot = reduce(lambda total , emp : total + emp['salary'], employees, 0)
print(tot)

#find the employees with highest salary for , max
#name of employees having age >30

#count of employees in HR department 