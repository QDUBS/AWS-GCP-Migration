import firebase_admin
from firebase_admin import credentials, auth

# Initialize the Firebase app
cred = credentials.Certificate('secrets/firebase-adminsdk.json')
firebase_admin.initialize_app(cred)

# List users
def list_firebase_users():
    page = auth.list_users()
    while page:
        for user in page.users:
            print('User ID: {}, Email: {}, Email Verified: {}'.format(
                user.uid, user.email, user.email_verified))
        # Get next batch of users
        page = page.get_next_page()


list_firebase_users()
