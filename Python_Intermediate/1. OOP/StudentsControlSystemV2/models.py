class Student:
    SUBJECTS = [
        "Spanish grade",
        "English grade",
        "Humanities grade",
        "Science grade"
    ]


    def __init__(self, name, section):
        self.name = name
        self.section = section
        self.grades = {}


    @classmethod
    def from_dict(cls, student_dict):
        student = cls(student_dict.get("name"), student_dict.get("section"))

        for subject in cls.SUBJECTS:
            grade = student_dict[subject.lower()]
            student.add_grade(subject, grade)

        return student


    def add_grade(self, grade_name, grade):
        self.grades[grade_name] = grade


    def get_average(self):
        average = 0
        for subject in self.SUBJECTS:
            average += float(self.grades.get(subject))
        return average / len(self.SUBJECTS)


    def to_dict(self):
        student_dict = {
            "name": self.name,
            "section": self.section,
        }
        for subject in self.SUBJECTS:
            student_dict[subject.lower()] = self.grades.get(subject)
        return student_dict

