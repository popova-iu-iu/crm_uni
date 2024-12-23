from student import Student
from teacher import NotStudentObjectError


class StudentGroup:
    def __init__(self, teacher):
        self.teacher = teacher
        self.students = []

    # Проверить есть ли студент в группе
    def __contains__(self, student):
        return student in self.students

    # Зачислить студента
    def add_student(self, student):
        if isinstance(student, Student):
            for st in self.students:
                if st.person_id == student.person_id:
                    print('Студент уже зачислен')
                    return
            self.students.append(student)
        else:
            raise NotStudentObjectError('Не студент')

    # Отчислить студента
    def del_student(self, student):
        if isinstance(student, Student):
            for st in self.students:
                if st.person_id == student.person_id:
                    self.students.remove(student)
        else:
            raise NotStudentObjectError('Не студент')

    # Получить список студентов в группе
    def get_students_list(self):
        return [student.get_info() for student in self.students]

    # Получить кол-во студентов для генерации кол-ва билетов на экзамен
    def __len__(self):
        return len(self.students)
