import requests

token = '7e45fabc7e45fabc7e45fabca47e2aed5277e457e45fabc2059516aed33d0bbd348d15b'
version = 5.103
f_user = 151861157
data = []
opened_users = []
op_accs = []


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

# проверяет
def opened_accs_arr(data):
    opened_accs = []
    for post in data:
        try:
            if post['can_access_closed']:
                opened_accs.append(post['id'])
        except:
            pass
    return opened_accs


# проверка на наличие в массиве
def check_if_in_arr(x, arr=[]):
    result = False
    for a in arr:
        if x == a:
            result = True
    return result


# Start
opened_users.append(f_user)

for ids in opened_users:
    data = all_friends_info(ids)
    if (not check_if_in_arr(data[], opened_users)):
        opened_users.append(data[0]['id'])
#    op_accs = opened_accs_arr(data)
print(1)
    # data нужно сохранить
