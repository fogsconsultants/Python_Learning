
"""
if condition:
    statements
else:
    statements


age=18
if age>=18:
    print("Eligible to Vote")
else:
    print("Not eligible to Vote")


age=int(input("Enter your age : "))
if age>=18:
    print("Eligible to Vote")
else:
    print("Not eligible to Vote")



num=int(input("Enter the number : "))
if num%2==0:
    print(num, "is an even number")
else:
    print(num, "is an Odd number")

    #else if

a=int(input("Enter the First number : "))
b=int(input("Enter the Second number : "))
print("1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Dvision")
choice=int(input("Enter your choice : "))
if choice==1:
    print("Sum =", a+b)
elif choice==2:
    print("Subtract =", a-b)
elif choice==3:
    print(f"{a} * {b} = {a*b}")
elif choice==4:
    print((f"{a} / {b} = {a/b}"))
else:
    print("Invalid input, Please enter the value 1, 2, 3, 4")

    
    """
#Match - Case

a=int(input("Enter the First number : "))
b=int(input("Enter the Second number : "))
print("1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Dvision")
choice=int(input("Enter your choice : "))
match choice:

    case 1:
        print("Sum =", a+b)
    case 2:
        print("Subtract =", a-b)
    case 3:
        print(f"{a} * {b} = {a*b}")
    case 4:
        print((f"{a} / {b} = {a/b}"))
    case _:
        print("Invalid input, Please enter the value 1, 2, 3, 4")