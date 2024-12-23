from random import randint
from person import Person
from student import Student


# Исключение
class NotStudentObjectError(Exception):
    pass


class Teacher(Person):
    def __init__(self, name, role, subject):
        super().__init__(name, role)
        self.subject = subject

    # Узнать информацию о предмете
    def get_subject_info(self):
        return self.subject.subject_name

    # Поставить оценку студенту на экзамене
    def rate_student(self, student):
        if isinstance(student, Student):
            mark = randint(2, 5)
            student.mark = mark
        else:
            raise NotStudentObjectError('Не студент')

    def get_info(self):
        info = super().get_info()
        info.update({
            'subject': self.subject
        })
        return info
