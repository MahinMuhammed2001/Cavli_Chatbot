import uuid
from rich.console import Console
from rich.text import Text
from database import load_data
from nlp import extract_keywords
from utils import filter_companies_by_field, format_company_info
from dialogflow_interaction import detect_intent_texts  # Import your Dialogflow interaction function

# Path to the data file
DATA_FILE = "../data/companies.json"
# Initialize the console for styled output
console = Console()
# Helper function to print chatbot messages with styling
def print_chatbot_message(message, style="bold green"):
    console.print(Text(message, style=style))
# Generate a unique session ID for each user
def generate_session_id():
    return str(uuid.uuid4())

# Main chatbot function
def main():
    # Your Dialogflow project setup
    project_id = 'intelligent-chatbot-ccah'  # my project id from google cloud console
    language_code = 'en'

    
    print_chatbot_message("Welcome to the Intelligent Chatbot! Type 'exit' to quit.", style="bold cyan") # Welcome message
    
    # Generate a new session ID for this interaction
    session_id = generate_session_id()
    try:
        data = load_data(DATA_FILE)
        print_chatbot_message("Chatbot: Data loaded successfully!", style="bold green")
    except FileNotFoundError:
        print_chatbot_message("Error: Data file not found. Please check the path.", style="bold red")
        return
    except ValueError:
        print_chatbot_message("Error: Invalid JSON in the data file.", style="bold red")
        return

 
    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print_chatbot_message("Chatbot: Goodbye!", style="bold red")
            break

        print_chatbot_message(f"You asked: {user_input}", style="italic white")

      
        detect_intent_texts(project_id, session_id, [user_input], language_code)   # Call Dialogflow to get the response based on user input

        # Extract keywords from user input for further processing (if needed)
        keywords = extract_keywords(user_input)
        print_chatbot_message(f"Chatbot: Processing your query with keywords: {keywords}", style="yellow")

        # Handle different queries based on extracted keywords
        if "semiconductors" in keywords:
            results = filter_companies_by_field(data, "industry_category", "semiconductor")
            if results:
                print_chatbot_message(f"Chatbot: Found {len(results)} companies in the 'Semiconductors' industry.", style="bold blue")
                print_chatbot_message(format_company_info(results), style="dim white")
            else:
                print_chatbot_message("Chatbot: No companies found in the 'Semiconductors' industry.", style="bold yellow")

        elif "microcontrollers" in keywords:
            results = filter_companies_by_field(data, "products_services", "microcontrollers")
            if results:
                print_chatbot_message(f"Chatbot: Found {len(results)} companies manufacturing 'Microcontrollers'.", style="bold green")
                print_chatbot_message(format_company_info(results), style="dim white")
            else:
                print_chatbot_message("Chatbot: No companies found manufacturing 'Microcontrollers'.", style="bold yellow")

        elif "germany" in keywords:
            results = filter_companies_by_field(data, "address", "germany")
            if results:
                print_chatbot_message(f"Chatbot: Found {len(results)} companies in Germany.", style="bold magenta")
                print_chatbot_message(format_company_info(results), style="dim white")
            else:
                print_chatbot_message("Chatbot: No companies found in Germany.", style="bold yellow")

        else:
            # Handle unrecognized queries
            print_chatbot_message("Chatbot: I didn't understand your query. Could you rephrase?", style="bold yellow")

# Entry point for the script
if __name__ == "__main__":
    main()



