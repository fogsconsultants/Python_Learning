#lower
text = "Hello, World!"
print(text.lower())
#upper
text = "Hello, World!"
print(text.upper())
#count
text = "Hello, World!"
print(text.count("l")) 
#partition
text = "Hello, World!"
print(text.partition(",")) 
#format # f string is much easier to use than format
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")
#strip
text = "   Hello, World!   "
print(text.strip())
#capitalize
text = "hello, woRLd!"
print(text.capitalize())
#Swapcase
text = "Hello, World!"
print(text.swapcase())
#Split
text = "Hello, World!" 
print(text.split(","))
#index
text = "Hello, World!"
print(text.index("W"))
#boolean
text = "HelloWorld2000"
print(text.isalnum())

text = "HelloWorld"
print(text.isalpha())

text = "19992000"
print(text.isdigit())

text = "2000"
print(text.isdecimal())