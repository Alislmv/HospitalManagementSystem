class Appointment():
    def __init__(self, appointmentID, doctor, patient, date):
        self.appointmentID = appointmentID
        self.doctor = doctor
        self.patient = patient
        self.date = date

    def showInfo(self):
        print(f"Appointment ID: {self.appointmentID}")
        print(f"Doctor: {self.doctor.name} {self.doctor.surname}")
        print(f"Patient: {self.patient.name} {self.patient.surname}")
        print(f"Date: {self.date}")