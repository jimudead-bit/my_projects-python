grades = {'Abbas': 91, 'Isa': 85, 'Zulaikha': 70}

while True:
    print()
    print("========== Student Grade Book ==========")
    print("1. Add student")
    print("2. View student names")
    print("3. View students' grades")
    print("4. Search student")
    print("5. Update grade")
    print("6. Delete student")
    print("7. Exit")

    choice = input("Enter your choice (use only numbers): ").strip()

    if choice == "1":
        name = input("Enter student name: ").strip().title()
        try:
            grade = int(input("Enter grade: ").strip())
        except ValueError:
            print("Invalid grade. Please enter a number.")
        else:
            grades[name] = grade
            print(f"{name} added with grade {grade}.")

    elif choice == "2":
        for student in grades:
            print(student)

    elif choice == "3":
        for student, grade in grades.items():
            print(f"{student} : {grade}")

    elif choice == "4":
        name = input("Enter student name: ").strip().title()
        if name in grades:
            print(f"{name}'s grade is {grades[name]}")
        else:
            print("Student is not in the grade book.")

    elif choice == "5":
        name = input("Enter student name: ").strip().title()
        if name in grades:
            try:
                new_grade = int(input("Enter updated grade: ").strip())
            except ValueError:
                print("Invalid grade. Please enter a number.")
            else:
                grades[name] = new_grade
                print(f"{name}'s grade updated to {new_grade}.")
        else:
            print("Student is not in the grade book.")

    elif choice == "6":
        name = input("Enter student name: ").strip().title()
        if name in grades:
            del grades[name]
            print(f"{name} has been deleted.")
        else:
            print("Student is not in the grade book.")

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Choice does not exist")

    print()
    input("Press Enter to continue...")

print()
input("Press Enter to exit...")
