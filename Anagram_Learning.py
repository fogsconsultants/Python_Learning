
#check two strings are anagram
str1 = list(input ("Enter the string 1: "))#"Listen"
str2 = list(input ("Enter the string 2: "))#"Silent"



if len(str1)==len(str2):
    for i in str1:
        while i in str2:
            str2.remove (i)
        else:
            print("Two strings are not anagram")
        break
else:
    print("Two strings are not anagram")


