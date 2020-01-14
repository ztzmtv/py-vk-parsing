import csv

import requests
import time

def take_1000_posts():
    token = '7e45fabc7e45fabc7e45fabca47e2aed5277e457e45fabc2059516aed33d0bbd348d15b'
    version = 5.103
    domain = 'mysterious_conditions'
    count = 100
    offset = 0
    all_posts = []

    while offset < 1000:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'domain': domain,
                                    'count': count,
                                    'offset': offset
                                }
                                )
        data = response.json()['response']['items']
        offset += 100
        all_posts.extend(data)
        time.sleep(0.5)
    return all_posts


def file_writer(data):
    with open('mysterious_conditions.csv', 'w', encoding="utf-8") as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('likes', 'body', 'url'))
        for post in data:
            try:                                            # тут только работа с фото
                if post['attachments'][0]['type']:          # если всё норм - это урл
                    img_url=post['attachments'][0]['photo']['sizes'][-1]['url']
                else:
                    img_url='pass'                          #нет - это пасс
            except:
                pass
            a_pen.writerow((post['likes']['count'], post['text'], img_url)) #запись строки и переход к след. в цикле

all_posts = take_1000_posts()
print(1)
file_writer(all_posts)

print(1)
