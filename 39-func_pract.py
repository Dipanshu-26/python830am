#program 1
nos = [1,2,3,4,5]

#map
print(list(map(lambda x: x*x,nos)))
sq=list(map(lambda x: x*x,nos))
print(sq)

print([x*x for x in nos])

#program 2
names = ["dipanshu chawde","rucha gaware","aditya masalkar","shivani ukhalkar"]

name1 = "dipanshu chawde"
print(name1.split(" ")[1])

print(list(map(lambda x : x.split(" ")[0],names)))
print(list(map(lambda x : x.split(" ")[1],names)))

print(f"first names are  =  ",[x.split(" " )[0] for x in names])
print(f"surname names are  =  ",[x.split(" " )[1] for x in names])

nos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

e = list(filter(lambda x : x%2==0,nos))
print(e)
o= list(filter(lambda x: x%2!=0,nos))
print(o)


print(f"even nos= ",[x for x in nos if x%2==0])
print(f"odd nos= ",[x for x in nos if x%2!=0])


names = ["dipanshu","neel","tanish","aditya","niranjan","nitin","raj"]

print(list(filter(lambda str : len(str) >=6 ,names)))

print([x for x in names if len(x)>=6])


students  = [
    {
        "fn":"sachin",
        "ln":"tendulkar",
        "age":23
    },
    {
        "fn":"ms",
        "ln":"dhoni",
        "age":34

    },
    {
        "fn":"sourav",
        "ln":"ganguli",
        "age":35
    }
]

print(students[0]["age"])
print(students[0]["fn"])

#    return(x)    for loop              condition(if any)
print([x        for x in students   if x["age"] > 30 ])

nos =[1,2,3,4,5,6,7]
print([x*x*x for x in nos ])
print([x*x*x for x in nos if x%2==0])