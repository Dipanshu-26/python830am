def get_numbers3():
    yield 1
    yield 2
    yield 3
    yield 4

gen = get_numbers3()
print(next(gen))
print(next(gen))

gen.close()
gen1 = get_numbers3()
print(next(gen1))

print("----------------------------------------------")

def read_file_normal(filepath):
    with open(filepath, "r") as f :
        return f.readlines()

content = read_file_normal("students_data.txt")
print(content)

# What happens here?
# readlines() loads the entire file into memory
# If file is very large (100MB, 1GB, etc.), memory usage becomes high
# Can slow down the program

# What is with?
# with open(...) as f:

# This means: open the file, do the work, automatically close the file
# So we do not need:
# f.close()
print("----------------------------------------------")
#------------------------------------------------------------------------------

# 2. Generator for reading a large file line by line (This is a real-life use case to save memory.)

def read_file(file_path):
    with open(file_path,"r") as f :
        for line in f :
            yield line


for line in read_file("students_data.txt"):
    print(line.strip())

#---------------------------------------------------------

squars =  (x*x for x in range (5))

# print(next(squars))

# print(next(squars))
# print(next(squars))

print(next(squars))
print(next(squars))
print(next(squars))
print(next(squars))
print(next(squars))

try : 
    print(next(squars))
except StopIteration :
    print("Iteration is stoped")


