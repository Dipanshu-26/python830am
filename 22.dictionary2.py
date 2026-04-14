#CRUD in dict 
info = {
    "name" : "Virat",
    "surname" : "koholi",
    "age" : 35,
    "city" : "mumbai"
}

#retrive
print(info)

a=info.get("name")
print(a)
b=info.get("city")
print(b)

#delete 

#delete all items
info.clear()
print(info)

# pop(k)
info = {
    "name" : "Virat",
    "surname" : "koholi",
    "age" : 35,
    "city" : "mumbai"
}

info.pop("age")
print(info)

#info.pop("location")    #KeyError: 'location'

info.pop("location" ,None)

#popitem : last key delets

print(info)
info.popitem()
print(info)

#del  : delet key from dictionary

del info["name"]
print(info)

info = {
    "name" : "Virat",
    "surname" : "koholi",
    "age" : 35,
    "city" : "mumbai"
}
print(info)
info.update({"team" : "mumbai indians"})
print(info)

info.update({"team" : "RR"})
print(info)

info["color"] = "blue"
print(info)

info["color"] = "sky blue"
print(info)


info.setdefault("batch" , "2029")
print(info)

info = {
    "name" : "Virat",
    "surname" : "koholi",
    "age" : 35,
    "city" : "mumbai",
    "team" : "mumbai indians"
}

info.setdefault("city" ,"pune")
print(info)

info.update({"city" : "delhi"})
print(info)