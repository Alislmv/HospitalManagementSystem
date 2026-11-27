from person import Person

class Doctor(Person):
    def __init__(self, name, surname, age, phone, doctorID, specialization, experience):
        super().__init__(name, surname, age, phone)
        self.doctorID = doctorID
        self.specialization = specialization
        self.experience = experience

    def showInfo(self):
        print(f"ID: {self.doctorID} - {self.name} {self.surname}")
        print(f"Specialization: {self.specialization}")
        print(f"Experience: {self.experience} years")
        print(f"Phone: {self.phone}")