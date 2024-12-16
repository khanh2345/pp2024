def input_student_no(num):
    return int(input(num))
def input_student_info():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student DOB: ")
    return student_id, student_name, student_dob
def input_course_no(num):
    return int(input(num))
def input_course_info():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    return course_id, course_name
def input_mark(students, course):
    marks = {}
    for student in students:
        mark = float(input(f"enter mark for {student[1]} in {course} "))
        marks[student[0]] = mark
        return marks
def main():
    numbers_student = input_student_no("enter student no: ")
    students = [input_student_info() for _ in range(numbers_student)]
    number_courses = input_course_no("enter course no: ")
    courses = [input_course_info() for _ in range(number_courses)]
    courses_marks = {}
    for course in courses:
        print(f"entering mark for course:", course[1])
        courses_marks[course[1]] = input_mark(students, course)
if __name__ == "__main__":
    main()