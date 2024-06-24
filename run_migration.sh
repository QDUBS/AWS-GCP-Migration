#!/bin/bash

# Define variables
USER_POOL_ID="us-east-2_7wGZgrBwC"
COGNITO_USERS_FILE="cognito_users.json"
MIGRATION_SCRIPT="migration.py"

echo "Listing all Cognito users about to be migrated:"
aws cognito-idp list-users --user-pool-id $USER_POOL_ID

echo "Exporting users to JSON file:"
aws cognito-idp list-users --user-pool-id $USER_POOL_ID > $COGNITO_USERS_FILE

echo "Running migration script:"
python $MIGRATION_SCRIPT
