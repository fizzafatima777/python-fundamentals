#To reduce the redundancy
#to define function: def
def calc_sum(a,b):#passing parameters
    sum=a+b
    print(sum)
    return sum

#or 
def calc_sum2(a,b):
    return a+b

sum2=calc_sum2(2,5)
print(sum2)
#calling func(e.g our maid)
calc_sum(2,3)#passing arguments

#if function return nothing, you try to call it inside print
#None will be return

def calc_avg(a,b,c=0):
    sum=a+b+c
    avg=sum/3
    print (avg)
    return avg

#Types:
#user defined, which we made
#built in : print(),len(),type(),range()

#default values if passed to parameter , then in function call
#if arguments is nit passed, no error , it will take default value

#e.g=> calc_avg(2,3), c value is used default

#print length of list
cities=["lhr","karachi","popopo"]
def print_len(list):
    print(len(list))
    #any list length can be printed 

def print_element(list):
    for item in list:
        print(item,end=" ")#to print in 1 line

print_element(cities)

#factorial
def calc_factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    print(fact)

calc_factorial(5)
