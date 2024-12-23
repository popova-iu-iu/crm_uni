import random
from faker import Faker

fake = Faker()


class TicketGenerator:
    def __init__(self, subject):
        self.subject = subject

    # Сгенерировать билет
    def gen_ticket(self):
        yield {'id': random.randint(1, 100), 'subject': self.subject.subject_name,
               'question': fake.text(max_nb_chars=100)}
