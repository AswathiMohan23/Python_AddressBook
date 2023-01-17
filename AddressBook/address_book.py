print("\n\t\t\t\t\t\t\t\t\t WELCOME TO ADDRESSBOOK \n\t\t\t\t\t\t\t\t  ***************************\n")


def adding_data_from_console(contact):
    print("\n------------------------------------------ UC5 (refactored UC2 to add multiple contacts) ----------------------------------------------------------------------\n")
    limit = int(input("Enter the no of contacts you need to add to the contact book : "))
    for i in range (0,limit):
        print("\nenter the details of contact ", i+1)
        data = adding_details()
        contact.append(data)


def display_contactBook(contact):
    print("\t\t\t\t\t---------------- Existing contact book ------------------------ \n\n", contact)


def adding_details():
    first_name = input("Enter the first name : ")
    second_name = input("Enter the second name : ")
    address = input("Enter the address : ")
    city = input("Enter the city : ")
    state = input("Enter the state : ")
    zip_code = input("Enter the zip_code : ")
    phn = input("Enter the phone number : ")
    email = input("Enter the email : ")
    data={"first_name": first_name, "second_name": second_name, "address": address, "city": city, "state": state,
         "zip_code": zip_code, "phn": phn, "email": email}
    return data


def edit_data(contact):
    print("\n------------------------------------------------------ UC3 ----------------------------------------------------------------------\n")
    name_to_be_edited = input("enter the first name to edit the contact : ")
    for dict in contact:
        for lst in dict:
            if dict.get(lst) == name_to_be_edited:
                data = adding_details()
                dict.update(data)
                return dict


def delete_contact():
    print("\n------------------------------------------------------ UC4 ----------------------------------------------------------------------\n")
    name_to_be_deleted = input("enter the first name of the person whose details should be deleted : ")
    if name_to_be_deleted == person1.get('first_name'):
        contact.remove(person1)
        after_deletion(contact,name_to_be_deleted)
    elif name_to_be_deleted == person2.get('first_name'):
        contact.remove(person2)
        after_deletion(contact,name_to_be_deleted)


def after_deletion(contact, name):
    print("\n******************************* After deleting details of", name, " ******************************\n")
    display_contactBook(contact)


"""def get_value(contact, key):
    result = [i[key] for i in contact]
    if result == 'Tom':
        data=adding_details()
        contact.index()
    return result"""


def get_value(lst, key, value):
    for i, contact in enumerate(lst):
        if contact[key] == value:
            data = adding_details();
            return data


# ------------------------------------------------------------------------------------------------------------------

print("------------------------------------------------------ UC1 ----------------------------------------------------------------------\n")
contact = []
person1 = {"first_name": "Tom", "second_name": "John", "address": "Abc Apartment", "city": "Bangalore",
               "state": "Karnataka", "zip_code": "123456", "phn": "91 9495123456", "email": "tom@gmail.com"}
person2 = {"first_name": "Ravi", "second_name": "Dev", "address": "pq villa", "city": "Kochi", "state": "Kerala",
               "zip_code": "120056", "phn": "91 9491122956", "email": "ravi@yahoo.com"}
contact.append(person1)
contact.append(person2)
display_contactBook(contact)

adding_data_from_console(contact)

display_contactBook(contact)
new_data=edit_data(contact)
contact.append(new_data)
display_contactBook(contact)
delete_contact()
