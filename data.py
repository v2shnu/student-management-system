FILE_NAME = "students.csv"


def read_students():
    students = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                students.append(line)
    except FileNotFoundError:
        pass
    return students


def write_students(students):
    with open(FILE_NAME, "w") as file:
        file.writelines(students)
