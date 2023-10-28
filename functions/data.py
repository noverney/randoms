import json
from datetime import date
import random
from faker import Faker

from firebase_admin import firestore
from firebase_admin import auth

class User:
  def __init__(self, id: str, doc: dict):
    self.id = id
    self.name = doc["name"]
    self.preferences = doc["preferences"]
    self.days = doc["days"]
    self.original = doc
    self.original["id"] = id
  
  def __str__(self):
    return json.dumps(self.original)

class Match:
  def __init__(self, user1: User, user2: User, date: date = date.today()):
    self.user1 = user1
    self.user2 = user2
    self.date = date

def get_workdays():
  random_array = [random.choice([False, True]) for _ in range(5)]
  return [days for nr, days in enumerate(['Mon', 'Tue', 'Wed','Thu','Fri']) if random_array[nr]]

def get_preferences():
  preference_topics = ['Lord of the Rings', 'Hackatons', 'Console Gaming', 'PC Gaming', 'Humans', 'Bouldering', 'Boxing', 'Football']
  score = [0,0,0,0,0,0,0,0,0,0,1,2,3,4,5]
  return {preference:random.choice(score) for preference in preference_topics}

def create_fake_users(amount):
  fake = Faker(locale = "en_GB")
  return [User(i, {'name':fake.name(),'days':get_workdays(),'preferences':get_preferences()}) for i in range(amount)]

def add_fake_firestore_users(amount):
  fake_users = create_fake_users(amount)
  db = firestore.client()
  for user in fake_users:
    new_user = auth.create_user(email=f"alex_rovner+{user.name.lower().replace('-', '_').replace(' ', '_')}@hotmail.de", password="123456")
    db.collection("users").document(new_user.uid).set({
      "name": user.name,
      "preferences": user.preferences,
      "days": user.days,
      "fun-facts": ["I like to eat", "I like to sleep", "I like to code"]
    })
    print(f"Created user {user.name} with id {new_user.uid}")
