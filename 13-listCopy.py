#     0 1  2 3
num1=[1,2,3,4]

num2 = num1

print(num1)
print(num2)

num2[1] =222
print(num1)
print(num2)

#copy

num3=[11,22,33,44,55]
num4=num3.copy()

num3[1]=100

print(num3)
print(num4)

num4[3]=400

print(num3)
print(num4)