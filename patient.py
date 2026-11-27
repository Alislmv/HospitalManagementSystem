from person import Person

class Patient(Person):
    def __init__(self, name, surname, age, phone, patientID, bloodGroup, medicalHistory):
        super().__init__(name, surname, age, phone)
        self.patientID = patientID
        self._bloodGroup = bloodGroup 
        self.__medicalHistory = medicalHistory 

    def showInfo(self):
        print(f"ID: {self.patientID} - {self.name} {self.surname}")
        print(f"Age: {self.age}")
        print(f"Phone: {self.phone}")
        print(f"Blood group: {self._bloodGroup}")

    def getMedicalHistory(self):
        pass

    def updateMedicalHistory(self):
        pass