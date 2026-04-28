#access package -> module - > function

from my_package.mod1 import mod1, mod2
print(mod1.add(16,18))
print(mod2.is_even(18))

#access package - directly import the function
from my_package.mod2 import 