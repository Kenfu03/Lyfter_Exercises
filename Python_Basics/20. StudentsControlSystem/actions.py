import inputs
import data
import os


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


def calculate_student_average(student : dict) -> float:
    grades_sum = 0

    for subject in SUBJECT_LIST:
        grades_sum += student.get(subject.lower())

    return grades_sum / 4


def find_student_index(new_student, data):
    for index, student in enumerate(data):
        if (
            student["name"] == new_student["name"]
            and student["section"] == new_student["section"]
        ):
            return index

    return None

def add_student(data):
    while True:
        name = inputs.ask_name()
        print(f"\n -> {name}")

        new_student : dict = {
            "name": name,
            "section": inputs.ask_section()
        }

        if find_student_index(new_student, data) is None:
            break

        print("Student already exists.")

    for subject in SUBJECT_LIST:
        new_student[subject.lower()] = inputs.ask_grade(subject)

    new_student["grades average"] = calculate_student_average(new_student)
    return new_student


def add_students(file_path, old_data):
    n_students = inputs.ask_how_many_students()
    new_students : list[dict] = []

    for i in range(1, n_students+1):
        print(f"\nPlease add the information for the student number {i}: ")
        new_students.append(add_student(old_data))

    old_data = old_data + new_students
    data.write_csv_file(file_path, old_data)
    print("\nStudent successfully included.")


def charge_data(file_path):
    if not os.path.isfile(file_path):
        return []

    return data.read_csv_file(file_path)


def check_none(item, key):
    return item.get(key) is not None


def show_dict_information(data : list[dict], title):
    print("\n" + title)

    for item in data:
        print(f"\n - {item.get("name")} in section {item.get("section")}")

        for subject in SUBJECT_LIST:

            if check_none(item, subject.lower()):
                print(f"{subject}: {item.get(subject.lower())}")

        if check_none(item, "grades average"):
            print(f"Grades average: {item.get("grades average")}")


def find_top_3_student(data, key_to_find):
    sorted_data : list[dict] = sorted(data, key=lambda student: student[key_to_find], reverse=True)
    return sorted_data[:3]


def calculate_general_avg(data):
    group_size = len(data)
    avg_grades_sum = 0

    for student in data:
        avg_grades_sum += float(student.get("grades average"))
    return avg_grades_sum / group_size


def find_disapproved_students(data : list[dict], minimun_grade):
    disapproved_students_list : list[dict] = []
    for student in data:
        aproved = True

        disapproved_student = {
                    "name": student.get("name"),
                    "section": student.get("section")
                }

        for subject in SUBJECT_LIST:
            actual_grade = float(student.get(subject.lower()))
            if actual_grade < minimun_grade:
                disapproved_student[subject.lower()] = actual_grade
                aproved = False

        if not aproved:
            disapproved_students_list.append(disapproved_student)

    return disapproved_students_list


def delete_student(file_path, students_list):
    print("\nPlease add the information of the student to delete.")
    name = inputs.ask_name()
    print(f"\n -> {name}")

    student_to_delete : dict = {
        "name": name,
        "section": inputs.ask_section()
    }

    index = find_student_index(student_to_delete, students_list)

    if index is not None:
        show_dict_information([students_list[index]], "Do you want to delete...")
        if input("\nY/N: ").lower() == "y":
            print("Student successfully removed.")
            del students_list[index]
            data.write_csv_file(file_path, students_list)
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

        data.write_csv_file(path, current_data + imported_data)
        break