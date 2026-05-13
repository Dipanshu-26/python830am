# enumerate() Used with loop counting.
def get_numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

for index, value in enumerate(get_numbers()):
    print(f"iteration index = {index} , iteration value = {value}")


# counter 
from collections import Counter

list1 = ['billing' , 'techinal','billing','login','billing','login']

count = Counter(list1)
print(count)

list2 = [1,2,3,4,1,2,3,4,5,6,7,4,3,2,7,8,9,5,4,3,7,8,9,7,5,4,3]
print(Counter(list2))