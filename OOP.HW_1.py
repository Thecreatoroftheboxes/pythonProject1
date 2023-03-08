class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_student(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course \
                in lecturer.courses_attached:
            if course in lecturer.lectures_grades:
                lecturer.lectures_grades[course] += [grade]
            else:
                lecturer.lectures_grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_value_st(self):
        if sum([len(i) for i in self.grades.values()]) > 0:
            res_st = round(sum([sum(i) for i in self.grades.values()]) /
                           sum([len(i) for i in self.grades.values()]), 2)
            self.grades = res_st
            return res_st

    def __str__(self):
        return f"{self.name}\n{self.surname}\nСредняя оценка за домашку: {self.grades}\n" \
               f"Курсы в процессе изучения: {self.courses_in_progress}\n" \
               f"Завершенные курсы: {self.finished_courses}"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lectures_grades = {}

    def average_value(self):
        if sum([len(i) for i in self.lectures_grades.values()]) > 0:
            res_ = round(sum([sum(i) for i in self.lectures_grades.values()]) /
                         sum([len(i) for i in self.lectures_grades.values()]), 2)
            self.lectures_grades = res_
            return res_

    def __str__(self):
        return f"{self.name}\n{self.surname}\nСредняя оценка за лекции: {self.lectures_grades}"


class Reviewer(Mentor):
    def rate_reviewer(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course \
                in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"{self.name}\n{self.surname}\n"


# lecturer_1 = Lecturer('Сэм', 'Бадьевич')
# print(lecturer_1)
lecturer_1 = Lecturer('Сэм', 'Бадьевич')
lecturer_1.courses_attached += ['Python']

student_1 = Student('Ученик', 'Заучка', 'гендер')
student_1.courses_in_progress += ['Python']

student_1.rate_student(lecturer_1, 'Python', 10)
student_1.rate_student(lecturer_1, 'Python', 8)
student_1.rate_student(lecturer_1, 'Python', 8)

reviewer_1 = Reviewer('Оценщик', 'Заданий')
reviewer_1.rate_reviewer(student_1, 'Python', 10)
reviewer_1.rate_reviewer(student_1, 'Git', 10)
reviewer_1.rate_reviewer(student_1, 'Python', 7)
reviewer_1.rate_reviewer(student_1, 'Python', 7)

lecturer_1.average_value()

student_1.add_courses('Введение в программирование')

student_1.average_value_st()
print(lecturer_1.__str__())
# print(lecturer_1.lectures_grades)
print(student_1.__str__())
