"""
number
int     age=28
float   p=3.14
complex c=7j

String  name="Ebin"
"""
age=28
print(type(age))

p=3.14
print(type(p))

c=7j
print(type(c)) 


name="Ebin"
print(name[2])      # name[] is used to accessing characters by index position

#String is immuatable, hence we cant change it

#list    mylist[] #list declare in [] also it is mutable

my_list=["One Team",2018,23.9,7]
my_list[2]=[9,'Ebin',23.9,7j] # [] is used to access/declare the index position

print(my_list[2][1])

#tuple

t=("Ebin", 12, 9,10,'python') #immutable #normal bracket #index position

#Set
s={12,'Ebin',78.23, 12, 'Python'}
print(s)   # unordered and will not allow duplicated

student={"name":"Ebin","age":"28",12:8, "hobbies":["Coding", "Travel","Reading"]}
print(student)
print(student["hobbies"][1])

#print(student["hobbies"][3])
student['place']="Kochi"
student["hobbies"]="Cycling", "Scuba"
print(student)
#boolean    is_active=True

