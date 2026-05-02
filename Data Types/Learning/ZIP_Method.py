#ZIP Method in Python
#The zip() function in Python is used to combine two or more iterables (like lists, tuples, etc.) into a single iterable of tuples. Each tuple contains elements from the input iterables that are at the same position. The zip() function stops when the shortest input iterable is exhausted.
#Example 1: Zipping two lists together
name=["Alice", "Bob", "Charlie"]
marks=[85, 90, 78] 
for k, m in zip(name, marks):
    print(f"{k}= {m}")

