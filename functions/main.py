# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn
from firebase_admin import initialize_app
from firebase_admin import firestore
from datetime import date
from data import User, Match
from notification import notify_user_about_match, POSTMARK_API_KEY
from matching_users import create_matches_from_users
from data import add_fake_firestore_users
import os

default_app = initialize_app()

def get_all_users():
  db = firestore.client()
  docs = (
    db.collection("users")
    .stream())
  return [ User(doc.id, doc.to_dict()) for doc in docs ]

def match_users(users: list[User]):
  # this is the entrypoint for your matching code
  return [Match(pair[0], pair[1]) for pair in create_matches_from_users(users)]


@https_fn.on_request(secrets=[POSTMARK_API_KEY])
def trigger_matching(req: https_fn.Request) -> https_fn.Response:
  matches = match_users(get_all_users())
  resp = ""

  # Write to Firestore
  db = firestore.client()
  
  seen = set()
  print("Putting match into firestore and notifying users")
  for match in matches:
    notify_user_about_match(match)

    if match.user1.id not in seen and match.user2.id not in seen:
      seen.add(match.user1.id)
      seen.add(match.user2.id)

      key = ".".join(sorted([match.user1.id, match.user2.id])) + "." + match.date.isoformat()

      match.user1.load_name_from_firestore()
      match.user2.load_name_from_firestore()
      match_data = {
        "participants": [
          {
            "id": match.user1.id,
            "name": match.user1.name,
            "email": match.user1.email,
            "avatarUrl": match.user1.avatarUrl or f"https://source.boringavatars.com/beam/120/{match.user1.id}?colors=264653,2a9d8f,e9c46a,f4a261,e76f51"
          },
          {
            "id": match.user2.id,
            "name": match.user2.name,
            "email": match.user2.email,
            "avatarUrl": match.user1.avatarUrl or f"https://source.boringavatars.com/beam/120/{match.user2.id}?colors=264653,2a9d8f,e9c46a,f4a261,e76f51"
          }
        ],
        "date": match.date.isoformat()
      }
      db.collection(f"users/{match.user1.id}/matches").document(key).set(match_data, merge=True)
      db.collection(f"users/{match.user2.id}/matches").document(key).set(match_data, merge=True)

      resp += f"{match.user1.name} + {match.user2.name}\n"

  return https_fn.Response(resp)

@https_fn.on_request()
def add_fake_users(req: https_fn.Request) -> https_fn.Response:
  if os.environ["PROFILE"] != "dev":
    return https_fn.Response("Not allowed")
  print("Adding fake users")
  add_fake_firestore_users(4)
  return https_fn.Response("Added 10 fake users")
