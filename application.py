import csv

class Student:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.enrollments = []

class Course:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit
        self.enrollments = []

class Enrollment:
    def __init__(self, student_id, course_id, semester, grade=None):
        self.student_id = student_id
        self.course_id = course_id
        self.semester = semester
        self.grade = grade

def load_data():
    students = {}
    courses = {}

    with open('project_files/students.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) # skip header row
        for row in reader:
            id, name, email = row
            students[id] = Student(id, name, email)

    with open('project_files/courses.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) # skip header row
        for row in reader:
            id, name, credit = row
            courses[id] = Course(id, name, credit)

    with open('project_files/enrollments.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) # skip header row
        for row in reader:
            student_id, course_id, semester, grade = row
            enrollment = Enrollment(student_id, course_id, semester, grade)
            students[student_id].enrollments.append(enrollment)
            courses[course_id].enrollments.append(enrollment)

    return students, courses

def add_student(students):
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    email = input("Enter student email: ")
    students[id] = Student(id, name, email)

def enroll_student(students, courses):
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")
    semester = input("Enter semester: ")
    enrollment = Enrollment(student_id, course_id, semester)
    students[student_id].enrollments.append(enrollment)
    courses[course_id].enrollments.append(enrollment)

def grade_student(students):
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")
    semester = input("Enter semester: ")
    grade = input("Enter grade: ")
    for enrollment in students[student_id].enrollments:
        if enrollment.course_id == course_id and enrollment.semester == semester:
            enrollment.grade = grade
            break

def display_student(students):
    id = input("Enter student ID: ")
    student = students.get(id)
    if student:
        print(f"Name: {student.name}")
        print(f"Email: {student.email}")
        for enrollment in student.enrollments:
            course = courses.get(enrollment.course_id)
            if course:
                print(f"Course: {course.name}")
                print(f"Semester: {enrollment.semester}")
                print(f"Grade: {enrollment.grade or 'N/A'}")
    else:
        print("Student not found")

def display_course(courses):    
    id = input("Enter course ID: ")
    course = courses.get(id)
    if course:
        print(f"Name: {course.name}")
        print(f"Credit: {course.credit}")
        for enrollment in course.enrollments:
            student = students.get(enrollment.student_id)
            if student:
                print(f"Student: {student.name}")
                print(f"Semester: {enrollment.semester}")
                print(f"Grade: {enrollment.grade or 'N/A'}")
        else:
                print("Course not found")

students, courses = load_data()

while True:
    print("1. Add Student")
    print("2. Enroll Student to Course")
    print("3. Grade Student")
    print("4. Display Student")
    print("5. Display Course")
    print("0. EXIT")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student(students)
    elif choice == '2':
        enroll_student(students, courses)
    elif choice == '3':
        grade_student(students)
    elif choice == '4':
        display_student(students)
    elif choice == '5':
        display_course(courses)
    elif choice == '0':
        break
    else:
        print("Invalid choice")
