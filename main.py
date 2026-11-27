from doctor import Doctor
from hospital import Hospital
from patient import Patient


def input_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a number.")


def add_doctor(hospital):
    print("\nAdd Doctor")
    name = input("Name: ").strip()
    surname = input("Surname: ").strip()
    age = input_number("Age: ")
    phone = input("Phone: ").strip()
    doctor_id = input_number("Doctor ID: ")
    specialization = input("Specialization: ").strip()
    experience = input_number("Experience (years): ")

    doctor = Doctor(name, surname, age, phone, doctor_id, specialization, experience)
    hospital.addDoctor(doctor)
    print("Doctor added successfully.")


def add_patient(hospital):
    print("\nAdd Patient")
    name = input("Name: ").strip()
    surname = input("Surname: ").strip()
    age = input_number("Age: ")
    phone = input("Phone: ").strip()
    patient_id = input_number("Patient ID: ")
    blood_group = input("Blood group: ").strip()
    medical_history = input("Medical history: ").strip()

    patient = Patient(name, surname, age, phone, patient_id, blood_group, medical_history)
    hospital.addPatient(patient)
    print("Patient added successfully.")


def create_appointment(hospital):
    print("\nCreate Appointment")
    doctor_id = input_number("Doctor ID: ")
    patient_id = input_number("Patient ID: ")
    date = input("Date (YYYY-MM-DD): ").strip()
    time = input("Time (HH:MM): ").strip()

    appointment = hospital.createAppointment(
        doctor_id,
        patient_id,
        f"{date} {time}".strip(),
    )
    if appointment:
        print("Appointment created successfully.")


def print_menu():
    print("\n1. Add Doctor")
    print("2. Add Patient")
    print("3. Show All Doctors")
    print("4. Show All Patients")
    print("5. Create Appointment")
    print("6. Show All Appointments")
    print("0. Exit")


def main():
    hospital = Hospital("Hospital")

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_doctor(hospital)
        elif choice == "2":
            add_patient(hospital)
        elif choice == "3":
            print()
            hospital.showDoctors()
        elif choice == "4":
            print()
            hospital.showPatients()
        elif choice == "5":
            create_appointment(hospital)
        elif choice == "6":
            print()
            hospital.showAppointments()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()