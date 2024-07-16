from backup_restore import books_in_library, lended_books, backup_books, backup_lent_books, restore_books, restore_lent_books
from utility import validate_price

def add_book():
    title = input('Enter book title: ')
    authors = input('Enter authors by space: ').split(' ')
    isbn = input('Enter ISBN of book: ')
    publishing_year = int(input('Enter book publishing year: '))
    price = float(input('Enter book price: '))
    quantity = int(input('Enter quantity: '))

    if not validate_price(price):
        print("Error: Price should be a floating number.")
        return

    book = {
        'title': title,
        'authors': authors,
        'isbn': isbn,
        'publishing_year': publishing_year,
        'price': price,
        'quantity': quantity
    }

    books_in_library.append(book)
    
    backup_books()

    print('Book added successfully!')


def view_all_books():
    
    try:
        for book in books_in_library:
            print(
                book['title'], 
                book['authors'], 
                book['isbn'], 
                book['publishing_year'], 
                book['price'], 
                book['quantity'], 
                sep=' | ')

    except:
        print('No book available to view!')


def search_by_title_isbn():
    
    try:
        search_term = input('Enter book title or ISBN: ')

        for book in books_in_library:
            if search_term.lower() in book['title'].lower() or search_term in book['isbn']:
                print(f"Found: {book['title']} - {book['authors']} - {book['isbn']}")

        else:
            print('No such books available!')

    except:
        print('No such books available!')


def search_by_authors():
    
    try:
        search_term = input('Enter book authors: ')

        for book in books_in_library:
            for authors in book['authors']:
                if search_term.lower() in authors.lower():
                    print(f"Found: {book['title']} - {book['authors']}")

        else:
            print('No such book available!')

    except:
        print('No such book available!')


def remove_book():
    
    search_term = input('Enter text to search to remove: ')

    for index, book in enumerate(books_in_library):
        if search_term.lower() in book['title'].lower():
            print(f"{index+1}. {book['title']} - {book['authors']}")

    selected_index = int(input('Enter a book number to remove: '))

    books_in_library.pop(selected_index - 1)

    print('Book removed successfully!')


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

                lended_books.append(lended_book)

                backup_lent_books()
                print(f'{lended_book["title"]} {lended_book["quantity"]} copies lended successfully!')


def view_lent_book():
    
    try:
        for book in lended_books:
            print(
                book['title'],
                book['name'],
                book['quantity'],
                sep=' | '
            )
    except:
        print('No books lent!')


def book_return():

    book_title = input('Enter book title to return(ex. Book_one): ')
    borrower_name =input('Enter borrower name(ex. Alice): ')
    quantity = int(input('Enter quantity of book(eg. 1): '))

    returned_book = {
        'title': book_title,
        'name': borrower_name,
        'quantity': quantity
    }

    for book in books_in_library:
        if book_title == book['title']:
            book['quantity'] += quantity
            print(f'Books remains: {book["title"]} | {book["quantity"]}')

    backup_books()

    for books in lended_books:
        if books['title'] == returned_book['title'] and books['quantity'] == returned_book['quantity']:
            lended_books.remove(books)

        elif books['title'] == returned_book['title']:
            books['quantity'] -= quantity


    backup_lent_books()


print('Welcome!')

menu_text = """
Your options:
1. Add book
2. View all books
3. Search by title or ISBN
4. Search by authors
5. Remove book
6. Lend books
7. View lent books
8. Book return
9. Backup books
10. Backup lent books
11. Restore books
12. Restore lent books
0. Exit
"""

def main_menu():
    restore_books()
    restore_lent_books()

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
            view_lent_book()

        elif choice == '8':
            book_return()

        elif choice == '9':
            backup_books()

        elif choice == '10':
            backup_lent_books()

        elif choice == '11':
            restore_books()

        elif choice == '12':
            restore_lent_books()

        elif choice == '0':
            break
        
        else:
            print('Wrong choice!')

main_menu()