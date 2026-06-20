total_grades = 0
total_approved = 0
total_desapproved = 0
approved_counter = 0
desapproved_counter = 0

grades_counter = int(input("Enter the number of grades to calculate: "))

for i in range(1, grades_counter + 1):
    grade = int(input(f"Enter the grade number {i}: "))
    total_grades += grade
    if grade >= 70:
        total_approved += grade
        approved_counter += 1
    else:
        total_desapproved += grade
        desapproved_counter += 1

print(f"""The total of approved grades is {approved_counter}
The total of desapproved grades is {desapproved_counter}
The average is {total_grades/grades_counter}
The average of approved grades is {total_approved/approved_counter if approved_counter > 0 else 0}
The average of desapproved grades is {total_desapproved/desapproved_counter if desapproved_counter > 0 else 0}
""")