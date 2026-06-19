#Recursion-function calls itself repeatedly
def show(n):
    #wanna print , n-1, then

    #step2: stop point return control #base case
    if(n==0):
        return


    #step1: what func have to do
    print(n)
    show(n-1)#for (show(n=4, then n=3 and so on))
    
show(5)

#call stack , function calls one after other
#when base case hit , n=0, call end its deleted and back to previous call stack 

#if no base case: infinite loop

#factorial
#fact(n)=fact(n-1)*n
#fact(n-1)=fact(n-2)*n-1
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
         return n*fact(n-1)


   