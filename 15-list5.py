#list slicing, list comprehension 

#      0   1  2  3
num = [10,20,30,40]

print(num[1:])

#slicing 
# list_name[startIndex, endIndex(not included):stepSize]
# startIndex==>default 0
# endIndex(not included) ==> last index of list
# stepsize ==> default +1

#print all elements except first

#      0   1  2  3  4  5  6
num = [10,20,30,40,50,60,70]

print(num[1:])

# from start to 50 
print(num[:5])

#print 30 to 60
print(num[2:6])

#copy list
print(num)
print(num[:])

#print list in reverse
print(num[::-1])

#      0   1  2  3  4  5  6
num = [10,20,30,40,50,60,70]

print(num[::2])

print(num[1::2])