#Leonardo Nava 
# 9/11/24
#the driver file to make the program run5

import contacts


def main():
    #make a clean contacts list
    contacts_list = []
    #continuously run since True does that
    while True:
        print("\nMenu:")
        print("1. Print Contact List ")
        print("2. Add Contact ")
        print("3. Modify Contact ")
        print("4. Delete Contact ")
        print("5. Sort list by first name")
        print("6. Sort list by last name")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            contacts.print_list(contacts_list)
        elif choice == "2":
            contacts_list = contacts.add_contact(contacts_list)
        elif choice == "3":
            contacts_list = contacts.modify_contact(contacts_list)
        elif choice == "4":
            contacts_list = contacts.delete_contact(contacts_list)
        elif choice == "5":
            contacts_list = contacts.sort_contacts(contacts_list, column=0)
            print("sorted by first name")
        elif choice == "6":
            contacts_list = contacts.sort_contacts(contacts_list, column=1)
            print("sorted by last name")
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again. ")

if __name__ == "__main__":
    main()