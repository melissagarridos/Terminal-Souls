# Melissa Garrido - Inicio
# 19/03/2026
# Inicio: first values and game stats
import random
from colorama import Fore, Style


# Logo
logo:str = r"""


         ████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗     
            ██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║     
            ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║     
            ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║     
            ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗
            ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝

            ███████╗ ██████╗ ██╗   ██╗██╗     ███████╗
            ██╔════╝██╔═══██╗██║   ██║██║     ██╔════╝
            ███████╗██║   ██║██║   ██║██║     ███████╗
            ╚════██║██║   ██║██║   ██║██║     ╚════██║
            ███████║╚██████╔╝╚██████╔╝███████╗███████║
            ╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝

"""

# Show logo
print(logo)

def get_player_name() -> str:
    """
    Prompt the user to enter a valid name.

    Validation rules:
    - Must not be empty or only spaces
    - Minimum length: 3 characters
    - Maximum length: 13 characters

    Returns:
        name (str): A validated name in lowercase.
    """

    valid:bool = False
    name = ""

    while not valid:
        name: str = input("Please enter your name: ").strip().lower()

        if not name:
            print("Name cannot be empty.")
        elif len(name) < 3:
            print("Name must be at least 3 characters.")
        elif len(name) > 13:
            print("Name must be at most 13 characters.")
        else:
            valid = True

    return name

print(f"Welcome {get_player_name()}!")


# def historia():

