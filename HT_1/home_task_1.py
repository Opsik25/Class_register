class SchoolMember:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Student(SchoolMember):

    def __init__(self, name, surname, sex):
        super().__init__(name, surname)
        self.sex = sex
        self.courses_finished = []
        self.grades = {}
        self.courses_in_progress = []

    def add_courses_finished(self, course_finished_name):
        self.courses_finished.append(course_finished_name)

    def add_lucturer_grade(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course not in lecturer.grades:
                lecturer.grades[course] = [grade]
            else:
                lecturer.grades[course].append(grade)
        else:
            return 'Ошибка'


class Teacher(SchoolMember):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []


class Lecturer(Teacher):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


class Reviewer(Teacher):

    def add_student_grade(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course not in student.grades:
                student.grades[course] = [grade]
            else:
                student.grades[course].append(grade)
        else:
            return 'Ошибка'


student_1 = Student('Ivan', 'Ivanov', 'male')
student_1.courses_finished.append('Git')
student_1.courses_in_progress.append('Python')
student_1.grades['Git'] = [10, 10, 10, 10, 10]
student_1.grades['Python'] = [10, 10]

reviewer_1 = Reviewer('Viktor', 'Stepanov')
reviewer_1.courses_attached.append('Python')
reviewer_1.courses_attached.append('Git')

lecturer_1 = Lecturer('Tom', 'Tailor')
lecturer_1.courses_attached.append('Python')
lecturer_1.courses_attached.append('Git')
lecturer_1.grades['Git'] = [5, 5, 4, 7]
lecturer_1.grades['Python'] = [3, 10, 8]

reviewer_1.add_student_grade(student_1, 'Python', 7)
reviewer_1.add_student_grade(student_1, 'Python', 8)
reviewer_1.add_student_grade(student_1, 'Python', 6)

student_1.add_lucturer_grade(lecturer_1, 'Python', 5)
student_1.add_lucturer_grade(lecturer_1, 'Python', 10)
student_1.add_lucturer_grade(lecturer_1, 'Python', 10)

print(student_1.grades)
print(lecturer_1.grades)

