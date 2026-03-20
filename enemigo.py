import random
from colorama import Fore, Style

# Enemy stats
enemy_hp = 120
max_enemy_hp = 120
enemy_name = ""
scenario = ""


def set_enemy():
    # Set enemy and scenario based on player choice
    global enemy_name, scenario

    print("""
These are your path options, Hero:

    1. Shadow Dungeon: A cold, stone prison.
    2. Eternal Forest: Where the Werewolves howl.
    3. Old Graveyard: Resting place of the restless.
    4. Vampire Castle: The path to horror.
""")

    chosen = False

    while not chosen:
        try:
            story = int(input("Choose your enemy (1-4): ").strip())

            if story == 1:
                enemy_name = "Dragon 🐉"
                scenario = "Shadow Dungeon"
                chosen = True
            elif story == 2:
                enemy_name = "Werewolf 🐺🌕"
                scenario = "Eternal Forest"
                chosen = True
            elif story == 3:
                enemy_name = "Zombie 🧟"
                scenario = "Old Graveyard"
                chosen = True
            elif story == 4:
                enemy_name = "Vampire 🧛"
                scenario = "Vampire Castle"
                chosen = True
            else:
                print("  ⚠️  Choose a valid option (1-4).\n")

        except ValueError:
            print("  ⚠️  Please enter a number (1-4).\n")

    print(f"\n  Enemy: {enemy_name} | Scenario: {scenario}\n")


def show_enemy_status():
    # Build and return the enemy HP bar
    global enemy_hp, max_enemy_hp, enemy_name

    width = 12
    filled = max(0, (enemy_hp * width) // max_enemy_hp)
    empty = width - filled
    bar = "[" + "█" * filled + "░" * empty + "]"

    if empty >= 9:
        bar = Fore.RED + bar + Style.RESET_ALL
    elif empty >= 5:
        bar = (Fore.YELLOW + bar + Style.RESET_ALL)
    else:
        bar = (Fore.GREEN + bar + Style.RESET_ALL)
    
    return f"{enemy_name}  {bar} {enemy_hp} / {max_enemy_hp} HP"


def heal_enemy():
    # Enemy AI: 50% chance to heal if HP drops to 20% or below
    global enemy_hp, max_enemy_hp, enemy_name

    if enemy_hp <= max_enemy_hp * 0.2:
        heal = random.choice([True, False])
        if heal:
            enemy_hp = min(enemy_hp + 20, max_enemy_hp)
            print(f"  💉 {enemy_name} decided to heal! +20 HP")

    return enemy_hp


def critical_hit():
    # 10% chance to deal double damage
    base_damage = random.randint(14, 25)

    if random.random() < 0.1:
        base_damage = base_damage * 2
        print("  ⚡ Critical hit! Double damage!")

    return base_damage