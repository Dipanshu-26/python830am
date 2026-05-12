#file handeling in python

#create file 

# file = open("students_data.txt","x")
# file.close()


#"x" mode means: create new file only, gives error if file already exists

#write file 
file = open("students_data.txt","w")
#"w" mode means:creates file if not exists ,clears old data if file already exists 

file.write("Name : Mohan \n")
file.write("COurse : Data Analyst \n")
file.write("Python Module : FIle handeling \n")
file.close()

print("Data is written successfully!")

#-------------------------------------------------------------

file = open("students_data.txt","r")
content = file.read()
print("\nReading file contsnts : \n")
print(content)
file.close()

file = open("students_data.txt","w")
file.write("Name : Dipanshu \n")
file.write("COurse : GenAI \n")
file.write("Python Module : oops concepts \n")
file.close()

print("Data is written successfully!")

#"w" mode replace file contents with new contents
#---------------------------------------------------------------
f= open("students_data.txt","a")
f.write("\n")
f.write("this is content of append mode \n")
f.write("Name : Mohan \n")
f.write("COurse : Data Analyst \n")
f.write("Python Module : FIle handeling \n")
f.close()

print("Data is written successfully!")
print("-----------------------------")
f=open("students_data.txt","r")
contents = f.read()
print(contents)

f.close()

#------------------------------------------------------------
#copy from one file to other file 
file1 = open("students_data.txt","r")
file2 = open("copiedfile.txt","w")

file2.write(file1.read())
file1.close()
file2.close()

#------------------------------------------------------------------------
file = open("students_data.txt","a+")
#"a+" : append + read 

file.write("\n this is append+ contents \n")

print("-----------------------")
contents = file.read()
print(contents)

print("-----------------------")
file.seek(0)
print(file.read())
file.close()
