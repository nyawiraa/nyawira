class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}  

    def add_grade(self, unit, grade):
        self.grades[subject] = grade

    def get_average_grade(self):
        if grades not in self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

class Classroom:
    def __init__(self):
        self.students = []  

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added successfully.")

    def display_all_students(self):
        if student not in self.students:
            print("No students found.")
        else:
            for student in self.students:
                print(f"Student Name: {student.name}, Grades: {student.grades}")

    def get_student_average(self, student_name):
        for student in self.students:
            if student.name == student_name:
                average = student.get_average_grade()
                print(f"Average grade for {student.name}: {average:.2f}")
                return
        print(f"No student found with the name {student_name}.")

    def get_class_average_for_subject(self, unit):
        total_grades = 0
        count = 0
        for student in self.students:
            if subject in student.grades:
                total_grades += student.grades[unit]
                count += 1
        if count == 0:
            print(f"No grades found for subject {unit}.")
        else:
            class_average = total_grades / count
            print(f"Class average for {unit}: {class_average:.2f}")

def main():
    classroom = Classroom()

    student1 = Student("Mercy")
    student1.add_grade("Graphic Design", 90)
    student1.add_grade("Networking", 85)

    student2 = Student("Cosmas")
    student2.add_grade("Graphic Design", 80)
    student2.add_grade("Networking", 88)

    classroom.add_student(student1)
    classroom.add_student(student2)

    print("Displaying all students:")
    classroom.display_all_students()

    print("Getting average grade for Mercy:")
    classroom.get_student_average("Mercy")

    print("Getting class average for Graphic Design:")
    classroom.get_class_average_for_unit("Graphic Design")

if __name__ == "__main__":
    main()