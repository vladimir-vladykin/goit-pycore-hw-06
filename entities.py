from collections import UserDict

PHONE_LENGTH = 10

# Base class for fields in Records.
# Implements holding of some data as string,
# and rendering of this data via __str__ method.
class Field:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

# Name of user.
# Note that name cannot be empty, exception will be raised otherwise.
class Name(Field):
	
    def __init__(self, name: str):
        if len(name) == 0:
            raise ValueError("Empty name is not supported")
        
        super().__init__(name)
    

# Phone of user.
# Note that it's strongly required that phone contains only numbers, and exactly
# 10 numbers. Exception will be thrown if this condition is not fulfilled.
class Phone(Field):
    def __init__(self, phone: str):
        if len(phone) != PHONE_LENGTH:
            raise ValueError(f"Phone length is not correct, it supposed to have {PHONE_LENGTH} symbols")
        
        if not phone.isdigit():
            raise ValueError("Phone number is supposed to contain only digits")

        super().__init__(phone)

    # matters for indexing in list of phones
    def __eq__(self, other):
        return self.value == other.value
        

# One Record corresponds to single user, contains name and can contain some phone numbers
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    # Note that phone sould contain only numbers and have exactly 10 symbols
    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        self.phones.remove[Phone(phone)]

    def edit_phone(self, phone: str, new_phone: str):
        # since Phone implements __eq__(), it's easy to work with list of Phones
        phone_object = Phone(phone)
        if phone_object not in self.phones:
            # we don't have such phone, therefore it's cannot be edited
            return
        
        # replace old phone object with new one
        existing_phone_index = self.phones.index(phone_object)
        self.phones[existing_phone_index] = Phone(new_phone)
        

    def find_phone(self, phone: str) -> Phone:
        for maybe_phone in self.phones:
            if maybe_phone.value == phone:
                return maybe_phone
    


# Contains all info about users and their phone numbers.
# Raw user's name is a key for each record
class AddressBook(UserDict):
       
    def add_record(self, record: Record):
        self.data[record.name.value] = record
    
    def find(self, name: str) -> Record:
        return self.data.get(name)
    
    def delete(self, name: str):
        if name not in self.data:
            # unknown name, nothing to remove
            return 
        
        self.data.pop(name)