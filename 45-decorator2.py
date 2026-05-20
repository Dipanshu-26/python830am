#decorator used to execute after and befrfor functions
def greet_deco(func):
    def wrapper(nm):
        print("I will execute before function")
        func(nm)
        print("I will execute after function")
    return wrapper    

@greet_deco
def greet(name):
    print(f"welcome {name} !!!!")

greet("dipanshu")   

#------------------------------------------------------------------------------
# 4. Decorator with * args and **kwargs function calls

def logger(func):
    def wrapper(*args,**kwargs):
        print(f"calling {func.__name__} with {args} and {kwargs}")
        return func(*args,**kwargs)
    return wrapper


@logger
def multiply(a,b):
    return a*b 

@logger
def student_info(data, details):
    return data, details

res = multiply(5,6)
print(res)

data =[1,2,3]
details = {"name" : "dip","rono": 23}

res2 = student_info([1,2,3],{"name" : "dip","rono": 23})
print(res2)


res2 = student_info(data = [1,2,3],details = {"name" : "dip","rono": 23})
print(res2)