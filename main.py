from student import Student
from student_group import StudentGroup
from subject import Subject
from teacher import Teacher
from exam import Exam

# Создать предметы
math = Subject('Математика')
english = Subject('Английский язык')
history = Subject('История')

# Создать учителей
t_math = Teacher('Мишка Сберкнижка', 'Преподаватель', math)
t_english = Teacher('Мишкинс-Джонсон', 'Преподаватель', english)
t_history = Teacher('Микаэла Хистори', 'Преподаватель', history)

# Создать студентов
s1 = Student('Мишутка', 'Студент')
s2 = Student('Молли', 'Студент')
s3 = Student('Сари', 'Студент')
s4 = Student('Урчи', 'Студент')

# Создать группу и добавить студентов
group = StudentGroup(t_math)
group.add_student(s1)
group.add_student(s2)
group.add_student(s3)
group.add_student(s4)

# добавить объект НЕ студент
# group.add_student(55)

# Проверить добавление студентов в группу
print(f'Студенты в группе:\n{group.get_students_list()}')

# Создать экзамен
e = Exam(math, group)

# Начало экзамена без сгенерированных билетов
# e.start_exam()

# генерация билетов
e.get_tickets()

# завершение экзамена до его начала
# e.stop_exam()

# начало экзамена
e.start_exam()

# завершение экзамена
e.stop_exam()

# вывод списка студентов и оценок
print(f'Результаты экзамена:\n{e.exam_list}')
