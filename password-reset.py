import json
import firebase_admin
from firebase_admin import credentials, auth

for user in users:
    try:
        auth.generate_password_reset_link(user.email)
        print(f'Password reset email sent to {user.email}')
    except firebase_admin.exceptions.FirebaseError as error:
        print(f'Error sending password reset email to {user.email}:', error)
