
#check two strings are anagram
str1 = list(input ("Enter the string 1: ").lower())#"Listen"
str2 = list(input ("Enter the string 2: ").lower())#"Silent"

is_anagram=True
if len(str1)==len(str2):
    for k in str1:
        if k in str2:
            str2.remove(k)
              
        else:
            is_anagram=False 
            break
    
    if is_anagram:
        print("Two strings are anagram")
else:
    print("Two strings are not anagram")