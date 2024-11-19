# Intelligent Chatbot

An intelligent chatbot that helps users find information about companies in various industries, such as Semiconductors, Microcontrollers, and more.

## Features

- Answer queries such as:
  - "How many companies are listed under the 'Semiconductors' industry?"
  - "List all companies that manufacture 'Microcontrollers'."
  - "Provide the contact details of companies located in 'Germany'."
- The chatbot handles follow-up questions and maintains context.
- It uses Dialogflow for NLP and spaCy for keyword extraction.

## Requirements

- Python 3.12
- Install the necessary Python libraries:
  - `pip install rich` 
  - `pip install spacy` 
  - `pip install google-cloud-dialogflow`

- Ensure that you have set up the Dialogflow API and your project credentials (see Dialogflow documentation for setup instructions).

- You will also need a `companies.json` file containing company data. 

## How to Run 
1. Install the required libraries and set up your Dialogflow API.
2. cd chatbot.py 
3. python src\chatbot.py


## Setting Up the Google Cloud Credentials
1. Download the service account key (`dialogflow-service.json`) from your Google Cloud Console.
2. Set the environment variable for authentication:

   For **Windows** (in Command Prompt):
   ```bash
   set GOOGLE_APPLICATION_CREDENTIALS="C:\path\to\your\dialogflow-service.json"

## Setting Up Dialogflow
1. Create a project in Google Cloud Console: https://console.cloud.google.com/
2. Enable the Dialogflow API: https://console.cloud.google.com/apis/library/dialogflow.googleapis.com
3. Create a service account and download the JSON key file.
4. Store the JSON file in a secure location and reference its path in the `GOOGLE_APPLICATION_CREDENTIALS` environment variable.
5. Install the Dialogflow library using pip: `pip install google-cloud-dialogflow`


## Sample Output
Welcome to the Intelligent Chatbot! Type 'exit' to quit.
Chatbot: Data loaded successfully!
You: How many companies are listed under the 'Semiconductors' industry?
Chatbot: Found 1 companies in the 'Semiconductors' industry.

Company Name: ACCRETECH (Europe) GmbH
Industry Category: Accretech develops advanced systems and machines for semiconductor manufacturing
Address: Landsberger Str. 396, 81241 München, Germany
Email: info@accretech.eu
Phone: 0049 89 250064-200
Website: http://www.accretech.eu/
LinkedIn: https://www.linkedin.com/company/accretech/
YouTube: https://www.youtube.com/channel/UCH3MeSdfXkCymTkT8bBDEzA


------------------------------
