#append() method is used to add an element at the end of the list.
"""
ml=['kochi', 12, 'one team']
ml.append('kerala')
print(ml)

#extend() method is used to add multiple elements at the end of the list.
ml=['kochi', 12, 'one team']
ml.extend(['kerala', 'Fzee', 2024])
print(ml)

#Clear() method is used to remove all the elements from the list.
ml=['kochi', 12, 'one team']
ml.clear()
print(ml)


#Count() method is used to count the number of occurrences of an element in the list.
ml=['kochi', 12, 'one team', 'kerala', 'Fzee', 2024]
count = ml.count('Fzee')
print(count)


#index() method is used to find the index of the first occurrence of an element in the list.
ml=['kochi', 12, 'one team', 'kerala', 'Fzee', 2024]
index = ml.index('kerala')
print(index)

#insert() method is used to insert an element at a specific index in the list.
ml=['kochi', 12, 'one team']
ml.insert(1, 'kerala')
print(ml)

#pop() method is used to remove and return an element at a specific index in the list.
ml=['kochi', 12, 'one team', 'kerala', 'Fzee', 2024]
ml.pop(2)
print(ml)

#remove() method is used to remove the first occurrence of an element in the list.
ml=['kochi', 12, 'one team', 'kerala', 'Fzee', 2024]
ml.remove('kerala')
print(ml)

#reverse() method is used to reverse the order of the elements in the list.
ml=['kochi', 12, 'one team', 'kerala', 'Fzee', 2024]
ml.reverse()
print(ml)   

#sort() method is used to sort the elements in the list in ascending order.
ml=[5, 2, 9, 1, 3]
ml.sort()
print(ml)

ml=['kochi', 'one team', 'kerala', 'Fzee']
ml.sort()
print(ml)


#List Slicing is used to access a portion of a list by specifying the start and end indices.
ml=['kochi', 12, 'one team', 'kerala', 'Fzee', 2024]
print(ml[1:4])  # Output: [12, 'one team', 'kerala']
print(ml[:3])   # Output: ['kochi', 12, 'one team']
print(ml[3:6])  # Output: ['kerala', 'Fzee', 2024]  
print(ml[ : : 2])  # Output: ['kochi', 'one team', 'Fzee']
print(ml[-3:])  # Output: ['kerala', 'Fzee', 2024]
print(ml[ : : -1])  # Output: [2024, 'Fzee', 'kerala', 'one team', 12, 'kochi']
print(ml[-3:-6:-2])  # Output: ['kerala', 'one team']
print(ml[2:-6:-1]) # Output: ['Fzee', 'kerala', 'one team', 12]

"""
#List Comprehension is a concise way to create lists in Python.
a=[1, 2, 3, 4, 5, 9, 0, 8, 7, 6]
odd=[k for k in a if k % 2 != 0]
print(odd)

a=[1, 2, 3, 4, 5, 9, 0, 8, 7, 6]
even=[k for k in a if k % 2 == 0]
print(even)

