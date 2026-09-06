import mysql.connector

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="vehicle_service"
)

cursor = db.cursor()


def add_record():
    vehicle_no = input("Enter Vehicle Number: ")
    owner_name = input("Enter Owner Name: ")
    vehicle_model = input("Enter Vehicle Model: ")
    service_date = input("Enter Service Date (YYYY-MM-DD): ")
    service_type = input("Enter Service Type: ")
    cost = float(input("Enter Service Cost: "))

    sql = """INSERT INTO service_records
             (vehicle_no, owner_name, vehicle_model, service_date, service_type, cost)
             VALUES (%s, %s, %s, %s, %s, %s)"""

    values = (vehicle_no, owner_name, vehicle_model,
              service_date, service_type, cost)

    cursor.execute(sql, values)
    db.commit()

    print("Record added successfully!")


def view_records():
    cursor.execute("SELECT * FROM service_records")
    records = cursor.fetchall()

    for record in records:
        print(record)


def search_record():
    vehicle_no = input("Enter Vehicle Number: ")

    cursor.execute(
        "SELECT * FROM service_records WHERE vehicle_no = %s",
        (vehicle_no,)
    )

    records = cursor.fetchall()

    if records:
        for record in records:
            print(record)
    else:
        print("Vehicle not found!")


def update_record():
    vehicle_no = input("Enter Vehicle Number: ")
    cost = float(input("Enter New Service Cost: "))
    service_type = input("Enter New Service Type: ")

    sql = """UPDATE service_records
             SET cost = %s, service_type = %s
             WHERE vehicle_no = %s"""

    cursor.execute(sql, (cost, service_type, vehicle_no))
    db.commit()

    print("Record updated successfully!")


def delete_record():
    vehicle_no = input("Enter Vehicle Number: ")

    cursor.execute(
        "DELETE FROM service_records WHERE vehicle_no = %s",
        (vehicle_no,)
    )

    db.commit()

    print("Record deleted successfully!")


while True:
    print("\n--- Vehicle Service Record Management System ---")
    print("1. Add Record")
    print("2. View Records")
    print("3. Search Vehicle")
    print("4. Update Record")
    print("5. Delete Record")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_record()

    elif choice == "2":
        view_records()

    elif choice == "3":
        search_record()

    elif choice == "4":
        update_record()

    elif choice == "5":
        delete_record()

    elif choice == "6":
        break

    else:
        print("Invalid choice!")

cursor.close()
db.close()
