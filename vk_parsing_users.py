import requests

token = '7e45fabc7e45fabc7e45fabca47e2aed5277e457e45fabc2059516aed33d0bbd348d15b'
version = 5.103
f_user=1028790

def get_user_info(user_id):
    response = requests.get('https://api.vk.com/method/users.get',
                            params={
                                'access_token': token,
                                'v': version,
                                'user_ids': user_id,
                                'fields': 'photo_id, verified, sex, bdate, city, country, home_town, has_photo, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, domain, has_mobile, contacts, site, education, universities, schools, status, last_seen, followers_count, occupation, nickname, relatives, relation, personal, connections, exports, activities, interests, music, movies, tv, books, games, about, quotes, can_post, can_see_all_posts, can_see_audio, can_write_private_message, can_send_friend_request, is_favorite, is_hidden_from_feed, timezone, screen_name, maiden_name, crop_photo, is_friend, friend_status, career, military, blacklisted, blacklisted_by_me, can_be_invited_group',
                                'name_case': 'Nom'
                            }
                            )
    return response.json()

#data = get_user_info(f_user)

response_friends = requests.get('https://api.vk.com/method/friends.get',
                            params={
                                'access_token': token,
                                'v': version,
                                'user_id': 1,
                                'order':'name',
                            }
                            )
data_friends=response_friends.json()

print(1)

# https://vk.com/dev/users.get?
# params[user_ids]=1028790
# &params[fields]=photo_50%2Ccity%2Cverified
# &params[name_case]=Nom
# &params[v]=5.103
