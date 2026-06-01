# // Use this editor to write, compile and run your Java code online
# // overloading - same class , same method name , different signature

# import java.util.*;

# public class Main {
#     public static void main(String[] args) {
#       System.out.println("Hello, World!");
#       addition(12,2);
#       addition(11,22,33);
#       addition(10,20,30,40);
#     }
    
#     public static void addition(int x , int y){
#       System.out.println(x+y);
#     }
    
#     public static void addition(int x , int y, int z){
#       System.out.println(x+y+z);
#     }
    
#     public static void addition(int x , int y,int z, int a){
#       System.out.println(x+y+z+a);
#     }
# }

#---------------------------------------------------------------------------------

class Claculator:
    # def addition(self,a,b):
    #     print(a+b)
    # def addition(self,a,b,c):
    #     print(a+b+c)  
    # def addition(self,a,b,c,d):
    #     print(a+b+c+d)              

    def addition(self, a=None,b=None,c=None,d=None):
        if a!=None and b!=None and c!=None and d!=None:
            print(a+b+c+d)  

        elif a!=None and b!=None and c!=None:
            print(a+b+c)     

        elif a!=None and b!=None :
            print(a+b)     

obj1= Claculator()
obj1.addition(11,22,33,44)
obj1.addition(10,20,30)
obj1.addition(12,3)           