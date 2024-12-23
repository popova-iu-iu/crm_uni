from person import Person


class Student(Person):
    def __init__(self, name, role):
        super().__init__(name, role)
        self.ticket_id = None
        self.mark = None

    def get_info(self):
        info = super().get_info()
        info.update({
            'ticket_id': self.ticket_id,
            'mark': self.mark
        })
        return info
