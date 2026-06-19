#files
#text file: .txt,.docx files
#binary: mp4,.pn.jpeg

#open, read, close
#open=> open("filename", mode(read/write)? by default is read mode)

f=open("demo.txt","r")
#by default bianry file operned, for bianry write "rb"e
# + read and writ
#if file is not right there , copy whole path
data=f.read()
data2=f.read(5)#to read 5 character
#enters the file
print(type(data))
print(data)
f.close()

#read one line
f=open("demo.txt","r")
line1=f.readline()
print(line1)

line2=f.readline()
print(line2)
#pointer at last at \n charcter
f.close()

#writing-> writing modes
#if file not created it will be self created
#w -> overwrite
#a append at end

f=open("demo.txt","w")
f.write("I wanna learn something new")
#\n should be given by yourself if you want to append line in new line
#  
f.close()

#r+ mode -? read +write and no truncation instead overwrite
# #pointer at start from starting

f=open("demo.txt","r+")
f.write("abc")
print(f.read())
f.close()

#w+ read and write and truncate-> complete wipe out
#a+ mode , read and append)pointer at end

#with syntax
with open("demo.txt","r") as f:
    data=f.read()
    print(data)
    #file automatically closed

#deleting file
#lets import a module
import os
#pip->package install for python (which packages are not install you can install using them thsi)

os.remove("sample.txt")

