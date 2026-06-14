students = {}

while True:
    print("\n===== Student Record Management System =====")
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
        marks = input("Enter Marks: ")

        students[roll] = {
            "Name": name,
            "Marks": marks
        }

        print("Student Added Successfully!")

    elif choice == "2":
        for roll, details in students.items():
            print("\nRoll No:", roll)
            print("Name:", details["Name"])
            print("Marks:", details["Marks"])

    elif choice == "3":
        roll = input("Enter Roll Number to Search: ")

        if roll in students:
            print("Student Found")
            print(students[roll])
        else:
            print("Student Not Found")

    elif choice == "4":
        roll = input("Enter Roll Number to Update: ")

        if roll in students:
            students[roll]["Name"] = input("Enter New Name: ")
            students[roll]["Marks"] = input("Enter New Marks: ")
            print("Record Updated")
        else:
            print("Student Not Found")

    elif choice == "5":
        roll = input("Enter Roll Number to Delete: ")

        if roll in students:
            del students[roll]
            print("Record Deleted")
        else:
            print("Student Not Found")

    elif choice == "6":
        print("Thank You")
        break

    else:
        print("Invalid Choice")