
#Dictionary methods
d1 = {"name":"John", "age":30, "city":"New York"}
print(d1)

#clear() method is used to remove all the elements from the dictionary.
d1 = {"name":"John", "age":30, "city":"New York"}   
d1.clear()
print(d1)

#fromkeys() method is used to create a new dictionary with the specified keys and values.
my_dict = ('name','age','city')
d=dict.fromkeys(my_dict)
d['name'] = 'John'
d['age'] = 30               
d['city'] = 'New York'
print(d)

#get() method is used to get the value of a specific key in the dictionary.
d1 = {"name":"John", "age":30, "city":"New York"}
print(d1.get("name"))

#items() method is used to get a view object that displays a list of dictionary's key-value tuple pairs.
d1 = {"name":"John", "age":30, "city":"New York"}
print(d1.items())

#keys() method is used to get a view object that displays a list of all the keys in the dictionary.
d1 = {"name":"John", "age":30, "city":"New York"}
print(d1.keys())

#values() method is used to get a view object that displays a list of all the values in the dictionary.
d1 = {"name":"John", "age":30, "city":"New York"}  
print(d1.values())

#pop() method is used to remove and return the value of a specific key in the dictionary.
d1 = {"name":"John", "age":30, "city":"New York"}
d1.pop("age")
print(d1)

#popitem() method is used to remove and return an arbitrary key-value pair from the dictionary.
d1 = {"name":"John", "age":30, "city":"New York"}
d1.popitem()
print(d1)

#update() method is used to update the dictionary with the key-value pairs from another dictionary.
d1 = {"name":"John", "age":30, "city":"New York"}
d2 = {"name":"Alice", "age":25, "city":"Los Angeles"}
d1.update(d2)
print(d1)


#setdefault() method is used to get the value of a specific key in the dictionary. If the key does not exist, it inserts the key with a specified value.
d1 = {"name":"John", "age":30, "city":"New York"}
print(d1.setdefault("country", "USA"))
print(d1)



