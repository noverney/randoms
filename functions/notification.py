from data import User, Match
from firebase_admin import auth
from firebase_functions.params import SecretParam
from postmarker.core import PostmarkClient

POSTMARK_API_KEY = SecretParam('POSTMARK_API_KEY')

def notify_user_about_match(match: Match):
  send_email_to_user(match.user1, match.user2) # the algorithm generates the matches in both directions, so we only need to send one email

def send_email_to_user(user: User, matchedWith: User):
  other_user_email = "alex_rovner@hotmail.de"
  try:
    other_user_data = auth.get_user(matchedWith.id)
    other_user_email = other_user_data.email
  except:
    pass
  body = f"Hi {user.name}! You have been matched with {matchedWith.name}! Reach out to them via {other_user_email} and have fun!"
  if POSTMARK_API_KEY.value == "dummy":
    print(f"Would send email to {other_user_email} with body:\n{body}")
  else:
    postmark = PostmarkClient(server_token=POSTMARK_API_KEY.value)
    postmark.emails.send(
      From='alex@rovner.ch',
      To=other_user_email,
      Subject='You have been matched!',
      HtmlBody=body
    )
