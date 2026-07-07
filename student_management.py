students = {}

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        students[roll] = {"Name": name, "Age": age}
        print("Student Added Successfully!")

    elif choice == "2":
        if students:
            print("\nStudent Records:")
            for roll, details in students.items():
                print(f"Roll No: {roll}, Name: {details['Name']}, Age: {details['Age']}")
        else:
            print("No student records found.")

    elif choice == "3":
        roll = input("Enter Roll Number to Search: ")
        if roll in students:
            print(students[roll])
        else:
            print("Student Not Found!")

    elif choice == "4":
        roll = input("Enter Roll Number to Update: ")
        if roll in students:
            name = input("Enter New Name: ")
            age = input("Enter New Age: ")
            students[roll] = {"Name": name, "Age": age}
            print("Student Updated Successfully!")
        else:
            print("Student Not Found!")

    elif choice == "5":
        roll = input("Enter Roll Number to Delete: ")
        if roll in students:
            del students[roll]
            print("Student Deleted Successfully!")
        else:
            print("Student Not Found!")

    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid Choice! Please try again.")
