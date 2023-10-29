from data import User, Match
from firebase_admin import auth
from firebase_functions.params import SecretParam
from postmarker.core import PostmarkClient

POSTMARK_API_KEY = SecretParam('POSTMARK_API_KEY')

def notify_user_about_match(match: Match):
  send_email_to_user(match.user1, match.user2) # the algorithm generates the matches in both directions, so we only need to send one email

def send_email_to_user(user: User, matchedWith: User):
  user_email = "alex_rovner@hotmail.de" # fallback email
  user.load_name_from_firestore()
  matchedWith.load_name_from_firestore()
  try:
    user_data = auth.get_user(user.id)
    user_email = user_data.email
  except:
    pass
  body = f"Hi {user.name}! You have been matched with {matchedWith.name}! Reach out to them via {user_email} and have fun!"
  if POSTMARK_API_KEY.value == "dummy":
    print(f"Would send email to {user_email} with body:\n{body}")
  else:
    postmark = PostmarkClient(server_token=POSTMARK_API_KEY.value)
    postmark.emails.send_with_template(
      From='noreply@meetingmunch.com',
      To=user_email,
      TemplateId="33637852",
      TemplateModel={
        "name": user.name,
        "action_url": "https://baselhack2023-randoms.web.app/",
        "matched_with": matchedWith.name,
        "help_url": "https://baselhack2023-randoms.web.app/",
        "product_name": "MeetingMunch"
      }
    )
