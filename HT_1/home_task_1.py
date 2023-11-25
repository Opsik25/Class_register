class SchoolMember:


    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def avg_grade(self):
        if hasattr(self, 'grades'):
            self.__grades_list = []
            for el in self.grades.values():
                self.__grades_list.extend(el)
            return sum(self.__grades_list) / len(self.__grades_list)
        else:
            return 'Нет оценок'

    def __lt__(self, other):
        if (isinstance(self, Student) and isinstance(other, Student) or
            isinstance(self, Lecturer) and isinstance(other, Lecturer)):
            if  self.avg_grade() < other.avg_grade():
                return (f"Да, средняя оценка {self.name} {self.surname} "
                        f"ниже средней оценки {other.name} {other.surname}")
            else:
                return (f"Нет, средняя оценка {self.name} {self.surname} "
                        f"не ниже средней оценки {other.name} {other.surname}")
        else:
            return 'Вы можете сравнить объекты только одного класса, у которых есть оценки'

    def __gt__(self, other):
        if (isinstance(self, Student) and isinstance(other, Student) or
            isinstance(self, Lecturer) and isinstance(other, Lecturer)):
            if  self.avg_grade() > other.avg_grade():
                return (f"Да, средняя оценка {self.name} {self.surname} "
                        f"выше средней оценки {other.name} {other.surname}")
            else:
                return (f"Нет, средняя оценка {self.name} {self.surname} "
                        f"не выше средней оценки {other.name} {other.surname}")
        else:
            return 'Вы можете сравнить объекты только одного класса, у которых есть оценки'

    def __eq__(self, other):
        if (isinstance(self, Student) and isinstance(other, Student) or
            isinstance(self, Lecturer) and isinstance(other, Lecturer)):
            if  self.avg_grade() == other.avg_grade():
                return (f"Да, средняя оценка {self.name} {self.surname} "
                        f"равна средней оценке {other.name} {other.surname}")
            else:
                return (f"Нет, средняя оценка {self.name} {self.surname} "
                        f"не равна средней оценке {other.name} {other.surname}")
        else:
            return 'Вы можете сравнить объекты только одного класса, у которых есть оценки'


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
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress and
            course in lecturer.courses_attached):
            if course not in lecturer.grades:
                lecturer.grades[course] = [grade]
            else:
                lecturer.grades[course].append(grade)
        else:
            return 'Ошибка'

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
            course in student.courses_in_progress):
            if course not in student.grades:
                student.grades[course] = [grade]
            else:
                student.grades[course].append(grade)
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


student_1 = Student('Ivan', 'Ivanov', 'male')
student_1.courses_finished.append('Git')
student_1.courses_finished.append('C++')
student_1.courses_in_progress.append('Python')
student_1.grades['Git'] = [10, 10, 10, 10, 10]
student_1.grades['Python'] = [10, 10]

student_2 = Student('Petr', 'Petrov', 'male')
student_2.courses_finished.append('Git')
student_2.courses_finished.append('C++')
student_2.courses_in_progress.append('Python')
student_2.grades['Git'] = [5, 7, 5, 5, 3]
student_2.grades['Python'] = [3, 10]

reviewer_1 = Reviewer('Viktor', 'Stepanov')
reviewer_1.courses_attached.append('Python')
reviewer_1.courses_attached.append('Git')

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

reviewer_1.add_student_grade(student_1, 'Python', 7)
reviewer_1.add_student_grade(student_1, 'Python', 8)
reviewer_1.add_student_grade(student_1, 'Python', 6)

student_1.add_lucturer_grade(lecturer_1, 'Python', 5)
student_1.add_lucturer_grade(lecturer_1, 'Python', 8)
student_1.add_lucturer_grade(lecturer_1, 'Python', 10)

print(student_1.grades)
print(lecturer_1.grades)

print(lecturer_1.avg_grade())
print(reviewer_1.avg_grade())

print(reviewer_1)
print(lecturer_1)
print(student_1)

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

