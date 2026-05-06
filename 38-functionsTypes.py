#map

birthyear = [2021,2020,2000,1999,1983,1990]
age=[]

#for loop ---
for year in birthyear:
    age.append(2026-year)

print(age)    

#map -----
#         el     return     list
age2  = list(map(lambda x : 2026 - x ,birthyear) )
print(age2)

#list comprehension
age3 =[2026 - y for y in birthyear]
print(age3)

#---------------------------------------------------------------
#filter
marks = [22,56,89,76,11,90,23,55,99]
above35 = []
for m in marks:
    if m>=35:
        above35.append(m)

print(above35)
#-------------
above35_2 = list(filter(lambda m : m>=35 , marks))
print(above35_2)

#------------------

above35_3 = [m for m in marks if m>=35]
print(above35_3)

#-----------------------
below35_2 = list(filter(lambda m : m<35 , marks))
print(below35_2)

#------------------

below35_3 = [m for m in marks if m<35]
print(below35_3)

#--------------------------------------------------------------------
#reduce

marks = [22,56,89,76,11,90,23,55,99]

total = 0
for m in marks:
    total = total+m            # 0+22, 22+56, 78+89.....

print(total)

#reduce-----
from functools import reduce
#addition
sum = reduce(lambda total,m : total+m ,marks,0 )
print(sum)

#multiplication
mul = reduce(lambda acc ,m : acc*m,marks,1)
print(mul)