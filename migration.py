import json
import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate('secrets/firebase-adminsdk.json')
firebase_admin.initialize_app(cred)

# Read Cognito users from the exported JSON file
with open('cognito_users.json', 'r') as file:
    cognito_users = json.load(file)['Users']

# Prepare users for Firebase Auth
users = []
for cognito_user in cognito_users:
    email = next((attr['Value'] for attr in cognito_user['Attributes']
                 if attr['Name'] == 'email'), None)
    email_verified = next((attr['Value'] for attr in cognito_user['Attributes']
                          if attr['Name'] == 'email_verified'), "false") == 'true'
    # Only add user if email exists
    user_record = auth.ImportUserRecord(
        uid=cognito_user['Username'],
        email=email if email else None,
        email_verified=email_verified
    )
    users.append(user_record)

# Import users to Firebase Auth in batches
try:
    if users:
        # Splitting the users list into chunks of 1000 for batch processing
        chunks = [users[i:i + 1000] for i in range(0, len(users), 1000)]
        for chunk in chunks:
            result = auth.import_users(chunk)
            print(
                f'Successfully imported {result.success_count} users. Failed to import {result.failure_count} users.')
    else:
        print("No users to import.")
except firebase_admin.exceptions.FirebaseError as error:
    print('Error importing users:', error)
