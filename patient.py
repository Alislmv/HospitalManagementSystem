from person import Person

class Patient(Person):
    def __init__(self, name, surname, age, phone, patientID, bloodGroup, medicalHistory):
        super().__init__(name, surname, age, phone)
        self.patientID = patientID # public
        self._bloodGroup = bloodGroup # protected 
        self.__medicalHistory = medicalHistory # private

    def showInfo(self):
        print(f"ID: {self.patientID} - {self.name} {self.surname}")
        print(f"Age: {self.age}")
        print(f"Phone: {self.phone}")
        print(f"Blood group: {self._bloodGroup}")

    def getMedicalHistory(self):
        return self.__medicalHistory

    def updateMedicalHistory(self, medicalHistory):
        self.__medicalHistory = medicalHistory

    @property
    def bloodGroup(self):
        return self._bloodGroup