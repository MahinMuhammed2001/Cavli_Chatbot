import os
from google.cloud import dialogflow_v2 as dialogflow

# Check if the environment variable is set
credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
if credentials_path:
    print(f"Authentication successful! Using credentials: {credentials_path}")
else:
    print("Error: GOOGLE_APPLICATION_CREDENTIALS environment variable not set.")
