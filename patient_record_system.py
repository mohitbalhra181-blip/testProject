patients = {}  # id -> {"name": str, "phone": int, "address": str}


def add_patient():
    pid = int(input("Enter the id: "))
    name = input("Enter the name: ")
    phone = int(input("Enter the phone number: "))
    address = input("Enter the address: ")

    if pid in patients:
        print("Patient already exists. Use update option.")
        return

    patients[pid] = {
        "name": name,
        "phone": phone,
        "address": address,
    }
    print("Patient added successfully")


def view_patient():
    pid = int(input("Enter the id: "))

    if pid in patients:
        p = patients[pid]
        print("Patient record found")
        print("ID:", pid)
        print("Name:", p["name"])
        print("Phone:", p["phone"])
        print("Address:", p["address"])
    else:
        print("Patient record not found")


def update_patient():
    pid = int(input("Enter the id: "))

    if pid in patients:
        name = input("Enter the new name: ")
        phone = int(input("Enter the new phone number: "))
        address = input("Enter the new address: ")

        patients[pid] = {
            "name": name,
            "phone": phone,
            "address": address,
        }
        print("Patient record updated successfully")
    else:
        print("Patient record not found")


def delete_patient():
    pid = int(input("Enter the id: "))

    if pid in patients:
        del patients[pid]
        print("Patient record deleted successfully")
    else:
        print("Patient record not found")


while True:
    print("\n(press 1 for add patient record)")
    print("(press 2 for view patient record)")
    print("(press 3 for update patient record)")
    print("(press 4 for delete patient record)")
    print("(press 0 to exit)")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_patient()
    elif choice == 2:
        view_patient()
    elif choice == 3:
        update_patient()
    elif choice == 4:
        delete_patient()
    elif choice == 0:
        print("Exiting...")
        break
    else:
        print("Invalid choice")

