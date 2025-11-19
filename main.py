import os
from InquirerPy import prompt
from log_folders import log_folders


def choose_folder():
    sub_questions = [
        {
            "type": "list",
            "name": "subAction",
            "message": "Choose an action:",
            "choices": ["Downloads", "Desktop", "Appdata","Exit"]
        }
    ]

    sub_answer = prompt(sub_questions)

    sub_action = sub_answer["subAction"]  # Extract string

    if sub_action == "Downloads":
        log_folders('C:\\Users\\ineic\\Downloads')
    elif sub_action == "Desktop":
        log_folders('C:\\Users\\ineic\\Desktop')
    elif sub_action == "Appdata":
        log_folders('C:\\Users\\ineic\\AppData')
    elif sub_action == "Exit":
        print("Goodbye!")


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
        choose_folder()  # Call your subfolder selection
    elif action == "Clean temp files":
        print("Cleaning temp files...")
    elif action == "Exit":
        print("Goodbye!")

if __name__ == '__main__':
    main_menu()
