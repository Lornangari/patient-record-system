import sqlite3
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

if __name__ == "__main__":
    init_db()

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
    print("Patient added successfully.\n")

add_patient()    

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
view_patients()


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
search_patient()


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
    print("Record updated.\n")
update_patient()


#delete patient
def delete_patient():
    patient_id = int(input("Enter patient ID to delete: "))

    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM patients WHERE id=?", (patient_id,))
    conn.commit()
    conn.close()
    print("Record deleted.\n")
delete_patient()



