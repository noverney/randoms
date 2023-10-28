from data import User, Match
from firebase_admin import auth

def notify_user_about_match(match: Match):
  send_email_to_user(match.user1, match.user2)
  send_email_to_user(match.user2, match.user1)

def send_email_to_user(user: User, matchedWith: User):
  other_user_email = "<unknown email>"
  try:
    other_user_data = auth.get_user(matchedWith.id)
    other_user_email = other_user_data.email
  except:
    pass
  print(f"Hi {user.name}! You have been matched with {matchedWith.name}! Reach out to them via {other_user_email} and have fun!")
