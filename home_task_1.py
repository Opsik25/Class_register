class SchoolMember:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __lt__(self, other):
        if ((isinstance(self, Student) and isinstance(other, Student) or
                isinstance(self, Lecturer) and isinstance(other, Lecturer)) and
                isinstance(self.avg_grade(), float) and isinstance(other.avg_grade(), float)):
            return self.avg_grade() < other.avg_grade()
        else:
            return 'Вы можете сравнить объекты только одного класса, у которых есть оценки'

    def __gt__(self, other):
        if ((isinstance(self, Student) and isinstance(other, Student) or
                isinstance(self, Lecturer) and isinstance(other, Lecturer)) and
                isinstance(self.avg_grade(), float) and isinstance(other.avg_grade(), float)):
            return self.avg_grade() > other.avg_grade()
        else:
            return 'Вы можете сравнить объекты только одного класса, у которых есть оценки'

    def __eq__(self, other):
        if ((isinstance(self, Student) and isinstance(other, Student) or
                isinstance(self, Lecturer) and isinstance(other, Lecturer)) and
                isinstance(self.avg_grade(), float) and isinstance(self.avg_grade(), float)):
            return self.avg_grade() == other.avg_grade()
        else:
            return 'Вы можете сравнить объекты только одного класса, у которых есть оценки'

    def avg_grade(self):
        if hasattr(self, 'grades'):
            if len(self.grades) > 0:
                self.__grades_list = []
                for el in self.grades.values():
                    self.__grades_list.extend(el)
                return round(sum(self.__grades_list) / len(self.__grades_list), 2)
            else:
                return f'У {self.name} {self.surname} пока нет оценок'
        else:
            return 'Оценки есть только у студентов и лекторов'


class Student(SchoolMember):

    def __init__(self, name, surname, sex):
        super().__init__(name, surname)
        self.sex = sex
        self.courses_finished = []
        self.grades = {}
        self.courses_in_progress = []

    def add_courses_finished(self, course_finished_name):
        self.courses_finished.append(course_finished_name)

    def add_lecturer_grade(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress and
                course in lecturer.courses_attached) and 0 < grade <= 10 and isinstance(grade, int):
            if course not in lecturer.grades:
                lecturer.grades[course] = [grade]
            else:
                lecturer.grades[course].append(grade)
            print('Оценка успешно добавлена')
        else:
            print('Ошибка. Проверьте правильность внесенных данных и попробуйте еще раз')

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.avg_grade()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.courses_finished)}")


class Teacher(SchoolMember):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []


class Lecturer(Teacher):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.avg_grade()}")


class Reviewer(Teacher):

    def add_student_grade(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached and
                course in student.courses_in_progress) and 0 < grade <= 10 and isinstance(grade, int):
            if course not in student.grades:
                student.grades[course] = [grade]
            else:
                student.grades[course].append(grade)
            print('Оценка успешно добавлена')
        else:
            print('Ошибка. Проверьте правильность внесенных данных и попробуйте еще раз')

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


def print_avg_student(students: list, course: str):
    """Print average grade for each given student"""
    grade_dict = {}
    for student in students:
        if isinstance(student, Student):
            if course in student.grades:
                grade_dict[f'{student.name} {student.surname}'] = (
                    round(sum(student.grades[course]) / len(student.grades[course]), 2))
            else:
                print(f"У студента {student.name} {student.surname} нет оценок "
                      f"по курсу {course}")
        else:
            print(f'Ошибка. {student.name} {student.surname} не является студентом')
    for name, avg_grade in grade_dict.items():
        print(f'Средняя оценка {name} по курсу {course}: {avg_grade}')


def print_avg_all_students(students: list, course: str):
    """Print average grade for all given students together"""
    grade_dict = {}
    for student in students:
        if isinstance(student, Student):
            if course in student.grades:
                grade_dict[f'{student.name} {student.surname}'] = (
                    round(sum(student.grades[course]) / len(student.grades[course]), 2))
            else:
                print(f"У студента {student.name} {student.surname} нет оценок "
                      f"по курсу {course}")
        else:
            print(f'Ошибка. {student.name} {student.surname} не является студентом')
    avg_grade = round(sum(list(grade_dict.values())) / len(list(grade_dict.values())), 2)
    print(f'Средняя оценка студентов {', '.join(list(grade_dict.keys()))} '
          f'по курсу {course}: {avg_grade}')


def print_avg_lecturer(lecturers: list, course: str):
    """Print average grade for each given lecturer"""
    grade_dict = {}
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer):
            if course in lecturer.grades:
                grade_dict[f'{lecturer.name} {lecturer.surname}'] = (
                    round(sum(lecturer.grades[course]) / len(lecturer.grades[course]), 2))
            else:
                print(f"У лектора {lecturer.name} {lecturer.surname} нет оценок "
                      f"по курсу {course}")
        else:
            print(f'Ошибка. {lecturer.name} {lecturer.surname} не является лектором')
    for name, avg_grade in grade_dict.items():
        print(f'Средняя оценка {name} по курсу {course}: {avg_grade}')


