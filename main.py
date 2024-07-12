class Student:
    def __init__(self, name, surname, gender):
        """Метод для инициализации атрибутов для студентов."""
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_mark(self):
        """Метод вычисляет среднюю оценку студента."""
        marks = []
        for i in self.grades.values():
            marks.extend(i)
        return sum(marks) / len(marks)

    def __str__(self):
        """Метод для отображения информации о студенте."""
        return f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.average_mark()}
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}
Завершенные курсы: {", ".join(self.finished_courses)}'''

    def __eq__(self, other):
        """Метод дял сравнения средних оценок студентов на равенство."""
        return self.average_mark() == other.average_mark()

    def __lt__(self, other):
        """Метод для сравнения средних оценок студентов."""
        return self.average_mark() < other.average_mark()


class Mentor:
    def __init__(self, name, surname):
        """Метод для инициализации атрибутов для менторов."""
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        """Метод для инициализации атрибутов для лекторов."""
        super().__init__(name, surname)
        self.grades = {}

    def get_grades(self, student, course, grade, lector):
        """Метод для выставления оценок лекторам."""
        if (isinstance(student, Student) and isinstance(lector, Lecturer) and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_mark(self):
        """Метод вычисляет среднюю оценку лектора."""
        marks = []
        for i in self.grades.values():
            marks.extend(i)
        return sum(marks) / len(marks)

    def __str__(self):
        """Метод для отображения информации о лекторе."""
        return f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.average_mark()}'''

    def __eq__(self, other):
        """Метод дял сравнения средних оценок лекторов на равенство."""
        return self.average_mark() == other.average_mark()

    def __lt__(self, other):
        """Метод для сравнения средних оценок лекторов."""
        return self.average_mark() < other.average_mark()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        """Метод для инициализации атрибутов для проверяющих."""
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        """Метод для выставления оценок студентам за домашнее задание."""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        """Метод для отображения информации о проверяющем."""
        return f'''Имя: {self.name}
Фамилия: {self.surname}'''


student_ivan = Student('Иван', 'Иванов', 'Муж')
student_anna = Student('Анна', 'Петрова', 'Жен')

lecturer_pavel = Lecturer('Павел', 'Павлов')
lecturer_petr = Lecturer('Петр', 'Смирнов')

reviewer_masha = Reviewer('Мария', 'Васильева')
reviewer_dima = Reviewer('Дмитрий', 'Сидоров')

student_ivan.finished_courses += ['Git', 'C++']
student_ivan.courses_in_progress += ['Python', 'Java']

student_anna.finished_courses += ['HTML', 'CSS']
student_anna.courses_in_progress += ['JavaScript', 'Python']

lecturer_petr.courses_attached += ['Python', 'Java']
lecturer_petr.get_grades(student_ivan, 'Python', 10, lecturer_petr)
lecturer_petr.get_grades(student_ivan, 'Java', 8, lecturer_petr)

lecturer_pavel.courses_attached += ['JavaScript', 'Python']
lecturer_pavel.get_grades(student_anna, 'Python', 9, lecturer_pavel)
lecturer_pavel.get_grades(student_anna, 'JavaScript', 9, lecturer_pavel)

reviewer_dima.courses_attached += ['Python', 'Java']
reviewer_dima.rate_hw(student_ivan, 'Python', 9)
reviewer_dima.rate_hw(student_ivan, 'Java', 8)

reviewer_masha.courses_attached += ['JavaScript', 'Python']
reviewer_masha.rate_hw(student_anna, 'JavaScript', 7)
reviewer_masha.rate_hw(student_anna, 'Python', 8)

print(student_ivan, end='\n\n')
print(student_anna, end='\n\n')
print(lecturer_petr, end='\n\n')
print(lecturer_pavel, end='\n\n')
print(reviewer_masha, end='\n\n')
print(reviewer_dima)

print(student_anna == student_ivan)
print(student_anna < student_ivan)

print(lecturer_petr == lecturer_pavel)
print(lecturer_pavel < lecturer_petr)


def avg_mark_students(students, course):
    """Функция принимает список студентов и курс и возвращает среднюю оценку в рамках курса"""
    marks = []
    for student in students:
        if course in student.grades:
            marks += student.grades[course]
        else:
            return 'Ошибка'
    return f'Для студентов средняя оценка по курсу {course} = {sum(marks) / len(marks)}'


print(avg_mark_students([student_ivan, student_anna], 'Python'))


def avg_mark_lecturers(lecturers, course):
    """Функция принимает список лекторов и курс и возвращает среднюю оценку в рамках курса"""
    marks = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            marks += lecturer.grades[course]
        else:
            return 'Ошибка'
    return f'Для лекторов средняя оценка по курсу {course} = {sum(marks) / len(marks)}'


print(avg_mark_lecturers([lecturer_petr, lecturer_pavel], 'Python'))
