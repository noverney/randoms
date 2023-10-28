from matching import Player

import time
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import collections

def get_sorted_list_func(users, user_preferences):
    def get_sorted_list(user_id):
        user_score_list = {users[partner_id]:score for partner_id, score in enumerate(user_preferences[user_id]) if partner_id != user_id}
        user_score_ordered = collections.OrderedDict(sorted(user_score_list.items(), key=lambda item: item[1], reverse=True))
        return list(user_score_ordered)
    return get_sorted_list

def check_input(users, preference_matrix):
    user_limit = 10000
    if len(users)>user_limit or len(preference_matrix)>user_limit:
        raise ValueError(f"The user limit is {user_limit}")
    if len(users) != len(preference_matrix):
        raise ValueError(f"user list and matrix length do not match")
    if len(users) != len(set(users)):
        raise ValueError(f"Duplicates exist in the users array")


def get_preference_lists(users, preference_matrix):
    check_input(users, preference_matrix)

    user_preferences = cosine_similarity(preference_matrix)
    get_sorted_list = get_sorted_list_func(users, user_preferences)
    return [get_sorted_list(user_id) for user_id in range(len(users))]











