#Shallow Copy and Deep Copy in Python
#In Python, a shallow copy creates a new object but does not create copies of nested objects. # Instead, it references the original nested objects. 
# A deep copy creates a new object and recursively copies all nested objects, resulting in a completely independent copy.

import copy


l=[1, 2, [3, 4], 5]
new_l=copy.copy(l) #or new_l=list(l) # Sahllow Copy


l=[1, 2, [3, 4], 5]
new_l=copy.deepcopy(l) #or new_l=list(l)


new_l[2][0]=10
print(l) # Output: [1, 2, [3, 4], 5]
print(new_l) # Output: [1, 2, [10, 4], 5]
