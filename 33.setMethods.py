setA = {"a", "b", "c", 11, 33}
setB = {11, 33, 55, 66, 77}

# 1. add() → Adds a single element
setA.add("new")
print(setA)

# 2. update() → Adds multiple elements
setA.update(["up1","up2"])
print(setA)

# 3. remove() → Removes element (error if not found)
setA.remove("up1")
print(setA)

# 4. discard() → Removes element (no error if not found)
setA.discard("up2")
print(setA)

setA.discard("up2abc")
print(setA)

# 5. pop() → Removes a random element
res=setA.pop()
print(setA)
print(res)

# 6. clear() → Removes all elements
setA.clear()
print(setA)

# 7. copy() → Creates a copy of set
setA=setB  #reference copy
setA=setB.copy()    #creates new reference(memory) elements copy

# 8. union() → Combines both sets removes duplicate
setA = {"a", "b", "c", 11, 33}
setB = {11, 33, 55, 66, 77}
res1 = setA.union(setB)
print(res1)
print(setA)
print(setB)

print("-----------------------------")
# 9. intersection() → Common elements
setA = {"a", "b", "c", 11, 33}
setB = {11, 33, 55, 66, 77}
res2 = setA.intersection(setB)
print(res2)
print(setA)
print(setB)

print("-----------------------------")
# 10. intersection_update() → updates first set with Common elements
# setA.intersection_update(setB)
# print(setA)
# print(setB)
print("-----------------------------")
setB.intersection_update(setA)
print(setA)
print(setB)

print("-----------------------------")
setA = {"a", "b", "c", 11, 33}
setB = {11, 33, 55, 66, 77}
# 11. symmetric_difference() → gives the uncommen Elements of setA not in setB
res3 = setA.symmetric_difference(setB)
print(res3)
print(setA)
print(setB)

print("-----------------------------")
setA = {"a", "b", "c", 11, 33}
setB = {11, 33, 55, 66, 77}
# 12. symmetric_difference() → make setA(first set) with the uncommen Elements of setA not in setB
setA.symmetric_difference_update(setB)
print(setA)
print(setB)
print("-----------------------------")
setA = {"a", "b", "c", 11, 33}
setB = {11, 33, 55, 66, 77}
setB.symmetric_difference_update(setA)
print(setA)
print(setB)

print("-----------------------------")
setA = {"a", "b", "c", 11, 33}
setB = {11, 33, 55, 66, 77}
# 13.difference() → Elements in setA not in setB

print(setA.difference(setB))
print(setB.difference(setA))
print(setA)
print(setB)

print("-----------------------------")
setA = {"a", "b", "c", 11, 33}
setB = {11, 33, 55, 66, 77}
# 14.difference_update() → updates setA(first) set with Elements in setB(second set)
setA.difference_update(setB)
print(setA)
print(setB)

print("-----------------------------")
# 15. issubset() → Checks if one set is subset of another
setA = {"a", "b", "c", 11, 33}
setB = {11, 33, 55, 66, 77}
print(setA.issubset(setB))

print("-----------------------------")
setA = {11, 33}
setB = {11, 33, 55, 66, 77}
print(setA.issubset(setB))

print("-----------------------------")
# 16. issuperset() → Checks if one set is superset of another
setA = {"a", "b", "c", 11, 33, 55, 66, 77}
setB = {11, 33, 55, 66, 77}
print(setA.issuperset(setB))

print("-----------------------------")
# 17. isdisjoint() → Checks if no common elements
setA = {"a", "b", "c", 11, 33, 55, 66, 77}
setB = {11, 33, 55, 66, 77}
print(setA.isdisjoint(setB))

print("-----------------------------")
setA = {"a", "b", "c"}
setB = {11, 33, 55, 66, 77}
print(setA.isdisjoint(setB))