#default parameters

def addA(x,y):
    print(x+y)

addA(10,20)

def addB(x=0,y=0):
    print(x+y)

addB(11,22)
addB(11)
addB()


#positional parameters

def sub(x,y):
    print(x-y)

sub(y=11,x=33)    

#args , kwargs

# *args
# *args → collects multiple values into a tuple
# * in function call → unpacks list into individual values


def addA(x,y):
    print(x+y)

addA(10,20)

def addAll(*args):
    print(type(args))
    print(args)
    print(*args)
    total = 0
    for nm in args:
        total=total+nm
    return total

add1 = addAll(1,2,3,4,5,6,7)
print(add1)

#kwargs 

def addCity(**kwargs):
    print(kwargs)
    kwargs.update({"city" : "pune"})
    return kwargs

q1 = addCity(fn = "dipanshu",ln="chawde")
print(q1)

#-------------------------------------------
def addInfo(**kwargs):
    return{
        **kwargs,
        "city" : "pune",
        "language" : "marathi"
    }

q2 = addInfo(fn = "dipanshu",ln="chawde")
print(q2)