name = input("Enter the name of the candidate: ")
experience = int(input("Enter the years of experience: "))

print(f"{name} has {experience} years of experience")

if experience >= 3:
    print("The candidate is eligible for the job")
else:
    print("the candidate is not eligible for the job")
    
    for i in range(3):
        name = input("Enter the name of the candidate: ")
    
while True:
    print("\n1. Add Candidate")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Adding candidate...")
    elif choice == "2":
        break
        