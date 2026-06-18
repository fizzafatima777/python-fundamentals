#Dictionairies and sets
#like word meaning pair , word is a key of pair , meaning is value, key:value
dict={
    "key":"value",
    "topics":("dict","set"),
    "name":"ikpictic",
    "cgpa":3.5,
    "age":20
    #key can be a float value,e.g 12.99:12
}
print(dict)

#no index in dict , so unoredered, mutable, dupliacte keys not allowed

#accessing specific values of dictioanry 
# dictionary name[key], and if something not exist and you try to access it, error ajaye ga 
print(dict["name"])

dict["name"]="new name"#overwrite
print(dict["name"])
#when youa assign then you can use print statement to check if its is assigned, not before this


#empty dictioanry acn also be created
null_dict={}
null_dict["name"]="new name"#assigning values

#Nestedness in dictioanory:: make key a dictioanry
student={
    "name":"aliptic",
    "subjects":{
        "math":99,
        "chem":98
    }

}
print(student["subjects"]["chem"])

#methods
#return all keys
print(dict.keys())
#internal nested keys not returned , just outer layer keys return, 

#we acn typecast it to list
print(list(student.keys()))
print(len(list(student.keys())))

#same for values 
print(dict.values())

#return all pairs
pairs=list(student.items())
print(pairs[0])
print(student.items())

#.get to get the value of specific key more better than simple access dict["key"] if not exist it will give error
print(dict.get("key"))

#update:: to add new dictioanry , new key value pairs
student.update({"lolo":"popopo"})
print(student)

#if we pass same key with diff value in new dict the in the same key value is updated 







#SETS - immutable string, tuples can be stored in them, dict and list can't(bcz they are immutable)
collection={1,2,3,"abc"}
print(collection)

#if something dupliacted, set ignore it, bcz set is always unique, set is unordered
#list.dict are un hashable

print(len(collection))

collection2={}#but its empty dict not empty set

collection3=set()
print(type(collection3))

#add(el) , remove(el), clear(), pop()
#pop -random values poped
collection.add(12)
collection.remove(1)

#set is mutable but elemnts immutable, means list and dict not passed
#if you passed something that not exist in set , its error

#union and intersection methods

set1={1,2,3}
set2={4,5,2}

print(set1.union(set2))#no dupliacte values just unique

#intersection-common elemnts

#practice questions
dict2={
    #2 values are stored in lsit or tuple
    "table":["a piece of furniture" "list of fact and figures"],
    "cat":"a small animal"

}

#count of unique values? store in set
subjects={"python","java","c++","c","java"}
print(subjects)

marks={}
x=int(input("entre phy: "))
y=int(input("entre chem: "))

marks.update({"phy":x})