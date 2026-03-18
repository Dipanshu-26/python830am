a=10
print(a)
print(type(a))

a=-10
print(a)
print(type(a))

a=-10.5
print(a)
print(type(a))

a=10.5
print(a)
print(type(a))

a="dipanshu"
print(a)
print(type(a))

a='dip@123'
print(a)
print(type(a))


a='10+10'
print(a)
print(type(a))

a=10+10
print(a)
print(type(a))


a=True
print(a)
print(type(a))

a=False
print(a)
print(type(a))

true = 123
a="true"
print(a)
print(type(a))

#----------------------------------------------------
#comparision operator ==,!=,<,<=,>,>=

#entity ===> entity ===>output True /False
print(4 == 4)
print(4 == 5)
print(4 != 5)

print(4>3)
print(4>4)
print(4 >= 4)

print(4 < 5)
print(4 < 3)
print(4 <= 4)
print(4 <= 5)


#logical operator  and , or , not

#and truth table
# i/p         i/p          o/p
# true        true          true
# true        false         false
#false        true          false
#false       false          false

#and == >  if any of input is false output is false ... true only if all inputes are true

print(4 == 4   and  4 > 3)
#       t     and    t      => True
print(4 > 3 and 4 > 6)
#      t    and   f        => False
print(4 != 4  and 4 >=4)
#       f     and    t      =>False
print(4 != 4  and  4 >= 6)
#      f      and    f      =>False

#or truth table
#or ==> if any of input is true then output is true.. flase only when all inputes are false 

# i/p         i/p          o/p
# true        true        true 
# true        false       true  
#false        true        true 
#false       false        flase 


print(4 ==4 or 4 != 3)
#      t    or    t    =>t
print(4==4 or 4 > 5)
#      t   or   f       =>t
print(4 != 4 or 4 >=4)
#      f     or    t     => t
print(4 != 4 or 4 > 6)
#      f      or  f       =>t


#not 
# True ==> False
# False  ==> True

print(not(4 == 4))
#    not   True
#      False

print(not(4 > 6))
#    not    False
#      True

print(not(8 == 8 and 8>9))  
#      not(t   and f)
#      not (f)
#      True

print(not(8 == 8 or 8>9))  
#      not(t   and f)
#      not (t)
#      False