class Person:

    def __init__(self, name, phone_number, email_address):
        self.name = name
        self.phone_number = phone_number
        self.email_address = email_address

    def print_person(self):
        print("Name:", self.name)
        print("Phone number:", self.phone_number)
        print("Email address:", self.email_address)
