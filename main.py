from student_ops import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student,
)


def main():
    while True:
        print("\nStudent Management System")
        print("1. Add student")
        print("2. View students")
        print("3. Search student by ID")
        print("4. Update student")
        print("5. Delete student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
