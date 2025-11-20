from InquirerPy import prompt
from log_folders import log_folders_and_files


def choose_folders():
    sub_questions = [
        {
            "type": "list",
            "name": "subAction",
            "message": "Choose an action:",
            "choices": ["Downloads", "Desktop", "Appdata","Back","Exit"]
        }
    ]

    sub_answer = prompt(sub_questions)
    sub_action = sub_answer["subAction"]  # Extract string

    if sub_action == "Downloads":
        log_folders_and_files('C:\\Users\\ineic\\Downloads')
    elif sub_action == "Desktop":
        log_folders_and_files('C:\\Users\\ineic\\Desktop')
    elif sub_action == "Appdata":
        log_folders_and_files('C:\\Users\\ineic\\AppData')
    elif sub_action == "Exit":
        from main import main_menu
        main_menu()
    elif sub_action == "Exit":
        print("Goodbye!")