import uuid  # Importing the uuid module for generating session IDs
from google.cloud import dialogflow

def detect_intent_texts(project_id, session_id, texts, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    for text in texts:
        text_input = dialogflow.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.QueryInput(text=text_input)
        response = session_client.detect_intent(request={"session": session, "query_input": query_input})

        print("Query text:", response.query_result.query_text)
        print("Detected intent:", response.query_result.intent.display_name)
        print("Response:", response.query_result.fulfillment_text)

def main():
    #  Dialogflow project ID
    project_id = 'unified-surfer-442117-u8'  


    session_id = str(uuid.uuid4())  # This will generate a new session ID for each conversation

    language_code = 'en'  # Language code for the interaction (English here)

    print("Welcome to the chatbot! Type 'exit' to quit.")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        # Call the Dialogflow detect_intent_texts function
        detect_intent_texts(project_id, session_id, [user_input], language_code)

if __name__ == "__main__":
    main()
