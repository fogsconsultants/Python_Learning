#Set Methods in Python
#A set is an unordered collection of unique elements. Sets are mutable, meaning you can add or remove elements from a set after it has been created. Here are some common set methods in Python:
#repetition of elements is not allowed in sets. If you try to add a duplicate element, it will be ignored.

"""#add() method is used to add an element to the set.
s = {1, 2, 3}
s.add(4)
print(s)

#remove() method is used to remove an element from the set. If the element is not present, it raises a KeyError.
s = {1, 2, 3}
s.remove(5)
print(s)

#discard() method is used to remove an element from the set. If the element is not present, it does nothing.
s = {1, 2, 3}
s.discard(5)
print(s)

#intersection() method is used to get the common elements between two sets.
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1.intersection(s2))

#pop() method is used to remove and return an arbitrary element from the set. If the set is empty, it raises a KeyError.
s = {1, 2, 3}
print(s.pop())
print(s)
"""

#union() method is used to get all the unique elements from both sets.
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1.union(s2))

#difference() method is used to get the elements that are present in one set but not in the other.
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1.difference(s2))
