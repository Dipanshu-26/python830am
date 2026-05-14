#GENERATORS IN PYTHON
# Example 1 : return statement
def get_numbers():
    return 1
    return 2   # this will never execute 
    return 3   # this will never execute

print(get_numbers())

# yield : it pauses function  
# return : end 

# Example 2 : return multiple values using list

def get_numbers2():
    return [1,2,3,4]

print(get_numbers2())

#Example 3 : yield statement

def get_numbers3():
    yield 1
    yield 2
    yield 3
    yield 4

gen = get_numbers3()
print(gen)    

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

#print(next(gen))     #StopIteration

print("--------------------------------")
# Example 4 : Infinite Generator

def infinite_generator():
    n=1
    while True :
        yield n
        n=n+1

gen2 = infinite_generator()

print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))

print(next(gen2))
print(next(gen2))
print(next(gen2))
    
print('---------------------------------------------')

# Example 5 : Generator with for loop

# def get_numbers3():
#     yield 1
#     yield 2
#     yield 3
#     yield 4

for x in get_numbers3():
    print(x)


print(next(gen2))    

print('---------------------------------------------')

# Example 6 : Generator for Squares

def square_generator():
    for i in range(1,6):
         yield i *i

sq = square_generator()

print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))
# print(next(sq))   #StopIteration 

print('---------------------------------------------')
#list , tuple , sum ,min max

# def get_numbers3():
#     yield 1
#     yield 2
#     yield 3
#     yield 4

gen = get_numbers3()

#print(list(gen))

#print(tuple(gen))

#print(sum(gen))

#print(min(gen))
print(max(gen))

print('---------------------------------------------')

# def get_numbers3():
#     yield 1
#     yield 2
#     yield 3
#     yield 4

gen = get_numbers3()
print(next(gen))
print(next(gen))

gen.close()
gen1 = get_numbers3()
print(next(gen1))