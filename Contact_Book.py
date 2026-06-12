
### Project 5: Contact Book 

contacts = []

while True:

    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")

        contact = {
            "name": name,
            "phone": phone
        }

        contacts.append(contact)

        print("Contact Added Successfully!")

    elif choice == "2":

        if len(contacts) == 0:
            print("No Contacts Found")

        else:
            print("\nAll Contacts")

            for contact in contacts:
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("----------------")

    elif choice == "3":

        search_name = input("Enter Name to Search: ")

        found = False

        for contact in contacts:

            if contact["name"].lower() == search_name.lower():

                print("Contact Found")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])

                found = True
                break

        if not found:
            print("Contact Not Found")

    elif choice == "4":

        print("Thank You!")
        break

    else:

        print("Invalid Choice")
