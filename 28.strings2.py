#count, find, index

#count() --counts presence of given latter
a="niranjan"
print(len(a))
print(a.count("a"))
print(a.count("z"))

#find()--finds index of given latter and gives -1 if not presesnt
print(a.find('n'))
print(a.find('a'))
print(a.find('r'))
print(a.find('z'))

#index() - finds index of letter and gives error if not presesnt
print(a.index('n'))
#print(a.index('z'))

#startswith 
print(a.startswith("n"))
print(a.startswith("z"))
print(a.startswith("ni"))

#endswith
print(a.endswith("n"))
print(a.endswith("jan"))
print(a.endswith("z"))

print("---------------------------------------")
#isalpha(),isnumeric(),isalnum()
name = "tanish"
print(name.isalpha())
print(name.isnumeric())
print(name.isalnum())

print("---------------------------------------")
#isalpha(),isnumeric(),isalnum()
name = "tanish@123"
print(name.isalpha())
print(name.isnumeric())
print(name.isalnum())

print("---------------------------------------")
#isalpha(),isnumeric(),isalnum()
name = "tanish123"
print(name.isalpha())
print(name.isnumeric())
print(name.isalnum())

print("---------------------------------------")
#isalpha(),isnumeric(),isalnum()
name = "123"
print(name.isalpha())
print(name.isnumeric())
print(name.isalnum())

print("---------------------------------------")
#isspace()

print(" ".isspace())
print(" a".isspace())
print("---------------------------------------")

txt="My Name Is Dipanshu"
print(txt.istitle())

txt="My name Is Dipanshu"
print(txt.istitle())

#join()
arr = ["My", "name", "Is", "Dipanshu"]
print("@".join(arr))
print("-".join(arr))

#split
txt="My name Is Dipanshu"
arr1 =txt.split(" ")
print(arr1)

txt="My-name-Is-Dipa-nshu"
arr2 = txt.split("-")
print(arr2)

str = "55₹/kg"
arr = str.split("₹")
print(arr)
print(arr[0])

# ljust , rjust -- Left-justifies the string. It adds extra characters on the right side.
# rjust(width, fillchar)
# ljust(width, fillchar)
# center(width, fillchar)

txt="hi"

print(txt.ljust(5,"."))
print(txt.rjust(5,"."))
print(txt.center(6,"."))

print(txt.ljust(5," "))
print(txt.rjust(5," "))
print(txt.center(6," "))

#rstrip,lstrip,strip

txt="     goa      "
print(txt.strip())
print(txt.lstrip())
print(txt.rstrip())

# remove prefix 
txt="unhappy"
q1=txt.removeprefix("un")
print(q1)

print()

# remove sufficx
str = "55₹/kg"
q2=str.removesuffix("₹/kg")
print(q2)

txt="studentData.txt"
print(txt.removesuffix(".txt"))

# replace()    -- case sensitive
txt = "I love Python programming... python is very easy to go language...."
q3 = txt.replace("Python","Javascript")
print(q3)


# swapcase()

#title()

# zfill

# partition()

#reverse string
