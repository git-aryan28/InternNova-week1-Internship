students = []
while True:
    print("\nstudent record management")
    print("1. add student")
    print("2. display students")
    print("3. search student")
    print("4. delete student")
    print("5. exit")
    choice = int(input("enter choice: "))
    if choice == 1:
        name = input("enter name: ")
        age = int(input("enter age: "))
        branch = input("enter branch: ")
        student = {
            "name":name,
            "age":age,
            "branch":branch
        }
        students.append(student)
        print("Student added successfully.")
    elif choice == 2:
        print("\nStudent Records")
        if len(students) == 0:
            print("No records found.")
        else:
            for student in students:
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Branch:", student["branch"])
                print()
    elif choice == 3:
        name = input("Enter name to search: ")
        found = False
        for student in students:
            if student["name"].lower() == name.lower():
                print("Student found!")
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Branch:", student["branch"])
                found = True
        if found == False:
            print("student not found.")

    elif choice == 4:
        name = input("enter name to delete: ")
        for student in students:
            if student["name"].lower() == name.lower():
                students.remove(student)
                print("deleted successfully.")
                break
        else:
            print("student not found.")
    elif choice == 5:
        print("thank you!")
        break
    else:
        print("invalid choice.")