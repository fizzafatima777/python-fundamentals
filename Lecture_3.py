#making lists
marks=[90,80,70,60,50]

#printing list
print(marks)

#list has same concept as string, indexing, its concept diff from array is that you can use diff datatypes things in array 
print(marks[0], marks[1])
print(len(marks))

#list concept diff from string is taht , we can manipulate list , but string cant be manipulated, just accesssed using index
marks[4]=0.0
print(marks)

#if you acces out of list index: error out of range

#slicing- same as string- ending index not included
print(marks[0:4])
print(marks[1:])

#also possible using negative indexes
print(marks[-3:-1])

#methods in list

marks.append(4)
print(marks)
print(marks.sort())
#sort function returns nothing actually list methods return nothing

print(marks)

#sorting in reverse order
marks.sort(reverse=True)

#string sorting done based on first smallest character and so on
list=["banana", "apple", "lichi"]
list.sort()
print(list)

list.reverse()
print(list)
 
#insert , just like append but at particular index list.insert(index,element)
list2=[2,1,3]
list2.insert(2,5)
print(list2)

#list2.remove(first occurence of taht element) or agr particular index sy value del krni ho list2.pop(2)
list2.remove(1)
list2.remove(3)
print(list2)

#search for python documentation if wanna learn more 


#tuple a built in datatype , but diff from list sas its immutable(can't maipulate) , list was mutable 
#tupel uses parenthesis cant assign something in it, empty tuple is also valid
tup=(1,2,3,4,5)
print(type(tup))
print(tup)
tup2=()

#single value tuple last coma is compulsory but for multi data(1,2,3,4) end coma is optional
tup3=(1,)
print(tup3)
print(tup[1:2])

print(tup.index(2))#2 ka index
print(tup.count(2))

#practice question
movie1=input("Entre movie1 name")
movie2=input("Entre movie2 name")
movie3=input("Entre movie3 name")

list4=[movie1,movie2,movie3]
print(list4)

#or make movies=[]
#then use movies.append
# or movies.append(input("entre movie 1"))

#check palindrome
#use copy() which make shallow copy and then reverse it , what about taht if original value=reversed value

pal1=[1,2,3,2,1]
pal2=pal1
pal2.reverse()
if(pal1==pal2):
    print("palindrome")
else:
    print("not palindrome")

#tupe practice
tup=("c","B","A","A")
print(tup.count("A"))