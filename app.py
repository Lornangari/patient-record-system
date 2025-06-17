import sqlite3
import csv
#clinic database and patients table
def init_db():
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            diagnosis TEXT,
            medication TEXT,
            visit_date TEXT
        )
    ''')
    conn.commit()
    conn.close()

#csv
def refresh_csv():
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")
    records = cursor.fetchall()
    conn.close()

    with open("patients.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Age", "Diagnosis", "Medication", "Visit Date"])  
        writer.writerows(records)




#add a new patient
def add_patient():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    diagnosis = input("Enter diagnosis: ")
    medication = input("Enter medication: ")
    visit_date = input("Enter visit date (YYYY-MM-DD): ")

    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO patients (name, age, diagnosis, medication, visit_date) VALUES (?, ?, ?, ?, ?)",
                   (name, age, diagnosis, medication, visit_date))
    conn.commit()
    conn.close()

    refresh_csv()
    print("Patient added successfully.\n")
    

#view all patients
def view_patients():
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")
    records = cursor.fetchall()
    conn.close()

    print("\n--- All Patients ---")
    for row in records:
        print(row)
    print()


#search patient
def search_patient():
    name = input("Enter name to search: ")
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients WHERE name LIKE ?", ('%' + name + '%',))
    records = cursor.fetchall()
    conn.close()

    print("\n--- Search Results ---")
    for row in records:
        print(row)
    print()


#update patient
def update_patient():
    patient_id = int(input("Enter patient ID to update: "))
    diagnosis = input("New diagnosis: ")
    medication = input("New medication: ")
    visit_date = input("New visit date (YYYY-MM-DD): ")

    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE patients SET diagnosis=?, medication=?, visit_date=? WHERE id=?",
                   (diagnosis, medication, visit_date, patient_id))
    conn.commit()
    conn.close()

    refresh_csv()
    print("Record updated.\n")


#delete patient
def delete_patient():
    patient_id = int(input("Enter patient ID to delete: "))

    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM patients WHERE id=?", (patient_id,))
    conn.commit()
    conn.close()
    
    refresh_csv()
    print("Record deleted.\n")


#main menuloop
def menu():
    while True:
        print("=== Patient Record System ===")
        print("1. Add Patient")
        print("2. View All Patients")
        print("3. Search Patient")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_patient()
        elif choice == '2':
            view_patients()
        elif choice == '3':
            search_patient()
        elif choice == '4':
            update_patient()
        elif choice == '5':
            delete_patient()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    init_db()
    menu()



