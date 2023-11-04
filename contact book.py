class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contact_list(self):
        for contact in self.contacts:
            print(f"{contact.name} - {contact.phone_number}")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact

    def update_contact(self, contact, new_name, new_phone_number, new_email, new_address):
        contact.name = new_name
        contact.phone_number = new_phone_number
        contact.email = new_email
        contact.address = new_address

    def delete_contact(self, contact):
        self.contacts.remove(contact)


def main():
    contact_book = ContactBook()

    while True:
        command = input("Enter a command (add, view, search, update, delete, or exit): ")

        if command == "add":
            name = input("Enter the contact's name: ")
            phone_number = input("Enter the contact's phone number: ")
            email = input("Enter the contact's email address: ")
            address = input("Enter the contact's address: ")

            contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(contact)

        elif command == "view":
            contact_book.view_contact_list()

        elif command == "search":
            name = input("Enter the contact's name: ")

            contact = contact_book.search_contact(name)

            if contact is not None:
                print(f"Name: {contact.name}")
                print(f"Phone number: {contact.phone_number}")
                print(f"Email: {contact.email}")
                print(f"Address: {contact.address}")
            else:
                print("Contact not found.")

        elif command == "update":
            name = input("Enter the contact's name: ")

            contact = contact_book.search_contact(name)

            if contact is not None:
                new_name = input("Enter the new contact name: ")
                new_phone_number = input("Enter the new contact phone number: ")
                new_email = input("Enter the new contact email address: ")
                new_address = input("Enter the new contact address: ")

                contact_book.update_contact(contact, new_name, new_phone_number, new_email, new_address)
            else:
                print("Contact not found.")

        elif command == "delete":
            name = input("Enter the contact's name: ")

            contact = contact_book.search_contact(name)

            if contact is not None:
                contact_book.delete_contact(contact)
            else:
                print("Contact not found.")

        elif command == "exit":
            break

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
