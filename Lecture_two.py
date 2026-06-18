#Strings 
str1="this is a apstrophe's used string"
str2="this contains a newline. \n an escape sequence used here"

#concatenation(but no space in bw them)
str1="Conactenated string part1 "
str2="concatenated string part2"
print(str1+str2)

#length of string
print(len(str1))

final_str=str1+" "+str2
print(len(final_str))

#indexing  when string created indexes assign per character str[0]=first cahracter
#index help us to access particular character

# but just access no manipulation
str3="apnacollge"
print(str3[1])

#slicing(the piece in middle  str[starting index: ending index])
#last index not included

print(str3[0:4])
print(str3[5:len(str3)])
print(str3[:4])#python automatically fill it with 0 

#backward counting minus mai start hoti hai apple(-5,-4,-3,-2,-1) last index is -1 , first index is -5 
str4="apple"
print(str4[-5:-1])

#string functions
str5="I am a coder"

#endwith
print(str5.endswith("er"))

#capitalize first letter , moreover original string is not modified new string created
print(str5.capitalize())

#to modify originak string
str5=str5.capitalize()


#replace this with this
print(str5.replace("a","o"))

#find to search word in string, if exist , return first index of first occurence
str6=" I am studying python from apna college"
print(str6.find("o"))
print(str6.find("python"))


#print first name and write its length 
name=input("Entre your first name: ")
print("length of your name is: ",len(name))

str7="Hi I $am  a  symbol $99"
print(str7.count("$"))

#Conditional statement (if-elif-else)
age=23
if(age==18):
    print("Apply for license")
elif(age<18):
    print("wait now")
else:
    print("you are too aged now, take license")
# you can end with elif also , else is not compulsory but elif(condition)
#if is always checked /executed, but elif if become true then stops checking further


marks=70
if(marks>=90):
    grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="C"
else:
    grade="D"

print("grade is: ",grade)




#checking odd or even
number=int(input("Entre a number either even or odd: "))
if(number%2==0):
    print("number is even")
else:
    print("number is odd")



#checking the number is multiple or not
x=int(input("Entre a number to check its multiple of 5 or not : "))
if(x%5==0):
    print("multiple of 5")
else:
    print("not multiple of 5 ")
