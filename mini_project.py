records = []

def add_record():
    vehicle_no = input("Enter Vehicle Number: ")
    owner_name = input("Enter Owner Name: ")
    vehicle_model = input("Enter Vehicle Model: ")
    service_date = input("Enter Service Date (YYYY-MM-DD): ")
    service_type = input("Enter Service Type: ")
    cost = float(input("Enter Service Cost: "))

    record = {
        "vehicle_no": vehicle_no,
        "owner_name": owner_name,
        "vehicle_model": vehicle_model,
        "service_date": service_date,
        "service_type": service_type,
        "cost": cost
    }

    records.append(record)
    print("Record added successfully!")

def view_records():
    if len(records) == 0:
        print("No records found!")
    else:
        for record in records:
            print(record)

def search_record():
    vehicle_no = input("Enter Vehicle Number: ")

    for record in records:
        if record["vehicle_no"] == vehicle_no:
            print(record)
            return

    print("Vehicle not found!")

def update_record():
    vehicle_no = input("Enter Vehicle Number: ")

    for record in records:
        if record["vehicle_no"] == vehicle_no:
            record["service_type"] = input("Enter New Service Type: ")
            record["cost"] = float(input("Enter New Service Cost: "))

            print("Record updated successfully!")
            return

    print("Vehicle not found!")

def delete_record():
    vehicle_no = input("Enter Vehicle Number: ")

    for record in records:
        if record["vehicle_no"] == vehicle_no:
            records.remove(record)
            print("Record deleted successfully!")
            return

    print("Vehicle not found!")

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
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
