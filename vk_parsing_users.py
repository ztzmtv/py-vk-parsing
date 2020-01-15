import requests

token = '7e45fabc7e45fabc7e45fabca47e2aed5277e457e45fabc2059516aed33d0bbd348d15b'
version = 5.103
f_user = 151861157
data = []
opened_users = []

def all_friends_info(user_id):
    friends = []
    response_friends = requests.get('https://api.vk.com/method/users.getFollowers',
                                    params={
                                        'access_token': token,
                                        'v': version,
                                        'user_id': user_id,
                                        'count': 1000,
                                        'fields': 'photo_id, verified, sex, bdate, city, country, home_town, has_photo, '
                                                  'photo_max_orig, online, lists, domain, has_mobile, contacts, site, education, '
                                                  'universities, schools, status, last_seen, followers_count, occupation, '
                                                  'nickname, relatives, relation, personal, connections, exports, wall_comments, '
                                                  'activities, interests, music, movies, tv, books, games, about, quotes, '
                                                  'can_post, can_see_all_posts, can_see_audio, can_write_private_message, '
                                                  'can_send_friend_request, is_favorite, is_hidden_from_feed, timezone, '
                                                  'screen_name, maiden_name, is_friend, friend_status, career, military, '
                                                  'blacklisted'
                                    }
                                    )

    data_friends = response_friends.json()['response']['items']
    friends.extend(data_friends)
    return friends

def opened_accs_arr(data):
    opened_accs = []
    for post in data:
        if post['is_closed']:
            opened_accs.append(post['id'])
    return opened_accs

# Start
opened_users.append(f_user)
for ids in opened_users:
    data1 = all_friends_info(ids)

data = all_friends_info(f_user)
#data нужно сохранить
op_accs = opened_accs_arr(data)

