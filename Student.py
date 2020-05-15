from Person import Person


class Student(Person):
    def __init__(self, name, phone_number, email_address, student_number, average_mark):
        super().__init__(name, phone_number, email_address)
        self.student_number = student_number
        self.average_mark = average_mark

    def is_eligible_to_enroll(self):
        return self.average_mark > 2.5

    def get_seminars_taken(self):
        return self.student_number
