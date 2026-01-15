from data import read_students, write_students


def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")

    students = read_students()
    students.append(f"{student_id},{name},{age},{course}\n")
    write_students(students)

    print("Student added successfully!")


def view_students():
    students = read_students()

    if not students:
        print("No students found.")
        return

    print("\nAll Students:")
    for line in students:
        student_id, name, age, course = line.strip().split(",")
        print(f"ID: {student_id}, Name: {name}, Age: {age}, Course: {course}")


def search_student():
    search_id = input("Enter student ID to search: ")
    students = read_students()

    for line in students:
        student_id, name, age, course = line.strip().split(",")
        if student_id == search_id:
            print("\nStudent found:")
            print(f"ID: {student_id}")
            print(f"Name: {name}")
            print(f"Age: {age}")
            print(f"Course: {course}")
            return

    print("Student not found.")


def update_student():
    target_id = input("Enter student ID to update: ")
    students = read_students()
    updated_students = []
    updated = False

    for line in students:
        student_id, name, age, course = line.strip().split(",")

        if student_id == target_id:
            new_name = input(f"Name ({name}): ") or name
            new_age = input(f"Age ({age}): ") or age
            new_course = input(f"Course ({course}): ") or course

            updated_students.append(f"{student_id},{new_name},{new_age},{new_course}\n")
            updated = True
        else:
            updated_students.append(line)

    if updated:
        write_students(updated_students)
        print("Student updated successfully!")
    else:
        print("Student not found.")


def delete_student():
    target_id = input("Enter student ID to delete: ")
    students = read_students()
    updated_students = []
    deleted = False

    for line in students:
        student_id = line.strip().split(",")[0]
        if student_id == target_id:
            deleted = True
        else:
            updated_students.append(line)

    if deleted:
        write_students(updated_students)
        print("Student deleted successfully!")
    else:
        print("Student not found.")
