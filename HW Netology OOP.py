# HomeWork-OOP

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grade_course_students(students, course):
        total_grade = 0
        count = 0
        for student in students:
            if course in student.courses_completed:
                grade = sum(student.grades[course]) / len(student.grades[course])
                total_grade += grade
                count += 1
        return round(total_grade / count, 1) if count else 0


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

print(Mentor.__dict__)


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}
        self.courses_attached = []

    def __str__(self):
        return f'{self.name} {self.surname}'

    def avg_grade_course_lecturers(lecturers, course):
        total_grade = 0
        count = 0
        for lecturer in lecturers:
            if course in lecturer.grades:
                grade = sum(lecturer.grades[course]) / len(lecturer.grades[course])
                total_grade += grade
                count += 1
        return round(total_grade / count, 1) if count else 0

class Reviewer(Mentor): # эксперты проверяющие домашние задания

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

print(Reviewer.__dict__)

student_sofi = Student('Sofi', 'Lis', 'women')
student_sofi.courses_in_progress += ['Python']
student_nik = Student('Nik', 'Lis', 'men')
student_nik.courses_in_progress += ['Java']

print(student_nik.__dict__)


lecture_oleg = Lecturer('Oleg', 'Buligin')
lecture_oleg.courses_attached += ['Python']
print(lecture_oleg.__dict__)

lecture_artem = Lecturer('Artem', 'Moskvin')
lecture_artem.courses_attached += ['Java']
print(lecture_artem.__dict__)

reviewer_andrey = Reviewer('Andrey', 'Gol')
reviewer_andrey.courses_attached += ['Python']
print(reviewer_andrey.__dict__)

reviewer_elena = Reviewer('Elena', 'Nikitina')
reviewer_elena.courses_attached += ['Java']
print(reviewer_elena.__dict__)

