class GradingStudents:
    def __init__(self, grades):
        self.grades = grades

    def round_grades(self):
        rounded_grades = []
        for grade in self.grades:
            if grade < 38 or grade % 5 < 3:
                rounded_grades.append(grade)
            else:
                rounded_grades.append(grade + (5 - (grade % 5)))
        return rounded_grades


if __name__ == '__main__':
    num_students = int(input("Enter the number of students: "))
    grades = []
    for i in range(num_students):
        grade = int(input("Enter the grade of student {}: ".format(i + 1)))
        grades.append(grade)

    gs = GradingStudents(grades)
    rounded_grades = gs.round_grades()
    print("Rounded grades: ", rounded_grades)
