from datetime import datetime, timedelta
import random
from ticket_generator import TicketGenerator


# Исключение
class NoTicketsError(Exception):
    pass


# Исключение
class NotStartedError(Exception):
    pass


class Exam:
    def __init__(self, subject, student_group):
        self.subject = subject
        self.student_group = student_group
        self.tickets_count = len(student_group) * 2
        self.tickets = []
        self.start_date = datetime.now()
        self.stop_date = self.start_date + timedelta(hours=2)
        self.exam_list = []

    # Сгенерировать билеты
    def get_tickets(self):
        t = TicketGenerator(self.subject)
        for i in range(self.tickets_count):
            ticket = next(t.gen_ticket())
            self.tickets.append(ticket)

    # Начать экзамен и выдать билеты
    def start_exam(self):
        if len(self.tickets) == 0:
            raise NoTicketsError('Билеты еще не сгенерированы')
        for student in self.student_group.students:
            ticket = random.choice(self.tickets)
            self.tickets.remove(ticket)
            student.ticket_id = ticket['id']

            self.exam_list.append(student.get_info())

    # закончить экзамен и выставить оценки
    def stop_exam(self):
        if len(self.exam_list) == 0:
            raise NotStartedError('Экзамен еще не начался')
        for s in self.exam_list:
            for student in self.student_group.students:
                if student.person_id == s['id']:
                    self.student_group.teacher.rate_student(student)
                    s['mark'] = student.mark
                    break
