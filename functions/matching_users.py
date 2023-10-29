from matching import Player
from matching.algorithms import stable_roommates

import time
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import collections
from functions.data import User

def get_sorted_list_func(user_ids, user_preferences):
    def get_sorted_list(user_index):
        user_score_list = {user_ids[partner_id]:score for partner_id, score in enumerate(user_preferences[user_index]) if partner_id != user_index}
        user_score_ordered = collections.OrderedDict(sorted(user_score_list.items(), key=lambda item: item[1], reverse=True))
        return list(user_score_ordered)
    return get_sorted_list

def check_input(user_ids, preference_matrix):
    user_limit = 10000
    if len(user_ids)>user_limit or len(preference_matrix)>user_limit:
        raise ValueError(f"The user limit is {user_limit}")
    if len(user_ids) != len(preference_matrix):
        raise ValueError(f"user list and matrix length do not match")

def get_preference_lists(user_ids, preference_matrix):
    check_input(user_ids, preference_matrix)

    user_preferences = cosine_similarity(preference_matrix)
    get_sorted_list = get_sorted_list_func(user_ids, user_preferences)
    return [get_sorted_list(user_index) for user_index in range(len(user_ids))]

def convert_preferences_to_matrix(users_preferences):
    # Get the list of all topics from the user preferences
    all_topics = set().union(*users_preferences)

    # Create a NumPy matrix from the user preferences
    pref_matrix = np.array([[user_pref.get(topic, 0) for topic in all_topics] for user_pref in users_preferences])

    return pref_matrix

def remove_previous_matches(preference_order, previous_matches):

    for match in previous_matches:
        preference_order[match[0]].pop(preference_order[match[0]].index(match[1]))
        preference_order[match[1]].pop(preference_order[match[1]].index(match[0]))

    return preference_order

def create_matches_from_users(users: list[User]):
    # now we need to build the matrix 
    names_to_player = {x.id: Player(x.id) for x in users}
    id_to_user = {x.id: x for x in users}
    # going to be unique for each user
    names = [x.id for x in users]
    pref_matrix = convert_preferences_to_matrix([x.preferences for x in users])



    #print(pref_matrix)
    preference_order = get_preference_lists(names, pref_matrix)
    #print(preference_order)

    # Uncomment line below if we want to remove previous matches, just need list of touples of previous matches
    # like [(1,2),(3,4)]
    # preference_order = remove_previous_matches(preference_order, previous_matches)

    for name,pref in zip(names,preference_order):
        player = names_to_player[name]
        player.set_prefs([names_to_player[x] for x in pref])

    players = [value for key,value in names_to_player.items()]

    matching = stable_roommates(players)
    user_tuples = []
    losers = []

    for match1, match2 in matching.items():
        #print(match1.name)
        if match2:
            user_tuples.append((id_to_user[match1.name], id_to_user[match2.name]))
        else:
            losers.append(id_to_user[match1.name])

    if len(losers) >= 2:
        user_tuples.extend(zip(losers[0::2], losers[1::2]))
    
    return user_tuples


