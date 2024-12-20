
class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

    def input_student_info():
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student DOB: ")
        return Student(student_id, name, dob)


class Course:
    def __init__(self, course_id, course_name):
        self.course_no = course_id
        self.course_name = course_name

    def input_course_info():
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        return Course(course_id, course_name)


class Mark:
    def __init__(self, mark, student, course):
        self.mark = mark
        self.student = student
        self.course = course

    def input_mark(students, course):
        marks = []
        for student in students:
            mark = float(input(f"enter mark for {student.name} in {course.course_name}: "))
            marks.append(Mark(mark, student, course))
        return marks


class School:
    def __init__(self):
        self.student = []
        self.course = []
        self.marks = []

    def input_student(self):
        number_student = int(input("Enter student number: "))
        self.students = [Student.input_student_info() for _ in range(number_student)]

    def input_course(self):
        number_course = int(input("Enter course number: "))
        self.courses = [Course.input_course_info() for _ in range(number_course)]

    def input_marks(self):
        for course in self.courses:
            print(f"Enter marks for {course.course_name} ")
            self.marks.extend(Mark.input_mark(self.students, course))

    def listings_students(self):
        for student in self.students:
            print(f"ID: {student.student_id}, Name: {student.name}, DOB: {student.dob}")

    def listings_courses(self):
        for course in self.courses:
            print(f"ID: {course.course_no}, Name: {course.course_name}")

    def show_marks(self):
        for course in self.courses:
            print(f"\nCourse: {course.course_name}")
            for student in self.students:
                mark_found = False
                for mark in self.marks:
                    if mark.course == course and mark.student == student:
                        print(f"{student.name}: {mark.mark}")
                        mark_found = True
                if not mark_found:
                    print(f"{student.name}: No marks")




def main():
    school = School()
    school.input_student()
    school.input_course()
    school.input_marks()
    # school.listings_students()
    # school.listings_courses()
    school.show_marks()

if __name__ == "__main__":
    main()