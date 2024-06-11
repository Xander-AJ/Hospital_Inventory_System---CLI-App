from datetime import datetime
from helpers import (
    add_patient,
    delete_patient,
    update_patient,
    add_doctor,
    delete_doctor,
    update_doctor,
    book_appointment,
    update_appointment,
    cancel_appointment,
    view_departments,
    view_doctors,
    view_patient_residents,
    view_patient_details,
    view_doctor_appointments,
    add_user,
    delete_user,
    update_user,
    search_patients,
    filter_appointments_by_date,
    generate_patient_report,
    generate_appointment_statistics,
)
from models import init_db


def patient_menu():
    while True:
        print("\nPatient Menu")
        print("1. Add New Patient")
        print("2. Delete Patient")
        print("3. Update Patient Details")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter patient name: ")
            age = input("Enter patient age: ")
            address = input("Enter patient address: ")
            phone = input("Enter patient phone: ")
            add_patient(name, age, address, phone)
            print("Patient added successfully.")

        elif choice == "2":
            patient_id = input("Enter patient ID to delete: ")
            delete_patient(patient_id)
            print("Patient deleted successfully.")

        elif choice == "3":
            patient_id = input("Enter patient ID to update: ")
            name = input("Enter new name (leave blank to skip): ")
            age = input("Enter new age (leave blank to skip): ")
            address = input("Enter new address (leave blank to skip): ")
            phone = input("Enter new phone (leave blank to skip): ")
            update_patient(patient_id, name, age, address, phone)
            print("Patient details updated successfully.")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")


def doctor_menu():
    while True:
        print("\nDoctor Menu")
        print("1. Add New Doctor")
        print("2. Delete Doctor")
        print("3. Update Doctor Details")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter doctor name: ")
            specialization = input("Enter doctor specialization: ")
            phone = input("Enter doctor phone: ")
            add_doctor(name, specialization, phone)
            print("Doctor added successfully.")

        elif choice == "2":
            doctor_id = input("Enter doctor ID to delete: ")
            delete_doctor(doctor_id)
            print("Doctor deleted successfully.")

        elif choice == "3":
            doctor_id = input("Enter doctor ID to update: ")
            name = input("Enter new name (leave blank to skip): ")
            specialization = input("Enter new specialization (leave blank to skip): ")
            phone = input("Enter new phone (leave blank to skip): ")
            update_doctor(doctor_id, name, specialization, phone)
            print("Doctor details updated successfully.")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")


def appointment_menu():
    while True:
        print("\nAppointment Menu")
        print("1. Book Appointment")
        print("2. Update Appointment")
        print("3. Cancel Appointment")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            patient_id = input("Enter patient ID: ")
            doctor_id = input("Enter doctor ID: ")
            appointment_time = input("Enter appointment time (YYYY-MM-DD HH:MM:SS): ")
            book_appointment(
                patient_id,
                doctor_id,
                datetime.strptime(appointment_time, "%Y-%m-%d %H:%M:%S"),
            )
            print("Appointment booked successfully.")

        elif choice == "2":
            appointment_id = input("Enter appointment ID to update: ")
            patient_id = input("Enter new patient ID (leave blank to skip): ")
            doctor_id = input("Enter new doctor ID (leave blank to skip): ")
            appointment_time = input(
                "Enter new appointment time (YYYY-MM-DD HH:MM:SS) (leave blank to skip): "
            )
            update_appointment(
                appointment_id,
                patient_id,
                doctor_id,
                (
                    datetime.strptime(appointment_time, "%Y-%m-%d %H:%M:%S")
                    if appointment_time
                    else None
                ),
            )
            print("Appointment updated successfully.")

        elif choice == "3":
            appointment_id = input("Enter appointment ID to cancel: ")
            cancel_appointment(appointment_id)
            print("Appointment canceled successfully.")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")


def view_menu():
    while True:
        print("\nView Menu")
        print("1. View Departments")
        print("2. View Doctors")
        print("3. View Patient Residents")
        print("4. View Patient Details")
        print("5. View Doctor's Appointments")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_departments()

        elif choice == "2":
            view_doctors()

        elif choice == "3":
            view_patient_residents()

        elif choice == "4":
            view_patient_details()

        elif choice == "5":
            view_doctor_appointments()

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")


def manage_users():
    while True:
        print("\nUser Management Menu")
        print("1. Add New User")
        print("2. Delete User")
        print("3. Update User Details")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            role_id = input("Enter role ID: ")
            add_user(username, password, role_id)
            print("User added successfully.")

        elif choice == "2":
            user_id = input("Enter user ID to delete: ")
            delete_user(user_id)
            print("User deleted successfully.")

        elif choice == "3":
            user_id = input("Enter user ID to update: ")
            username = input("Enter new username (leave blank to skip): ")
            password = input("Enter new password (leave blank to skip): ")
            role_id = input("Enter new role ID (leave blank to skip): ")
            update_user(user_id, username, password, role_id)
            print("User details updated successfully.")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")


def search_menu():
    while True:
        print("\nSearch Menu")
        print("1. Search Patients")
        print("2. Filter Appointments by Date")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            query = input("Enter patient name to search: ")
            patients = search_patients(query)
            for patient in patients:
                print(
                    f"ID: {patient.id}, Name: {patient.name}, Age: {patient.age}, Address: {patient.address}, Phone: {patient.phone}"
                )

        elif choice == "2":
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            appointments = filter_appointments_by_date(start_date, end_date)
            for appointment in appointments:
                print(
                    f"Appointment ID: {appointment.id}, Patient ID: {appointment.patient_id}, Doctor ID: {appointment.doctor_id}, Appointment Time: {appointment.appointment_time}"
                )

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")


def report_menu():
    while True:
        print("\nReport Menu")
        print("1. Generate Patient Report")
        print("2. Generate Appointment Statistics")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            report = generate_patient_report()
            for item in report:
                print(item)

        elif choice == "2":
            stats = generate_appointment_statistics()
            for key, value in stats.items():
                print(f"{key}: {value}")

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")


def main_menu():
    init_db()
    while True:
        print("\nMain Menu")
        print("1. Manage Patients")
        print("2. Manage Doctors")
        print("3. Manage Appointments")
        print("4. View Information")
        print("5. Manage Users")
        print("6. Search")
        print("7. Reports")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            patient_menu()
        elif choice == "2":
            doctor_menu()
        elif choice == "3":
            appointment_menu()
        elif choice == "4":
            view_menu()
        elif choice == "5":
            manage_users()
        elif choice == "6":
            search_menu()
        elif choice == "7":
            report_menu()
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()