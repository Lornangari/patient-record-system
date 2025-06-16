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


