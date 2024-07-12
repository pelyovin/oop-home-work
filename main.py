class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_mark(self):
        marks = []
        for i in self.grades.values():
            marks.extend(i)
        return sum(marks) / len(marks)

    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.average_mark()}
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}
Завершенные курсы: {", ".join(self.finished_courses)}'''


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    grades = {}

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def get_grades(self, student, course, grade, lector):
        if (isinstance(student, Student) and isinstance(lector, Lecturer) and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_mark(self):
        marks = []
        for i in self.grades.values():
            marks.extend(i)
        return sum(marks) / len(marks)

    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.average_mark()}'''


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}'''


some_student = Student('Some', 'Student', 'Male')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Java']
some_student.finished_courses += ['JS']
some_student.finished_courses += ['C++']


some_reviewer = Reviewer('Some', 'Reviewer')
some_reviewer.courses_attached += ['Python', 'Java']
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Java', 8)

some_lecturer = Lecturer('Some', 'Lecturer')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Java']
some_lecturer.get_grades(some_student, 'Python', 10, some_lecturer)
some_lecturer.get_grades(some_student, 'Python', 6, some_lecturer)
some_lecturer.get_grades(some_student, 'Java', 8, some_lecturer)


print(some_lecturer)
print()
print(some_student)
print()
print(some_reviewer)
