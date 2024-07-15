import csv

books_in_library = [
    {
        'title': 'Book_one',
        'authors': ['Author_one'],
        'isbn': '12345-543',
        'publishing_year': 2000,
        'price': 200.00,
        'quantity': 20
    },

    {
        'title': 'Book_two',
        'authors': ['Author_two'],
        'isbn': '56789-768',
        'publishing_year': 2010,
        'price': 208.00,
        'quantity': 25
    },

    {
        'title': 'Book_three',
        'authors': ['Author_three'],
        'isbn': '127658-897',
        'publishing_year': 2014,
        'price': 215.00,
        'quantity': 15
    }
]

books_lend = [

    {
        'title': 'Book_one',
        'name': 'Alice',
        'quantity': 2
    }
]

def add_book():
    title = input('Enter book title: ')
    authors = input('Enter authors by space: ').split(' ')
    isbn = input('Enter ISBN of book: ')
    publishing_year = int(input('Enter book publishing year: '))
    price = float(input('Enter book price: '))
    quantity = int(input('Enter quantity: '))

    book = {
        'title': title,
        'authors': authors,
        'isbn': isbn,
        'publishing_year': publishing_year,
        'price': price,
        'quantity': quantity
    }

    books_in_library.append(book)

    print('Book added successfully!')


def view_all_books():
    for book in books_in_library:
        print(
            book['title'], 
            book['authors'], 
            book['isbn'], 
            book['publishing_year'], 
            book['price'], 
            book['quantity'], 
            sep=' | ')


def search_by_title_isbn():
    search_term = input('Enter book title or ISBN: ')

    for book in books_in_library:
        if search_term.lower() in book['title'].lower() or search_term in book['isbn']:
            print(f"Found: {book['title']} - {book['authors']} - {book['isbn']}")


def search_by_authors():
    search_term = input('Enter book authors: ')

    for book in books_in_library:
        if search_term.lower() in book['authors'].lower():
            print(f"Found: {book['title']} - {book['authors']}")


def remove_book():
    search_term = input('Enter text to search to remove: ')

    for index, book in enumerate(books_in_library):
        if search_term.lower() in book['title'].lower():
            print(f"{index+1}. {book['title']} - {book['authors']}")

    selected_index = int(input('Enter a book title to remove: '))

    books_in_library.pop(selected_index - 1)

    print('Contact remove successfully!')


def lend_books():

    book_title = input('Enter book title to lend(ex. Book_one): ')
    borrower_name =input('Enter borrower name(ex. Alice): ')
    quantity = int(input('Enter quantity of book(eg. 1): '))

    for book in books_in_library:
        if book_title == book['title']:
            if book['quantity'] == 0:
                print('Not enough books available to lend.')

            else:
                book['quantity'] -= quantity
                print(f'Books remains: {book["quantity"]}')

    lended_book = {
        'title': book_title,
        'name': borrower_name,
        'quantity': quantity
    }

    books_lend.append(lended_book)

    print(books_lend)


def view_lended_book():
    for book in books_lend:
        print(
            book['title'],
            book['name'],
            book['quantity'],
            sep=' | '
        )


def book_return():

    book_title = input('Enter book title to return(ex. Book_one): ')
    borrower_name =input('Enter borrower name(ex. Alice): ')
    quantity = int(input('Enter quantity of book(eg. 1): '))

    returned_book = {
        'title': book_title,
        'name': borrower_name,
        'quantity': quantity
    }
    
    print(returned_book)

    for book in books_in_library:
        if book_title == book['title']:
            book['quantity'] += quantity
            print(f'Books remains: {book["title"]} | {book["quantity"]}')


def backup_books():
    
    with open('books.csv', 'w', newline='') as file:

        fieldnames = ["title", "authors", "isbn", "publishing_year", "price", "quantity"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
    
        writer.writeheader()
        writer.writerows(books_in_library)

    with open('books_lend.csv', 'w', newline='') as file:
        fieldnames = ["title", "name", "quantity"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
    
        writer.writeheader()
        writer.writerows(books_lend)

    print('Books are backuped!')

print('Welcome!')

menu_text = """
Your options:
1. Add book
2. View all books
3. Search by title or ISBN
4. Search by authors
5. Remove book
6. Lend books
7. View lended books
8. Book return
9. Backup books
0. Exit
"""

while True:
    print(menu_text)
    choice = input('Enter your choice: ')

    if choice == '1':
        add_book()

    elif choice == '2':
        view_all_books()

    elif choice == '3':
        search_by_title_isbn()

    elif choice == '4':
        search_by_authors()

    elif choice == '5':
        remove_book()

    elif choice == '6':
        lend_books()

    elif choice == '7':
        view_lended_book()

    elif choice == '8':
        book_return()

    elif choice == '9':
        backup_books()

    elif choice == '0':
        break
    
    else:
        print('Wrong choice!')