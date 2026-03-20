#sort count ,reverese ,sorted

#sort - element assesnding order
listA=[33,55,99,22,77,11]
print(listA)
listA.sort()
print(listA)

listB=["dip","adi","babita","karan","zshan","deep"]
print(listB)
listB.sort()
print(listB)

#desceding order
listA=[33,55,99,22,77,11]
listB=["dip","adi","babita","karan","zshan","deep"]
listA.sort(reverse=True)
listB.sort(reverse=True)
print(listA)
print(listB)

#sorted()

numbers=[7,1,4,2,8,9,3,5]
new_nums=sorted(numbers)
print(new_nums)
print(numbers)

#desceding
new_nums2=sorted(numbers,reverse=True)
print(new_nums2)

#reverse()
listA=[33,55,99,22,77,11]
listB=["dip","adi","babita","karan","zshan","deep"]

listA.reverse()
print(listA)

listB.reverse()
print(listB)

#count 
listB=["dip","adi","zshan","babita","adi","karan","zshan","adi","deep"]
print(listB.count("dip"))
print(listB.count("zshan"))
print(listB.count("adi"))