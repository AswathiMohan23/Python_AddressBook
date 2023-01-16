print("\n\t\t\t\t\t\t\t\t WELCOME TO ADDRESSBOOK \n\t\t\t\t\t\t\t  ***************************\n")

contact = []
person1 = {"first_name": "Tom", "second_name": "John", "address": "Abc Apartment", "city": "Bangalore", "state": "Karnataka", "zip_code": "123456", "phn": "91 9495123456", "email": "tom@gmail.com"}
person2 = {"first_name": "Ravi", "second_name": "Dev", "address": "pq villa", "city": "Kochi", "state": "Kerala", "zip_code": "120056", "phn": "91 9491122956", "email": "ravi@yahoo.com"}
contact.append(person1)
contact.append(person2)
person3 = {}

print("-------------------------------------------- UC2 ---------------------------------------------------\n")

print("\t\t\t\t\t---------------- Existing contact book ------------------------ \n\n", contact)
first_name = input("Enter the first name : ")
second_name = input("Enter the first name : ")
address = input("Enter the address : ")
city = input("Enter the city : ")
state = input("Enter the state : ")
zip_code = input("Enter the zip_code : ")
phn = input("Enter the phone number : ")
email = input("Enter the email : ")
person3.update({"first_name": first_name, "second_name": second_name, "address": address, "city": city, "state": state,
                "zip_code": zip_code, "phn": phn, "email": email})
print(person3)