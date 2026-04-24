# In Python, immutable means:

# 🟥 You cannot change the object after it is created.

# Once the value is stored, it cannot be modified, updated, or altered in memory.

# 🟦 Examples of Immutable Types

# These cannot be changed:

# int (numbers)
a=11
a=12

# float

# str (string)
d="dipanshu"
print(d)
#d[0]="a"
print(d[0])

# tuple

# bool

# frozenset

#Example: String is immutable

s = "hello"
#s[0] = "H"

# Output: TypeError: 'str' object does not support item assignment
# You cannot change individual characters.

# Example: Tuple is immutable
t = (1, 2, 3)
#t[0] = 10

# Error: TypeError: 'tuple' object does not support item assignment

# but mutable objects CAN change ---------------------------------------

# Examples of mutable (changeable):

# list

# dict

# set

# Example:

nums = [1, 2, 3]
nums[0] = 10
print(nums)

# Output: [10, 2, 3]

# Immutable = cannot be changed
# Mutable = can be changed