books_in_library = [
    {
        'title': 'Book_one',
        'authors': ['Author_one'],
        'isbn': 12345,
        'publishing_year': 2000,
        'price': 200.00,
        'quantity': 20
    },

    {
        'title': 'Book_two',
        'authors': ['Author_two'],
        'isbn': 56789,
        'publishing_year': 2010,
        'price': 208.00,
        'quantity': 25
    },

    {
        'title': 'Book_three',
        'authors': ['Author_three'],
        'isbn': 127658,
        'publishing_year': 2014,
        'price': 215.00,
        'quantity': 15
    }
]


def add_book():
    title = input('Enter book title: ')
    authors = input('Enter authors by space: ').split(' ')
    isbn = int(input('Enter ISBN of book: '))
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


def search_by_title():
    search_term = input('Enter book title: ')

    for book in books_in_library:
        if search_term.lower() in book['title'].lower():
            print(f"Found: {book['title']} - {book['authors']}")


def search_by_authors():
    search_term = input('Enter book authors: ')

    for book in books_in_library:
        if search_term.lower() in book['authors'].lower():
            print(f"Found: {book['title']} - {book['authors']}")


def remove_contact():
    search_term = input('Enter text to search to remove: ')
    for index, book in enumerate(books_in_library):
        if search_term.lower() in book['title'].lower():
            print(f"{index+1}. {book['title']} - {book['authors']}")

    selected_index = int(input('Enter a book title to remove: '))

    books_in_library.pop(selected_index - 1)

    print('Contact remove successfully!')


print('Welcome!')

menu_text = """
Your options:
1. Add book
2. View all books
3. Search by title
4. Search by authors
5. Remove contact
6. Exit
"""

while True:
    print(menu_text)
    choice = input('Enter your choice: ')

    if choice == '1':
        add_book()

    elif choice == '2':
        view_all_books()

    elif choice == '3':
        search_by_title()

    elif choice == '4':
        search_by_authors()

    elif choice == '5':
        remove_contact()

    elif choice == '6':
        break
    
    else:
        print('Wrong choice!')