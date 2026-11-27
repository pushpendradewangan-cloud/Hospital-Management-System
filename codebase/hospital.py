import csv
import os

FILE = "patients.csv"


# Create CSV file if it does not exist
if not os.path.exists(FILE):
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Age", "Disease", "Doctor"])


# Load patient records
def load_patients():
    patients = {}

    with open(FILE, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            patients[row["ID"]] = row

    return patients


# Save patient records
def save_patients(patients):
    with open(FILE, "w", newline="") as f:
        fields = ["ID", "Name", "Age", "Disease", "Doctor"]

        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()

        for patient in patients.values():
            writer.writerow(patient)


# Add new patient
def add_patient():
    patients = load_patients()

    name = input("Enter Name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    age_input = input("Enter Age: ")

    try:
        age = int(age_input)

        if age < 0 or age > 120:
            print("Invalid age. Enter a number between 0 and 120.")
            print("Patient not added.")
            return

    except ValueError:
        print("Invalid age. Enter a number between 0 and 120.")
        print("Patient not added.")
        return

    disease = input("Enter Disease: ").strip()
    doctor = input("Enter Doctor: ").strip()

    # Generate next patient ID
    numbers = []

    for patient_id in patients:
        numbers.append(int(patient_id[1:]))

    if len(numbers) == 0:
        next_id = 101
    else:
        next_id = max(numbers) + 1

    patient_id = "P" + str(next_id)

    patients[patient_id] = {
        "ID": patient_id,
        "Name": name,
        "Age": age,
        "Disease": disease,
        "Doctor": doctor
    }

    save_patients(patients)

    print("Patient added. ID:", patient_id, "|",
          name, "|", age, "|", disease, "|", doctor)


# View all patients
def view_patients():
    patients = load_patients()

    if len(patients) == 0:
        print("No patient records found.")
        return

    for patient in patients.values():
        print("-----------------------------")
        print("ID:", patient["ID"])
        print("Name:", patient["Name"])
        print("Age:", patient["Age"])
        print("Disease:", patient["Disease"])
        print("Doctor:", patient["Doctor"])


# Search patient by ID
def search_patient():
    patients = load_patients()

    patient_id = input("Enter Patient ID: ").strip().upper()

    if patient_id in patients:
        patient = patients[patient_id]

        print("Patient Found!")
        print("ID:", patient["ID"])
        print("Name:", patient["Name"])
        print("Age:", patient["Age"])
        print("Disease:", patient["Disease"])
        print("Doctor:", patient["Doctor"])

    else:
        print("Patient ID not found.")


# Update patient details
def update_patient():
    patients = load_patients()

    patient_id = input("Enter Patient ID: ").strip().upper()

    if patient_id not in patients:
        print("Patient ID not found.")
        return

    patient = patients[patient_id]

    print("Leave blank to keep the old value.")

    name = input("Enter New Name: ").strip()

    if name:
        patient["Name"] = name

    age_input = input("Enter New Age: ").strip()

    if age_input:
        try:
            age = int(age_input)

            if age < 0 or age > 120:
                print("Invalid age. Patient not updated.")
                return

            patient["Age"] = age

        except ValueError:
            print("Invalid age. Patient not updated.")
            return

    disease = input("Enter New Disease: ").strip()

    if disease:
        patient["Disease"] = disease

    doctor = input("Enter New Doctor: ").strip()

    if doctor:
        patient["Doctor"] = doctor

    save_patients(patients)

    print(patient_id, "updated successfully.")


# Delete patient
def delete_patient():
    patients = load_patients()

    patient_id = input("Enter Patient ID: ").strip().upper()

    if patient_id in patients:
        del patients[patient_id]

        save_patients(patients)

        print(patient_id, "deleted successfully.")
        print("Total patients:", len(patients))

    else:
        print("Patient ID not found.")


# Main menu
while True:

    print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
    print("1. Add Patient")
    print("2. View All Patients")
    print("3. Search Patient")
    print("4. Update Patient")
    print("5. Delete Patient")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_patient()

    elif choice == "2":
        view_patients()

    elif choice == "3":
        search_patient()

    elif choice == "4":
        update_patient()

    elif choice == "5":
        delete_patient()

    elif choice == "6":
        print("Thank you for using Hospital Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
