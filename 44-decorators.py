# =====================================
# DECORATORS IN PYTHON – Explanation
# =====================================

# Decorator means:
# Before a function runs → do something
# Run the original function
# After function runs → do something

# Real-life Example:
# Before entering office → security check
# Enter office → main work
# After work → exit process

# Syntax:
# @decorator_name

#syntax decorator
def decorator(func):
    def wrapper():
        #before 
        func()
        #after 
    return wrapper    

# func → original function
# wrapper → extra functionality holder


# ---------------------------------
# Example 1 : Basic Decorator
# ---------------------------------

# Step 1 : Defining Decorator

def my_decorator(func):                 #my_decorator(say_hello())
    def wrapper():
        print("I will execute before function")
        func()
        print("I will execute after function")
    return wrapper    

# Step 3 : Defining function

@my_decorator
def say_hello():
    print("I am original function")

# Step 3 : call function

say_hello()

# ---------------------------------
# Example 2 : Decorator with Parameters
# ---------------------------------

def my_deco(func):
    def wrapper(a,b):
        print(f"Adding {a} and {b}")
        result = func(a,b)
        print(F"Addition = {result}")
    return wrapper    

        

@my_deco
def addition(a,b):
    return a+b

addition(5,6)

#------------------------------------------------------------------------------
# 1. Decorator to measure execution time

import time
def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Time taken  = {end - start} seconds")
    return wrapper    

@timer
def slow_function():
    time.sleep(3)

slow_function()    


#------------------------------------------------------------------------------
# 2. Decorator that checks login before accessing a function(Useful in web apps.)

def require_login(func):
    def wrapper(user):
        if not user.get("loginIn"):
            print("Access Denied")
        else:
            func(user)    
    return wrapper

@require_login
def dashboard(user):
    print("welcome to your dashboard!!")


user1 = {"name" : "Jhon", "loginIn" : True}
user2 = {"name" : "Merry", "loginIn" : False} 

dashboard(user2)

#------------------------------------------------------------------------------
# 3. Decorator that validates arguments
def non_zero(func):
    def wrapper(a,b):
        if(b==0):
            #print("Error: can not devide by zero")
            return "Error: can not devide by zero"
        return func(a,b)
    return wrapper


@non_zero
def divide(a,b):
    return a/b


result = divide(20,0)
print("result = ",result)

#------------------------------------------------------------------------------
# 4. Decorator that logs function calls