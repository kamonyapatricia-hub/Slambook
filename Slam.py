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

def delete_all():

    slam_book.clear()
    print("All contacts deleted")

def menu():
        
        while True:
            print("\n==========SLAMBOOK============")
            print("1. Add contact")
            print("2.Display contact")
            print("3.Search contact")
            print("4.Delete all")
            print("5.Exit")

            choice=input("Choose an option:")

            if choice == "1":
                add_contact()
            elif choice == "2":
                display_contact()
            elif choice == "3":
                search_contact()
            elif choice == "4":
                delete_all()
            elif choice =="5":
                print("Thank you for using the slambook")
                sys.exit()
            else:
                print("Invalid choice!!")

menu()