from Book import Book
from Client import Client

book_list = []
book1 = [Book(101, "Orientalism", "Orientalism ", "Edward W. Said", False)]
book2 = [Book(102, "History of Palestine", "Talks about the history of Palestine, and it's historical people",
              "Ali Alhaj", True)]
book3 = [Book(103, "Engineering Physics", "A teaching book taught to the engineering students in all fields",
              "Abdul-Karim Sahmoud", True)]
book_list.__add__(book1)
book_list.__add__(book2)
book_list.__add__(book3)
client_list = []

client1 = [Client(201, "Mohammad Mahmoud Alhirthani", 20, "90095782", "00970567845291", "mo7ameh.202gmail.com")]
client2 = [Client(201, "Ali Omar Jaber", 36, "400598756", "009705244125786", "ali_omar36@outlook.com")]
client3 = [Client(201, "Hassan Alaa' Hussain", 42, "957854120", "00970584275869", "hassan@gmail.com")]
client_list.__add__(client1)
client_list.__add__(client2)
client_list.__add__(client3)


def choice1():
    print("********* Welcome to Library *********")
    choice = int(input("Who is using this platform? "
                       "\n1.Client Account"
                       "\n2.Librarian Account"
                       "\n3.Exit\n"))
    if choice == 1:
        client()
        pass
    elif choice == 2:
        librarian()
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        exit()
    else:
        print("Invalid Entry")
        choice1()


def librarian():
    print("Enter Username And Password")
    user = "1"
    password = "1"
    input_user = input("Enter Username: ")
    input_password = input("Enter Password: ")
    if input_user.__eq__(user) and input_password.__eq__(password):
        print("Welcome Librarian ")




        # for i in range(len(book_list)):
        #     print(book_list[i])
        #     search_id = int(input("Enter Book id:   "))
        #
        #     if search_id == book_list[i.Book.get_id()]:
        #         print(book_list[i.Book.get_id()])
        #     else:
        #         print("Book NOT Found!!")


def client():
    client_id = int(input("Enter your ID:   "))
    for y in range(len(client_list)):
        if client_id == client_list[y.Client.get_id()]:
            print("Welcom ", y.Client.get_id())
choice1()
