import json

books_in_library = [
    
]

lended_books = [

]

def backup_books():
    
    # Writing books to a JSON file
    with open('books_in_library.json', 'w') as json_file:
        json.dump(books_in_library, json_file, indent=4)
    
    print('Books data are backuped!')

def backup_lent_books():

    # Writing books lend data to a JSON file
    with open('books_lend.json', 'w') as json_file:
        json.dump(lended_books, json_file, indent=4)

    print('Lended books data are backuped!')


def restore_books():

    # Data restoring for books

    try:
        books_in_library.clear()

        with open('books_in_library.json', 'r') as json_file:
            books = json.load(json_file)
            for data in books:
                books_in_library.append(data)

        print('Books restored successfully!')

    except:
        print('File refreshed!')


def restore_lent_books():

    # Data restoring for lent books

    try:
        lended_books.clear()

        with open('books_lend.json', 'r') as json_file:
            books = json.load(json_file)
            for data in books:
                lended_books.append(data)

        print('Lent books restored successfully!')
        
    except:
        print('File refreshed!')
