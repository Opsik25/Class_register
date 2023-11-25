class Student:
    def __init__(self, name, surname, sex):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.courses_finished = []
        self.grades = {}
        self.courses_in_progress = []

    def add_courses_finished(self, course_finished_name):
        self.courses_finished.append(course_finished_name)


class Teacher:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def add_student_grade(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course not in student.grades:
                student.grades[course] = [grade]
            else:
                student.grades[course].append(grade)
        else:
            return 'Ошибка'

class Lecturer(Teacher):
    pass

class Reviewer(Teacher):
    pass


student_1 = Student('Ivan', 'Ivanov', 'male')
student_1.courses_finished.append('Git')
student_1.courses_in_progress.append('Python')
student_1.grades['Git'] = [10, 10, 10, 10, 10]
student_1.grades['Python'] = [10, 10]

teacher_1 = Teacher('Tom', 'Tailor')
teacher_1.courses_attached.append('Python')

teacher_1.add_student_grade(student_1, 'Python', 10)
teacher_1.add_student_grade(student_1, 'Python', 10)
teacher_1.add_student_grade(student_1, 'Python', 10)

print(student_1.grades)

