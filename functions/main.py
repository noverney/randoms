# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn
from firebase_admin import initialize_app
from firebase_admin import firestore

default_app = initialize_app()

class User:
  def __init__(self, id: str, doc: dict):
    self.id = id
    self.name = doc["name"]
    self.preferences = doc["preferences"]
  
  def __str__(self):
    return f"User({self.id}, {self.name}, {self.preferences})"

def get_all_users():
  db = firestore.client()
  docs = (
    db.collection("users")
    .stream())
  return [ User(doc.id, doc.to_dict()) for doc in docs ]

def match_users(users: list[User]):
  # this is the entrypoint for your matching code
  return zip(users[0::2], users[1::2])

@https_fn.on_request()
def trigger_matching(req: https_fn.Request) -> https_fn.Response:
  return https_fn.Response(",".join([f"{str(x[0])}+{str(x[1])}" for x in match_users(get_all_users())]))