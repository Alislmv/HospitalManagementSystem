from appointment import Appointment

class Hospital:
    def __init__(self, name):
        self.name = name
        self.doctors = []
        self.patients = []
        self.appointments = []

    def addDoctor(self, doctor):
        self.doctors.append(doctor)

    def addPatient(self, patient):
        self.patients.append(patient)

    def showDoctors(self):
        if not self.doctors:
            print("There are no doctors")
            return

        for doctor in self.doctors:
            doctor.showInfo()

    def showPatient(self):
        if not self.patients:
            print("There are no patients")
            return

        for patient in self.patients:
            patient.showInfo()

    def createAppointment(self, doctorID, patientID, date):
        pass

    def showAppointments(self):
        if not self.appointments:
            print("There are no appointments")
            return
      
        for appointment in self.appointments:
            self.appointments.showInfo()