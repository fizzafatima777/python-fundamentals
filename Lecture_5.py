#loops
#while loop and for loop 

"""while True:#untill truth and truth is always truth
    print("Hello")"""

count=1
while count<=5:
    print("hello")
    count=count+1
print (count)

i=5
while i>=1:
    print(i)
    i=i-1

j=1
while j<=100:
    print(j)
    j=j+1

#multiplication table:
tableOf=2
value=1
counter=1
while(counter<=10):
    print(tableOf,"*",value, "=",tableOf * value)
    counter+=1
    value+=1
#q4 print all these elemnts of list
nums=[1,4,9,16,25,36,49,64,81,100]

idx=0
while idx<(len(nums)):
    print(nums[idx])
    
    idx+=1


#q5 search

nums2 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36
j = 0
while j < len(nums2):
    if(nums2[j] == x):
        print("found at idx", j)
        break
    #if we dont use break here, even after finding value the else will continue untill loop not neded
    else:
        print("finding")
    j = j + 1 


#break and continue
#to terminate loop: break

k=1
while(k<=5):
    
    print(k)
    if(k==3):
        break
    
    k=k+1

#continue
#just terminate the current iteration and goes on further
l=0
while l<=5:
    if(l==3):
        l+=1
        continue
    print(l)
    l+=1

#for loop :: ssequential traversal we dont wanna go into using index
list1=[1,2,3,4,5]
for val in list1:
    print(val)

veggies=["potatoes","brinjal","ladyfinder","cucumber"]
for val in veggies:
    print(val)

tup=(1,2,3)
for numo in tup:
    print(numo)

str="goodgirl"
for char in str:
    if(char=='o'):
        print("o found")
        break
    print(char)
else:#optional
    #but it is not executed in case of break
    print("end")


#practice
nums3=[1,4,9,16,25,36,49,64,81,100]
for val in nums3:
    print(val)
y=81
idx=0
tup2=(1,4,9,16,25,36,49,64,81,100)
for val in tup2:
    if(val==y):
        print("found at idx ",idx)
        idx+=1
    
#Range()
#range(start,stop,stepsize)
#returns a sequence like a list

print(range(0,5))

seq=range(5)
print(seq[3])

for i in seq:
    print(i)

for i in range(2,10):#range(start,end) start included, stop not 
    print(i)

for i in range(4,10,2):
    print(i)

for i in range(1,100,2):
    print(i)#even numbers

#print from 1-100
for i in range(1,101):
    print(i)

#pass statement =null statement
#to write loop in which we have to done nothing but run loop

for i in range(5):
    pass
#means no work in loop ,like a placeholder for future code

#find sum of first n numbers

n=5
sum=0
for i in range(1,n+1):
    sum=sum+i
print("sum=",sum)


#factorial
m=5
factorial=1
while(i<=5):
    factorial*=i
    i+=1
print(factorial)