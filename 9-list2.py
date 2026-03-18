#list
x1=1
x2=2
x3=3

#          0  1   2  3  4
numbers = [11,22,33,44,55]
print(numbers)

print(numbers[0])

#          0      1        2       3
city = ["pune","delhi","nagpur","banglore"]
print(city[3])
print(city)
print(len(city))

print(type(city))
print(type(numbers))

print("pune" in city)
print("kolkota" in city)


#loops
for x in range(4):
    print(x)
    print(city[x])


num = [0,1,2,4,6,7,9,3,6,9,3,6,8,6,2,6,7,99,5,5]

for x in range(len(num)):           #range(20)
    print(num[x])

print(min(num))
print(max(num))



