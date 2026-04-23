#slicing 

#string[startIndex(0):endIndex(not inclusive)(end of string):stepSize(1)]

# 0     1     2     3     4      5      6      7       8       9
# c     h     a     n     d      r      a      p       u       r
#-10   -9    -8    -7    -6     -5     -4     -3      -2      -1

city = "chandrapur"
print(city[1::])          #handrapur
print(city[2:7:])         #andra
print(city[-8:-2])
print(city[-8:8:])
print(city[-4:-8:])
print(city[-4:-8:-1])
print(city[-8:-4:-1])
print(city[::-1])

print(city[::2])
print(city[1::2])

print(city[::-2])
print(city[1::-2])
print(city[::-2])
print(city[8::-2])

