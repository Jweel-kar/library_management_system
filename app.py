books_in_library = [
    
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

    with open('books.csv', 'a') as file_pointer:
        book_line = f"{book['title']},{book['authors']},{book['isbn']},{book['publishing_year']},{book['price']},{book['quantity']}\n"
        file_pointer.write(book_line)

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

    with open('books_lend.csv', 'a') as file_pointer:
        book_line = f"{lended_book['title']},{lended_book['name']},{lended_book['quantity']}\n"
        file_pointer.write(book_line)

    # books_lend.append(lended_book)

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
    
    with open('books.csv', 'w') as file_pointer:
        for books in books_in_library:
            book_line = f"{books['title']},{books['authors']},{books['isbn']},{books['publishing_year']},{books['price']},{books['quantity']}\n"
            file_pointer.write(book_line)

    with open('books_lend.csv', 'w') as file_pointer:
        for book in books_lend:
            book_lines = f"{book['title']},{book['name']},{books['quantity']}\n"
            file_pointer.write(book_lines)

    print('Books are backuped!')


def restore_books():

    books_in_library.clear()


    with open('books.csv', 'r') as file_pointer:
        for line in file_pointer.readlines():
            line_splitted = line.split()
            
            books = {
                'title': line_splitted[0],
                'authors': line_splitted[1],
                'isbn': line_splitted[2],
                'publishing_year': line_splitted[3],
                'price': line_splitted[4],
                'quantity': line_splitted[5]
            }

            books_in_library.append(books)

    print('Contact restored successfully!')

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
10. Restore books
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

    elif choice == '10':
        restore_books()

    elif choice == '0':
        break
    
    else:
        print('Wrong choice!')