@echo off
set USER_POOL_ID=us-east-2_7wGZgrBwC
set COGNITO_USERS_FILE=cognito_users.json
set MIGRATION_SCRIPT=migration.py
set LIST_USERS_SCRIPT=retrieve_firebase_users.py

echo Listing all Cognito users about to be migrated:
aws cognito-idp list-users --user-pool-id %USER_POOL_ID%

echo Exporting users to JSON file:
aws cognito-idp list-users --user-pool-id %USER_POOL_ID% > %COGNITO_USERS_FILE%

echo Running migration script:
python %MIGRATION_SCRIPT%

echo Retrieving migrated users from Firebase:
python %LIST_USERS_SCRIPT%

pause
