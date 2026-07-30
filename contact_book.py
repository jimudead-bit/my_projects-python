contacts = {"Noor": "03459689750", "Tabeer": "03288709795", "Mehdi": "03115048994", "Ayan": "03782746294"}

while True:
    print("========📞 Contact Book ========")
    print()
    print("1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")
    print()

    choice = input("Enter your choice (use only numbers): ").strip()

    if choice == "1":
        contact_name = input("Enter contact name: ").strip().title()
        contact_no = input("Enter contact number: ")
        contacts[contact_name] = contact_no
        print()
        print(f"{contact_name} has been added to the contact book.")
    elif choice == "2":
        if contacts:
            for contact_name, contact_no in contacts.items():
                print(f"{contact_name} : {contact_no}")
        else:
            print("No contacts found!")
    elif choice == "3":
        contact_name = input("Enter contact name: ").strip().title()
        print()

        if contact_name in contacts:
            print(f"{contact_name}'s contact number is {contacts[contact_name]}.")
        else:
            print("Contact not found!")
    elif choice == "4":
        new_contact_name = input("Enter contact name: ").strip().title()

        if new_contact_name in contacts:
            new_contact_no = input("Enter updated contact number: ")
            contacts[new_contact_name] = new_contact_no
            print()
            print(f"{new_contact_name} has been updated in the 📞contact book.")
        else:
            print("Contact not found!")
    elif choice == "5":
        delete_name = input("Enter contact to be deleted: ").strip().title()
        print()

        if delete_name in contacts:
            del contacts[delete_name]
            print(f"{delete_name} has been deleted from 📞contact book.")
        else:
            print("Contact not found!")
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, use only numbers.")

    input("Press Enter to continue...")


input("Press Enter to exit...")
