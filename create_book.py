import os


def stapling_pages(book_name):
    chapters = []
    for cp in range(1, len(os.listdir('data')) + 1):
        with open(f'data/{cp}.txt', 'r') as file:
            chapter = file.read()

        chapters.append(chapter)

    book = '\n\n\n'.join(chapters)
    with open(f'books/{book_name}.txt', 'w') as file:
        file.write(book)
