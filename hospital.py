from appointment import Appointment

class Hospital:
    def __init__(self, name):
        self.name = name
        self.doctors = []
        self.patients = []
        self.appointments = []

    def addDoctor(self, doctor):
        self.doctors.append(doctor)
        return doctor

    def addPatient(self, patient):
        self.patients.append(patient)
        return patient

    def showDoctors(self):
        if not self.doctors:
            print("No doctors found.")
            return
        for doctor in self.doctors:
            doctor.showInfo()
            print()

    def showPatients(self):
        if not self.patients:
            print("No patients found.")
            return
        for patient in self.patients:
            patient.showInfo()
            print()

    def createAppointment(self, doctorID, patientID, date):
        doctor = next((d for d in self.doctors if d.doctorID == doctorID), None)
        patient = next((p for p in self.patients if p.patientID == patientID), None)

        if doctor is None:
            print("Doctor not found.")
            return None
        if patient is None:
            print("Patient not found.")
            return None

        appointmentID = len(self.appointments) + 1
        appointment = Appointment(appointmentID, doctor, patient, date)
        self.appointments.append(appointment)
        return appointment

    def showAppointments(self):
        if not self.appointments:
            print("No appointments found.")
            return
        for appointment in self.appointments:
            appointment.showInfo()
            print()