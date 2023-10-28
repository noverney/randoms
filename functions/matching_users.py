from matching import Player

import time
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import collections

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



def match_users(users):


    matches = [("You", "A Penguin")]
    return matches










