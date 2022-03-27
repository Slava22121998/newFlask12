import json
import logging
import os

logging.basicConfig(filename='error.log')


def find_post(word_request=''):
    posts_list = list()
    try:
        with open('posts.json', encoding='windows-1251') as f:
            file = json.load(f)
            for item in file:
                if word_request in item['content']:
                    posts_list.append(item)
            return posts_list
    except FileNotFoundError:
        logging.exception('JSONFile not found')
        posts_list.append({"pic": " ", "content": 'JSONFile not found'})
        return posts_list
    except json.JSONDecodeError:
        logging.exception('JSON decoding is not allowed')
        posts_list.append({"pic": " ", "content": 'JSON decoding is not allowed'})
        return posts_list


def add_post(filename, text):
    try:
        with open('posts.json', 'r+', encoding='windows-1251') as f:
            file = json.load(f)
            json_item = {"pic": f'static/uploads/images/{filename}', "content": text}
            file.append(json_item)
            f.seek(0)
            json.dump(file, f, indent=2, ensure_ascii=False)
            return True
    except json.JSONDecodeError:
        logging.exception('JSONFIle is damaged')
        return False
    except FileNotFoundError:
        logging.exception('Post is created, but not added on the page')
        return False
