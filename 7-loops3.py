#loops 
#print 0 to 10
#range(startIndex, endIndex, stepSize)
# for x in range(11):
#   print(x)
  
#break  : stop  

# for x in range(11):    #x=0,1.....7
#   if x==7:
#     break
#   print(x)           #x=0,1...6,
  
  
# for x in range(11): 
#   print(x)
#   if x==7:
#     break

#table of 2 16
# for x in range(2,21,2):
#   #print(x)
#   if x==16:
#     break
#   print(x)
  
# #break at 17 table of 2  
# for x in range(2,21,2):
#   #print(x)
#   if x==17:
#     break
#   print(x)
  
#continue ==>skip
#print 0 to 10 and skip for 7 
# for x in range(11):      #x==>0,1.....6,7,8..10
#   if x==7:
#     continue
#   print(x)              #x==>0,1....6,8...10

# for x in range(11):      
#   print(x)
#   if x==7:
#     continue
#   #print(x)   
  
#--------------------------------------------------
#while

# for ==> range(startIndex,endindex,stepSize)
# startIndex  => inilization  
# endIndex ==> condition    10 ==> x<10
# stepSize ==> inc/dec

# inilization
# while(condition):
#   stemts1
#   stmt2
#   ..
#   ..
#   inc/dec

#print 0 to 10
# x=0 
# while x<=10:
#   print(x)
#   x=x+1


#print table of 2 
# a=2 
# while a<=20:
#   print(a)
#   a=a+2
  
# a=1 
# while a<=10:
#   print(2*a)
#   a=a+1
  
#print table of 5  

# a=5
# while a<=50:
#   print(a)
#   a=a+5
  
# #print table of 5 in reverse 
# a=50
# while a>=5:
#   print(a)
#   a=a-5
  
#break and continue in while loops

#print 0 to 10 and break at 7

# a=0 
# while a<=10:
#   if a==7:
#     break
#   print(a)
#   a=a+1

#print table of 2 in reverse and break at 16
# x=20 
# while x>=2:
#   if x==16:
#     break
#   print(x)
#   x=x-2

#continue   : skips the step

#print 0 to 10 and skip for 7
x=0 
while x<=10:      #x=0,1.....6,7,8
  if x==7:        #x=7
    x=x+1         #x=8
    continue
  print(x)      #x=0,1,6,8
  x=x+1         #x=1,2....7,9