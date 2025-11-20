from InquirerPy import prompt
from choose_folder import choose_folders

def main_menu():
    questions = [
        {
            "type": "list",
            "name": "action",
            "message": "Choose an action:",
            "choices": ["Clean temp files", "Check disk usage", "Exit"]
        }
    ]

    answer = prompt(questions)
    action = answer["action"]  # Extract string from dictionary

    if action == "Check disk usage":
        choose_folders()  # Call your subfolder selection
    elif action == "Clean temp files":
        print("Cleaning temp files...")
    elif action == "Exit":
        print("Goodbye!")

if __name__ == '__main__':
    main_menu()
