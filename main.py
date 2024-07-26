from entities import *

def main():
    book = AddressBook()

    # Create John's recor
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Add John to AdressBook
    book.add_record(john_record)

    # Create and add Jane's record
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Output all records in AddressBook
    print("Output Address Book after first initialization:")
    for name, record in book.data.items():
        print(record)

    # Find and edit John's phone number
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(f"Jonh after editing of phone numbers: {john}")  # Output: Contact name: John, phones: 1112223333; 5555555555

    # check for non-existing phone
    john.edit_phone("0123456789", "1112223333")
    print(f"Jonh after trying to edit non-existing phone number: {john}")

    # Search for specific John's Phone 
    found_phone = john.find_phone("5555555555")
    print(f"Found phone of {john.name}'s: {found_phone}")  # Output: 5555555555

    # Remove Jane's record
    book.delete("Jane")

     # Output all after deleting to ensure Jane is missing
    print("Output all after Jane is deleted from Address Book:")
    for name, record in book.data.items():
        print(record)



if __name__ == "__main__":
    # run program
    main()