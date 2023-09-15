import requests
import json
import time


def get_chapter_content(book_id, chapter_id):
    headers = {
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'Content-Type': 'application/json',
        'webnovel-content-language': 'en',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Linux"',
    }

    params = {
        'bookId': f'{book_id}',
        'chapterId': f'{chapter_id}',
        'isBot': 'false',
        '_fsae': '0',
        'encryptType': '3',
    }

    response = requests.get('https://m.webnovel.com/go/pcm/chapter/getContent', params=params, headers=headers)
    data = response.json()

    max_chapter_number = data['data']['bookInfo']['totalChapterNum']

    while True:
        chapter_data = data['data']['chapterInfo']['chapterName'] + '\n\n'
        for p in data['data']['chapterInfo']['contents']:
            chapter_data += p['content']

        with open(f"data/{data['data']['chapterInfo']['chapterIndex']}.txt", 'w') as file:
            file.write(chapter_data)

        if data['data']['chapterInfo']['chapterIndex'] == max_chapter_number:
            print(f"[!] Lust chapter: {data['data']['chapterInfo']['chapterIndex']}")
            break

        params['chapterId'] = data['data']['chapterInfo']['nextChapterId']
        response = requests.get('https://m.webnovel.com/go/pcm/chapter/getContent', params=params, headers=headers)
        data = response.json()
        print(f"[+] Chapter: {data['data']['chapterInfo']['chapterIndex'] - 1}")
        time.sleep(3)
