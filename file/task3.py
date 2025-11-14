#write a python code on book system 
#make function and store the data in dictionaries atleast five books
#user call the number of the book and that book need to be displayed


def book_system():
    books = {
        1: "English",
        2: "Mathematics",
        3: "Science",
        4: "History",
        5: "Geography"
    }
    print("Available Books:")
    number = int(input("Enter the number of the book you want to select (1-5): "))
    print("You have selected book:",number, books[number])
    if number in books:
        print(f"{number}. {books[number]}")
    else:
        print("Invalid book number. Please select a number between 1 and 5.")
book_system()




