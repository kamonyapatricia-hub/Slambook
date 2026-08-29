import sys

slam_book = []

def add_contact():
    name=input("Enter name :")

    if name =="":
        sys.exit("Name cannot be empty!")

        number = input("Enter phone number:")
        email=input("Enter email:")

        contact = [name,number,email]
        slam_book.append(contact)

        print("Contact added")
def display_contact():
    if len(slam_book)==0:
        print("slambook is empty!")
    else:
        print("\n--------Contact------------")
        for contact in slam_book:
          print("Name :",contact[0])
          print("Number :",contact[1])
          print("Email :",contact[2])
          print()


def search_contact():
    name = input("Enter the name to search :").lower()

    for contact in slam_book:

        if contact[0] == name:
         
            print("contact Found!")
            print("Name: ",contact[0])
            print("Number: ", contact[1])
            print("Email: ", contact[2])
            return

    print("Contact not found!")
