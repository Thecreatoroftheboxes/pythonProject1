class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.grades_av = 0

    def add_courses(self, course_name):
        """ Adds a course to the list"""
        self.finished_courses.append(course_name)

    def rate_by_students(self, lecturer, course, grade):
        """Adds a grade to the lecturer from the student"""
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course \
                in lecturer.courses_attached:
            if course in lecturer.lectures_grades:
                lecturer.lectures_grades[course] += [grade]
            else:
                lecturer.lectures_grades[course] = [grade]

    def average_value_st(self):
        """Сalculates the average value"""
        if sum([len(i) for i in self.grades.values()]) > 0:
            res_st = round(sum([sum(i) for i in self.grades.values()]) /
                           sum([len(i) for i in self.grades.values()]), 2)
            self.grades_av = res_st
            return res_st

    def rating_of_students(self, other):
        """Sorts by students rating"""
        if self.grades_av > other.grades_av:
            print(f'Рейтинг студента {self.name} {self.surname} составляет {self.grades_av} и выше, чем у'
                  f'студента {other.name} {other.surname} с рейтингом {other.grades_av}')
        elif self.lectures_grades_av < other.lectures_grades_av:
            print(f'Рейтинг студента {self.name} {self.surname} составляет {self.grades_av} и ниже, чем у'
                  f'студента {other.name} {other.surname} с рейтингом {other.grades_av}')
        else:
            print(f'Рейтинг студента {self.name} {self.surname} составляет {self.grades_av} и такой же, как у'
                  f'студента {other.name} {other.surname} с рейтингом {other.grades_av}')

    def __str__(self):
        """Overrides the string for the Student class"""
        return f"{self.name}\n{self.surname}\nСредняя оценка за домашку: {self.grades_av}\n" \
               f"Курсы в процессе изучения: {','.join(self.courses_in_progress)}\n" \
               f"Завершенные курсы: {','.join(self.finished_courses)}\n"

    def average_grade_for_the_course(self, other, course):
        if course in self.courses_in_progress or course in other.courses_in_progress:
            if course == self.grades.keys() or course == other.grades.keys():
                x = [sum(i) for i in self.grades.values()]
                print(x)



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lectures_grades = {}
        self.lectures_grades_av = 0

    def average_value(self):
        """Сalculates the average value"""
        if sum([len(i) for i in self.lectures_grades.values()]) > 0:
            res_ = round(sum([sum(i) for i in self.lectures_grades.values()]) /
                         sum([len(i) for i in self.lectures_grades.values()]), 2)
            self.lectures_grades_av = res_

    def rating_of_lecturers(self, other):
        """Sorts by lecturer rating"""
        if self.lectures_grades_av > other.lectures_grades_av:
            print(f'Рейтинг лектора {self.name} {self.surname} составляет {self.lectures_grades_av} и выше, чем у'
                  f'лектора {other.name} {other.surname} с рейтингом {other.lectures_grades_av}')
        elif self.lectures_grades_av < other.lectures_grades_av:
            print(f'Рейтинг лектора {self.name} {self.surname} составляет {self.lectures_grades_av} и ниже, чем у'
                  f'лектора {other.name} {other.surname} с рейтингом {other.lectures_grades_av}')
        else:
            print(f'Рейтинг лектора {self.name} {self.surname} составляет {self.lectures_grades_av} и такой же, как у'
                  f'лектора {other.name} {other.surname} с рейтингом {other.lectures_grades_av}')

    def __str__(self):
        """Overrides the string for the Lecturer class"""
        return f"{self.name}\n{self.surname}\nСредняя оценка за лекции: {self.lectures_grades_av}\n"


class Reviewer(Mentor):
    def rate_reviewer(self, student, course, grade):
        """Adds a grade to the student from the reviewer"""
        if isinstance(student, Student) and course in self.courses_attached and course \
                in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка')

    def __str__(self):
        """Overrides the string for the Reviewer class"""
        return f"{self.name}\n{self.surname}\n"


lecturer_1 = Lecturer('Сэм', 'Бадьев')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Git']

lecturer_2 = Lecturer('Сэм2', 'Бадьев2')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Git']

student_1 = Student('Ученик', 'Заучка', 'гендер')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']

student_2 = Student('Ученик2', 'Заучка2', 'гендер2')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']

student_1.rate_by_students(lecturer_1, 'Python', 10)
student_1.rate_by_students(lecturer_1, 'Python', 9)
student_1.rate_by_students(lecturer_1, 'Git', 8)
student_1.rate_by_students(lecturer_1, 'Git', 10)
student_1.rate_by_students(lecturer_1, 'Python', 8)

student_1.rate_by_students(lecturer_2, 'Python', 10)
student_1.rate_by_students(lecturer_2, 'Python', 10)
student_1.rate_by_students(lecturer_2, 'Git', 10)
student_1.rate_by_students(lecturer_2, 'Git', 10)
student_1.rate_by_students(lecturer_2, 'Python', 10)

reviewer_1 = Reviewer('Оценщик', 'Заданий')
reviewer_2 = Reviewer('Оценщик2', 'Заданий2')

reviewer_1.courses_attached += ['Git']
reviewer_1.courses_attached += ['Python']
reviewer_1.rate_reviewer(student_1, 'Python', 10)
reviewer_1.rate_reviewer(student_1, 'Git', 10)
reviewer_1.rate_reviewer(student_1, 'Python', 7)
reviewer_1.rate_reviewer(student_1, 'Python', 7)
reviewer_1.rate_reviewer(student_1, 'Git', 10)

student_1.add_courses('Введение в программирование')

student_1.average_value_st()
lecturer_1.average_value()
lecturer_2.average_value()
print(lecturer_1.__str__())
print(lecturer_2.__str__())
print(student_1.__str__())
print(student_2.__str__())

print(reviewer_1.__str__())

lecturer_1.rating_of_lecturers(lecturer_2)
student_1.rating_of_students(student_2)
student_1.average_grade_for_the_course(student_2, 'Python')
