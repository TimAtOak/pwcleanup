from InquirerPy import prompt
from log_folders import log_folders_and_files
import os

def choose_folders():
    home = os.path.expanduser("~")  # dynamic home path
    paths = {
        "Downloads": os.path.join(home, "Downloads"),
        # "Desktop": os.path.join(home, "Desktop"),
        "AppData": os.path.join(home, "AppData")
    }

    sub_questions = [
        {
            "type": "list",
            "name": "subAction",
            "message": "Choose an action:",
            "choices": ["Downloads", "AppData", "Back", "Exit"]
        }
    ]

    sub_answer = prompt(sub_questions)
    sub_action = sub_answer["subAction"]

    if sub_action in paths:
        log_folders_and_files(paths[sub_action])
    elif sub_action == "Back":
        from main import main_menu
        main_menu()
    elif sub_action == "Exit":
        print("Goodbye!")