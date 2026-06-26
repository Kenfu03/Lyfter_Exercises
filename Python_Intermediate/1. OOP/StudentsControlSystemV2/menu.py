from models import Student
import actions

REQUIRES_DATA = {2, 3, 4, 5, 6}


def print_menu():
    print("""1. Add students
2. View all students
3. Top 3 students
4. General average grade
5. Show disapproved studentss
6. Delete student
7. Import students using csv file
8. Change csv file to work with
9. Exit""")


def options_menu():
    while True:
        print("\n\tWelcome to the student System.")
        file_to_work = actions.check_csv_path()
        print(f"The file we gonna work with is '{file_to_work}'\n")
        print_menu()
        
        data = actions.charge_data(file_to_work)
        menu_option = actions.choose_option()

        if menu_option in REQUIRES_DATA and not data:
            print("\nThere are no students. Please add or import students first.")
            continue

        match (menu_option):
            case (1):
                actions.add_students(file_to_work, data)
                continue
            case (2):
                actions.show_dict_information(data, "Students in the system")
                continue
            case (3):
                top_3 = actions.find_top_3_student(data, "grades average")
                continue
            case (4):   
                print("\nGeneral average grade")
                general_avg = actions.calculate_general_avg(data)
                print(f"The average in the whole group is: {general_avg}")
                continue
            case (5):
                disapproved_students : list[Student] = actions.find_disapproved_students(data, 60)
                actions.show_dict_information(disapproved_students, "\nDisapproved students")
                continue
            case (6):
                actions.delete_student(file_to_work, data)
                continue
            case (7):
                actions.import_csv_file(file_to_work)
                continue
            case (8):
                actions.change_csv_path()
            case (9):
                print("Thanks for use our students system!, bye.")
                return False
    