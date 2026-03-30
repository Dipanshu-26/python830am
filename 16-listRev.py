#list slicing, list comprehension 

#list slicing allows you to extract the part of list 
#[startIndex:endIndex:stepSize]
# startIndex ==>default strats form 0 
# endIndex ==> default end of list (id values is given end value nit included)
# stepSize ==>1


#print all elements except 0th index
#         0  1  2  3  4  5 6   7
listA = [11,22,33,44,55,66,77,88]
print(listA[1:])


#print 1 to 4
print(listA[1:5])

#print from start to 66(5)
print(listA[:6])

#copy list
print(listA)
print(listA[:])

#print in reverse
print(listA[::-1])
print(listA[::-2])

#list comprehension 

listB = [44,67,88,12,33,7,42,82,5]

print("---------------------------")
# #square of each elemet 
# square = []
# for x in listB:     # x= 44,67,88...5
#     print(x)

# #with range function
# print("---------------------------")
# for x in range(len(listB)):     #range(0,9,1)  ==> 0,1,2....8
#     #print(x) 
#     print(listB[x])             #listB[0],listB[1],listB[2]

#         0  1  2 3  4  5  6  7 8 
listB = [44,67,88,12,33,7,42,82,5]      #length =9

#for loop  without range
for x in listB:
    print(x)

print("---------------------------")
#for loop with range for list

for x in range(len(listB)):       #range(0,9(endIndex<9),1)
    #print(x)                     # x= 0 1 2 3 4 5 6 7 8
    print(listB[x])                #listB[0],listB[1],listB[2].....list[8]