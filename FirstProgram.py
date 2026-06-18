print("Hello World")
print(23)

#Operations also allowed in it
print(1+2)

#Comma separted text will still be on same line
print("My name is fizza", "I am a passionated girl")

#variables(var=value)
#using assignment opertaor
name="fizza"
age=20
cgpa=3.5
cgpa2=cgpa

print("My name is:",name, "My age is: ",age,"My cgpa is:" ,cgpa)

#types
print(type(name))

#way to write strings
name1='sk'
name2="sk2"


old=True
new=False
a=None

print(type(old))
print(type(a))

#python is a case sensitive language e.g False, not false

#function of sum

a=100
b=200
sum=a+b
print(sum)

#triple code -- multi line comment

# Arithmetic Operators (+, -, *, /, %, **)
# plus
# minus
# multiply
# divide
# modulus
# exponent a**b=a^b

# Relational / Comparison Operators (==, !=, <, <=, >=, >)
# equals to
# not equals to
# less than
# less than or equal to
# greater than or equal to
# greater than

# Assignment Operators (=, +=, -=, *=, /=, %=, **=)
# assign
# add and assign
# subtract and assign
# multiply and assign
# divide and assign
# modulus and assign
# exponent and assign

# Logical Operators (not, and, or)
# not
# and
# or

print(not(a<b))

val1=True
val2=True
print (val1 and val2)

#Type conversion(type conversion(automatic), type casting(manyually))

a=2
b=4.25
sum=a+b
#int type converted automatically to int

print(sum)

#but string and int are not type converted
a,b=1,"2"
b=int(b)
print(a+b)

a=3
a=str(3)

#Take input:: input() output is always in string you acn type cast it
"""name=input("Entre your Name  :")
print("Welcome",name)
"""

#wrong , abc type string int mai shift nhi hoti , if ypu want to convert 23 received as string converted to int 
"""name3=int(input("Entre your Name  :"))
print("Welcome",name3)
print (type(name3))
"""

#final practice
#for strings concatenation
first=input("Entre first: ")
second=input("Entre second:")
sum2=first+second
print(sum2)

a=float(input("Entre first: "))
b=float(input("Entre second:"))
sum2=a+b
print((sum2)/2)

aa=10
bb=20
print(aa>bb)
