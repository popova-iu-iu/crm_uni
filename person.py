import random


class Person:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.person_id = random.randint(1000, 9999)
        self.notifications = []

    # Получить информацию
    def get_info(self):
        return {
            'id': self.person_id,
            'name': self.name,
            'role': self.role
        }

    # Отправить уведомление
    def notify(self, msg):
        self.notifications.append(msg)

    # Получить список уведомлений
    def get_notifications(self):
        return self.notifications

    # Узнать роль
    def get_role(self):
        return self.role

    # Узнать id:
    def get_id(self):
        return self.person_id
