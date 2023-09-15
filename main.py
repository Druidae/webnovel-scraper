from get_book_data import get_chapter_content
from create_book import stapling_pages

import os


# bookId: 24567274306284105
# chapteerId: 65947289910310803


def create_book(
        book_id=input('Enter book id: '),
        chapter_id=input('Enter chapter id: '),
        book_name=input('Enter book name: ')
        ):

    if not os.path.isdir('data'):
        os.mkdir('data')
    if not os.path.isdir('books'):
        os.mkdir('books')

    for f in os.listdir('data'):
        os.remove(os.path.join('data', f))

    try:
        get_chapter_content(
            book_id=book_id,
            chapter_id=chapter_id
        )
        stapling_pages(book_name=book_name)
        print('[+] Successful')
    except Exception as ex:
        print(f'[!] Error: {ex}')


if __name__ == "__main__":
    create_book()
