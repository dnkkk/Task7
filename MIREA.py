class MIREA:
    def __init__(self):
        self.students = []
        self.workers = []

    def add_student(self, student):
        self.students.append(student)

    def add_worker(self, worker):
        self.students.append(worker)

    def print_students(self):
        for student in self.students:
            print(student)

    def print_workers(self):
        for worker in self.workers:
            print(worker)

    def print_info(self):
        print("Info:")
        print(" - Count students:", len(self.students))
        print(" - Count workers:", len(self.workers))
