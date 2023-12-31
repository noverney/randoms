import json
from datetime import date
import random
from faker import Faker

from firebase_admin import firestore
from firebase_admin import auth

def get_user_from_auth(uid: str):
  return auth.get_user(uid)

class User:
  def __init__(self, id: str, doc: dict):
    self.id = id
    self.name = "<no name>" if "name" not in doc else doc["name"]
    self.preferences = doc["preferences"]
    self.days = doc["days"]
    self.original = doc
    self.original["id"] = id
  
  def load_name_from_firestore(self):
    user = get_user_from_auth(self.id)
    self.name = user.display_name
    self.avatarUrl = user.photo_url
    self.email = user.email
  
  def __str__(self):
    return json.dumps(self.original)

class Match:
    def __init__(self, user1: User, user2: User, date: date = date.today()):
        self.user1 = user1
        self.user2 = user2
        self.date = date


def get_workdays():
    random_array = [random.choice([False, True]) for _ in range(5)]
    return [days for nr, days in enumerate(['Mon', 'Tue', 'Wed', 'Thu', 'Fri']) if random_array[nr]]


def get_preferences():
    preference_topics = ['Sports', 'Eating', 'Board Games', 'Video Games', 'Coffee Enthusiasm', 'Tea Appreciation',
                         'Nightlife and Parties', 'Nature and Greenery', 'Books', 'Anime and Manga']

    score = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]
    return {preference: random.choice(score) for preference in preference_topics}


def create_fake_users(amount):
    fake = Faker(locale="en_GB")
    return [User(i, {'name': fake.name(), 'days': get_workdays(), 'preferences': get_preferences()}) for i in
            range(amount)]


def get_funfact(preferences):
    max_key = max(preferences, key=preferences.get)
    return 'I really like {}!'.format(max_key)


def add_fake_firestore_users(amount):
  fake_users = create_fake_users(amount)
  db = firestore.client()
  for user in fake_users:
    new_user = auth.create_user(email=f"alex_rovner+{user.name.lower().replace('-', '_').replace(' ', '_')}@hotmail.de", display_name=user.name ,password="123456")
    db.collection("users").document(new_user.uid).set({
      "preferences": user.preferences,
      "days": user.days,
      "fun-facts": ["I like to eat", "I like to sleep", "I like to code"]
    })
    print(f"Created user {user.name} with id {new_user.uid}")
