#loops in python 
#for , while

#for
#print 0 to 5
# print(0)
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# range(startIndex, endIndex, stepSize)
# startIndex -- default 0 (optional)
# endIndex -- must (end value is not included)
# stepSize -- default step size +1

#print 0 to 10
for x in range(11):     # x=0,1,2,3,4.......10,11      (x=0,x<11,x=x+1)
    print(x)             # x=0,1,2,3,4.......10


#print 1 to 10
for x in range(1,11):
    print(x)

#print table of 2
for x in range(2,21,2):
    print(x)    

for x in range(1,11):
    print(x*2)    

#print table of 5
for x in range(5,51,5):
    print(x)    

#print  0 to 10 in reverse
for a in range(10,-1,-1):
    print(a)

#print  1 to 10 in reverse
for a in range(10,0,-1):
    print(a)

#print table of 2 in reverse 
for a in range(20,1,-2):
    print(a)

#print table of 5 in reverse
for a in range(50,4,-5):
    print(a)

#break and continue 
#print  0 to 10 exit loop at 7
#break

for x in range(11):
    #print(x)
    if(x==7):
        break
    print(x)


#print table of 2  break on 16
for x in range(2,21,2):
    if(x==16):
        break
    print(x) 

#continue 
#print  0 to 10 skip loop at 7
for x in range(11):        #x=0,1,2.....6,7,8...10,11  (x<11)
    if(x==7):
        continue         
    print(x)          #x=0,1,2,.....6,8...10