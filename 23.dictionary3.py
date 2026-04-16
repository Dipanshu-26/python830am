info = {
    "fname" : "virat",
    "lname" : "koholi",
    "age" : 38,
    "city" : "mumbai"
}

a=info.get("fname")
print(a)
b=info.get("city")
print(b)

info.clear()
print(info)

info = {
    "fname" : "virat",
    "lname" : "koholi",
    "age" : 38,
    "city" : "mumbai"
}

info.popitem()
print(info)

info.pop("agee",None)
print(info)

print(info["fname"])

#----------------------------------------------------

info = {
    "fname" : "virat",
    "lname" : "koholi",
    "age" : 38,
    "city" : "mumbai"
}
info.update({"language" : "panjabi"})
print(info)

info.update({"language" : "hindi"})
print(info)

info["language"] = "marathi"
print(info)

#--------------------------------------------------------

print(info.keys())
print(info.values())
print(info.items())

#----------------------------------------------------------

#loops
for k in info.keys():
    print(k)

for v in info.values():
    print(v)   

for k, v in info.items():
    print(f"key : {k} , values : {v}")     


for k, v in info.items():
    print(f"{k} : {v}")

#-----------------------------------------------------------
info = {
    "fname" : "virat",
    "lname" : "koholi",
    "age" : 38,
    "city" : "mumbai"
}   

dv = info.setdefault("language" ,"hindi")
print(info)
print(dv)

info = {
    "fname" : "virat",
    "lname" : "koholi",
    "age" : 38,
    "city" : "mumbai",
    "language" : "panjabi"
}   

dv = info.setdefault("language" ,"hindi")
print(info)
print(dv)
#----------------------------------------------------------
info = {
    "fname" : "virat",
    "lname" : "koholi",
    "age" : 38,
    "city" : "mumbai",
    "language" : "panjabi"
}


defaults = {
    "language": "hindi",
    "country": "India",
    "course": "Python"
}

for key, value in defaults.items():
    info.setdefault(key, value)

print(info)    