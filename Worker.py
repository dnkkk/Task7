from Person import Person


class Worker(Person):
    def __init__(self, name, phone_number, email_address, experience, hourly_wag, hours_work):
        super().__init__(name, phone_number, email_address)
        self.experience = max(experience, 0)
        self.hourly_wage = max(hourly_wag, 0)
        self.hours_work = max(hours_work, 0)
        self.salary = self.calculate_salary(self.hours_work, self.hourly_wage)
        self.premium = round(self.calculate_premium(self.experience, self.salary))

    def get_worker(self):
        return self

    def set_worker(self, worker):
        self.name = worker.name
        self.phone_number = worker.phone_number
        self.email_address = worker.email_address
        self.experience = worker.experience
        self.hourly_wage = worker.hourly_wage
        self.hours_work = worker.hours_work
        self.salary = worker.salary
        self.premium = worker.premium

    @staticmethod
    def calculate_premium(experience, salary):
        if experience < 1:
            return 0
        elif experience < 3:
            return salary * 0.05
        elif experience < 5:
            return salary * 0.08
        else:
            return salary * 0.15

    @staticmethod
    def calculate_salary(hours_work, hourly_wage):
        return hours_work * hourly_wage

    def __str__(self):
        return "Surname: " + str(self.name) + \
               "\nExperience: " + str(self.experience) + "\n" + \
               str(self.name) + " has worked: " + str(self.hourly_wage) + " hours\n" + \
               "Salary: " + str(self.salary) + "\n" + "Premy: " + str(self.premium)

    def in_file(self):
        file_name = self.name + ".txt"
        with open(file_name, "w") as file:
            file.write(self.__str__())

        print("Information about", self.name, "was written in file", file_name)