def print_avg_all_lecturers(lecturers: list, course: str):
    """Print average grade for all given lecturers together"""
    grade_dict = {}
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer):
            if course in lecturer.grades:
                grade_dict[f'{lecturer.name} {lecturer.surname}'] = (
                    round(sum(lecturer.grades[course]) / len(lecturer.grades[course]), 2))
            else:
                print(f"У лектора {lecturer.name} {lecturer.surname} нет оценок "
                      f"по курсу {course}")
        else:
            print(f'Ошибка. {lecturer.name} {lecturer.surname} не является лектором')
    avg_grade = round(sum(list(grade_dict.values())) / len(list(grade_dict.values())), 2)
    print(f'Средняя оценка лекторов {', '.join(list(grade_dict.keys()))} '
          f'по курсу {course}: {avg_grade}')


student_1 = Student('Ivan', 'Ivanov', 'male')
student_1.courses_finished.append('Git')
student_1.courses_finished.append('C++')
student_1.courses_in_progress.append('Python')
student_1.courses_in_progress.append('Java')
student_1.grades['Git'] = [10, 10, 10, 10, 10]
student_1.grades['Python'] = [10, 10]
student_1.grades['Java'] = [10, 10]

student_2 = Student('Petr', 'Petrov', 'male')
student_2.courses_finished.append('Git')
student_2.courses_in_progress.append('C++')
student_2.courses_in_progress.append('Python')
student_2.grades['Git'] = [5, 7, 5, 5, 3]
student_2.grades['Python'] = [3, 10]

student_3 = Student('Mikhail', 'Mikhailov', 'male')
student_3.courses_finished.append('Git')
student_3.courses_in_progress.append('C++')
student_3.grades['Git'] = [5, 7, 5, 5, 3]
student_3.grades['C++'] = [3, 10]

reviewer_1 = Reviewer('Viktor', 'Stepanov')
reviewer_1.courses_attached.append('Python')
reviewer_1.courses_attached.append('Git')

reviewer_2 = Reviewer('Dmitriy', 'Segreev')
reviewer_2.courses_attached.append('Python')
reviewer_2.courses_attached.append('Git')
reviewer_2.courses_attached.append('C++')

lecturer_1 = Lecturer('Tom', 'Tailor')
lecturer_1.courses_attached.append('Python')
lecturer_1.courses_attached.append('Git')
lecturer_1.grades['Git'] = [5, 5, 4, 7]
lecturer_1.grades['Python'] = [3, 10, 8]

lecturer_2 = Lecturer('Nikolay', 'Sidorov')
lecturer_2.courses_attached.append('Python')
lecturer_2.courses_attached.append('Git')
lecturer_2.grades['Git'] = [10, 10, 10, 7]
lecturer_2.grades['Python'] = [10, 10, 8]

lecturer_3 = Lecturer('Fred', 'Perry')
lecturer_3.courses_attached.append('Python')
lecturer_3.courses_attached.append('Git')
lecturer_3.grades['Git'] = [10, 10, 10, 7]
lecturer_3.grades['Python'] = [10, 10, 8]

lecturer_4 = Lecturer('Nils', 'Nicklson')
lecturer_4.courses_attached.append('Java')
lecturer_4.courses_attached.append('Git')


reviewer_1.add_student_grade(student_1, 'Python', 10)
reviewer_1.add_student_grade(student_1, 'Python', 10)

reviewer_2.add_student_grade(student_2, 'Python', 10)
reviewer_2.add_student_grade(student_2, 'Python', 5)

student_1.add_lecturer_grade(lecturer_1, 'Python', 8)
student_1.add_lecturer_grade(lecturer_1, 'Python', 10)

print(lecturer_4.avg_grade())
print(lecturer_4 == lecturer_1)

print(lecturer_4)

print(student_1.grades)

print(student_1.grades)
print(lecturer_1.grades)

print(lecturer_1.avg_grade())
print(reviewer_1.avg_grade())

print(student_1)
print(reviewer_1)
print(lecturer_1)
print(student_2)

print(lecturer_1 < lecturer_2)
print(lecturer_2 < lecturer_1)
print(student_1 < student_2)
print(student_2 < student_1)
print(reviewer_1 < lecturer_1)

print(lecturer_1 > lecturer_2)
print(lecturer_2 > lecturer_1)
print(student_1 > student_2)
print(student_2 > student_1)
print(reviewer_1 > lecturer_1)

print(student_1 == student_2)
print(lecturer_2 == lecturer_3)

print_avg_student([student_1, lecturer_1, student_2, student_3], 'Python')
print_avg_lecturer([lecturer_1, reviewer_1, lecturer_2, lecturer_3, lecturer_4], 'Python')

print_avg_all_students([student_1, reviewer_1, student_2, student_3], 'Python')
print_avg_all_lecturers([lecturer_1, lecturer_2, student_2, lecturer_3, lecturer_4], 'Python')
