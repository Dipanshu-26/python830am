#sort, count ,reverese ,sorted

#sort - element assesnding order

listA=[11,44,88,4,90,33,77,9,2]
print(listA)
listA.sort()
print(listA)

listB = ['dip','tanish','deep','adi','akay','zeshan','karan']
print(listB)
listB.sort()
print(listB)
#-------------------------------------------------
listA=[11,44,88,4,90,33,77,9,2]
print(listA)
listA.sort(reverse=True)
print(listA)

listB = ['dip','tanish','deep','adi','akay','zeshan','karan']
print(listB)
listB.sort(reverse=True)
print(listB)

print("----------------------------")
#------------------------------------------------
#sorted - returns new list
listA=[11,44,88,4,90,33,77,9,2]
listB = ['dip','tanish','deep','adi','akay','zeshan','karan']

print(listA)
new_listA = sorted(listA)
print(new_listA)
print(listA)

print(listB)
new_listB = sorted(listB)
print(new_listB)
print(listB)

print("----------------------------")
#------------------------------------------------

listA=[11,44,88,4,90,33,77,9,2]
listB = ['dip','tanish','deep','adi','akay','zeshan','karan']

print(listA)
new_listA = sorted(listA, reverse=True)
print(new_listA)
print(listA)

print(listB)
new_listB = sorted(listB,reverse=True)
print(new_listB)
print(listB)

print("----------------------------")
#count
listB = ['dip','adi','tanish','deep','adi','deep','akay','zeshan','karan','deep','adi']
q1 = listB.count('deep')
print(q1)

q1 = listB.count('tanish')
print(q1)

q1 = listB.count('tanishhh')
print(q1)

print("----------------------------")

num1 = [1,2,3,4,5]
num2= num1 

print(num1)
print(num2)

num2[2] ='dip' 

print(num1)
print(num2)

num1[4] = 111

print(num1)
print(num2)

#copy
num1 = [1,2,3,4,5,6]

num2 = num1.copy()

print(num1)
print(num2)

num2[2] ='dip' 

print(num1)
print(num2)

num1[4] = 111

print(num1)
print(num2)

#------------------------------------------------------

listA = [11,22,33,44]
listB = listA

print(listA)
print(listB)

listB[2] = "dip"

print(listA)
print(listB)

listA[1] = "0000"

print(listA)
print(listB)

#-----------------------------------------
listC = [1,2,3,4,5]
listD = listC.copy()

print(listC)
print(listD)

listD[2] = "dip"
print(listC)
print(listD)

listC[2] = "aaa"
print(listC)
print(listD)