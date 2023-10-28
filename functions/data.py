import json
from datetime import date

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
  def __init__(self, user1: User, user2: User, date: date):
    self.user1 = user1
    self.user2 = user2
    self.date = date
