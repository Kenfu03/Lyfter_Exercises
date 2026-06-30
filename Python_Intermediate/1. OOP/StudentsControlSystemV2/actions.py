from models import Student
import inputs
import data
import os
import models


SUBJECT_LIST = ["Spanish grade", "English grade", "Humanities grade", "Science grade"]


def check_csv_path():
    if not os.path.isfile("csv_path.txt"):
        print("\nFirst time here. Please add the next information.")
        data.write_txt_file(inputs.ask_for_csv_path("work with:"))
    return data.read_txt_file()


def change_csv_path():
    return data.write_txt_file(inputs.ask_for_csv_path("work with:"))


def choose_option():
    return inputs.ask_option()


def find_student_index(new_student, data):
    for index, student in enumerate(data):
        if (
            student.name == new_student.name
            and student.section == new_student.section
        ):
            return index

    return None


def add_student(data):
    while True:
        name = inputs.ask_name()
        print(f"\n -> {name}")

        new_student = Student(name, inputs.ask_section())

        if find_student_index(new_student, data) is None:
            break

        print("Student already exists.")

    for subject in Student.SUBJECTS:
        new_student.add_grade(subject, inputs.ask_grade(subject))

    return new_student


def add_students(file_path, old_data):
    n_students = inputs.ask_how_many_students()
    new_students : list[models.Student] = []

    for i in range(1, n_students+1):
        print(f"\nPlease add the information for the student number {i}: ")
        new_students.append(add_student(old_data))

    old_data = old_data + new_students
    data.write_students(file_path, old_data)
    print("\nStudent successfully included.")


def charge_data(file_path):
    if not os.path.isfile(file_path):
        return []
        
    return data.read_students(file_path)


def check_none(student, key):
    return student.grades.get(key) is not None


def show_dict_information(data : list[Student], title):
    print("\n" + title)

    for student in data:
        print(f"\n - {student.name} in section {student.section}")

        for subject in Student.SUBJECTS:

            if check_none(student, subject):
                print(f"{subject}: {student.grades.get(subject)}")


def find_top_3_student(data, key_to_find):
    print("\nTop 3 students in the system")
    sorted_data : list[Student] = sorted(data, key=lambda student: student.get_average(), reverse=True)
    for student in sorted_data[:3]:
        print(f"\n - {student.name} in section {student.section}")
        print(f"Grade average: {student.get_average()}")


def calculate_general_avg(data):
    group_size = len(data)
    avg_grades_sum = 0

    for student in data:
        avg_grades_sum += float(student.get_average())
    return avg_grades_sum / group_size


def find_disapproved_students(data : list[Student], minimum_grade):
    disapproved_students_list : list[Student] = []
    for student in data:
        aproved = True

        disapproved_student = Student(student.name, student.section)

        for subject in Student.SUBJECTS:
            if float(student.grades[subject]) < minimum_grade:
                disapproved_student.add_grade(subject, student.grades[subject])
                aproved = False

        if not aproved:
            disapproved_students_list.append(disapproved_student)

    return disapproved_students_list


def delete_student(file_path, students_list):
    print("\nPlease add the information of the student to delete.")
    name = inputs.ask_name()
    print(f"\n -> {name}")

    student_to_delete = Student(name, inputs.ask_section())

    index = find_student_index(student_to_delete, students_list)

    if index is not None:
        show_dict_information([students_list[index]], "Do you want to delete...")
        if input("\nY/N: ").lower() == "y":
            print("Student successfully removed.")
            del students_list[index]
            data.write_students(file_path, students_list)
        else:
            print("Student not deleted!")
    
    else:
        print("Student not found in the system!")
    return


def import_csv_file(path):
    while True:
        current_data = charge_data(path)
        import_path = inputs.ask_for_csv_path("import:")
        imported_data = charge_data(import_path)

        if not imported_data:
            print(f"'{import_path}' may not exist or may be empty.")
            continue

        data.write_students(path, current_data + imported_data)
        break