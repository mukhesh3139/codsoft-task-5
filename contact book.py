class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contact_list(self):
        print("Contact List:")
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contact(self, keyword):
        results = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
                results.append(contact)
        return results

    def update_contact(self, contact_name, new_phone_number):
        for contact in self.contacts:
            if contact.name.lower() == contact_name.lower():
                contact.phone_number = new_phone_number
                print("Contact updated successfully!")
                return
        print("Contact not found.")

    def delete_contact(self, contact_name):
        for contact in self.contacts:
            if contact.name.lower() == contact_name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                return
        print("Contact not found.")

def user_interface():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_manager.add_contact(new_contact)

        elif choice == "2":
            contact_manager.view_contact_list()

        elif choice == "3":
            keyword = input("Enter name or phone number to search: ")
            results = contact_manager.search_contact(keyword)
            if results:
                print("Search Results:")
                for contact in results:
                    print(f"Name: {contact.name}, Phone: {contact.phone_number}")
            else:
                print("No contacts found.")

        elif choice == "4":
            contact_name = input("Enter the name of the contact to update: ")
            new_phone_number = input("Enter the new phone number: ")
            contact_manager.update_contact(contact_name, new_phone_number)

        elif choice == "5":
            contact_name = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact(contact_name)

        elif choice == "6":
            print("Exiting Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    user_interface()
