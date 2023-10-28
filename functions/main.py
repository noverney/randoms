# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn
from firebase_admin import initialize_app
from firebase_admin import firestore
from datetime import date
from data import User, Match
from notification import notify_user_about_match, POSTMARK_API_KEY
from postmarker.core import PostmarkClient

default_app = initialize_app()

def get_all_users():
  db = firestore.client()
  docs = (
    db.collection("users")
    .stream())
  return [ User(doc.id, doc.to_dict()) for doc in docs ]

def match_users(users: list[User]):
  # this is the entrypoint for your matching code
  return [Match(pair[0], pair[1]) for pair in zip(users[0::2], users[1::2])]

@https_fn.on_request(secrets=[POSTMARK_API_KEY])
def trigger_matching(req: https_fn.Request) -> https_fn.Response:
  matches = match_users(get_all_users())
  resp = ""
  for match in matches:
    resp += f"{match.user1.name} + {match.user2.name}\n"
    notify_user_about_match(match)

  return https_fn.Response(resp)
