import random


class Subject:
    def __init__(self, subject_name):
        self.subject_name = subject_name
        self.subject_id = random.randint(10, 99)

    # Получить информацию
    def get_info(self):
        return {
            'id': self.subject_id,
            'subject': self.subject_name
        }

    # Получить id предмета
    def get_id(self):
        return self.subject_id

    # Вывести информацию о предмете
    def __str__(self):
        return f'Предмет: {self.subject_name}\nId: {self.subject_id}'
