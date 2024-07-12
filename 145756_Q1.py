patients = []

def add_patient(name, age, illness):
    patient = {'name': name, 'age': age, 'illness': illness}
    patients.append(patient)
    print(f"Patient {name} added successfully.")

def display_all_patients():
    if patient not in patients:
        print("No patients found.")
    else:
        for idx, patient in enumerate(patients):
            print(f"Patient {idx + 1}: Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")

def search_patient_by_name(name):
    found = False
    for patient in patients:
        if patient['name'].lower() == name.lower():
            print(f"Patient found: Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")
            found = True
            break
    if not found:
        print(f"No patient found with the name {name}.")

def remove_patient_name(name):
    
    Patients list
    updated_patients = [patient for patient in patients if patient['name'].lower() != name.lower()]
    if len(updated_patients) == len(patients):
        print(f"No patient found with the name {name}.")
    else:
        patients = updated_patients
        print(f"Patient {name} removed successfully.")

def main():
    while True:
        print("Patient Management System")
        print("1. Add a new patient")
        print("2. Display all patients")
        print("3. Search for a patient by name")
        print("4. Remove a patient by name")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter patient's name: ")
            age = input("Enter patient's age: ")
            illness = input("Enter patient's illness: ")
            add_patient(name, age, illness)
        elif choice == '2':
            display_all_patients()
        elif choice == '3':
            name = input("Enter patient's name to search: ")
            search_patient_by_name(name)
        elif choice == '4':
            name = input("Enter patient's name to remove: ")
            remove_patient_by_name(name)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()