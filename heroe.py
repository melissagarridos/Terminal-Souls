import random
import enemigo
from colorama import Fore, Style

# ============================================================
# Hero stats
# ============================================================

hero_hp = 100
max_hero_hp = 100
potions = 3
hero_name = "Hero ⚔️"


def show_logo():
    # Print the game title
    logo = ("""

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

    """)
    print(Fore.CYAN + logo + Style.RESET_ALL)


# Show logo and pick enemy once at startup
show_logo()
enemigo.set_enemy()


def show_hero_status():
    # Build and return the hero HP bar
    global hero_hp
    width = 12
    filled = max(0, (hero_hp * width) // max_hero_hp)
    empty = width - filled
    bar = "[" + "█" * filled + "░" * empty + "]"

    if empty >= 9:
        bar = Fore.RED + bar + Style.RESET_ALL
    elif empty >= 5:
        bar = (Fore.YELLOW + bar + Style.RESET_ALL)
    else:
        bar = (Fore.GREEN + bar + Style.RESET_ALL)

    return f"🦸 {hero_name}: {bar} {hero_hp} / {max_hero_hp} HP"
 
    



def show_status():
    # Print both HP bars
    print("\n" + "═" * 40)
    print(show_hero_status())
    print(enemigo.show_enemy_status())
    print("═" * 40 + "\n")


def hero_critical(base_damage):
    # 10% chance to deal double damage
    if random.random() < 0.1:
        base_damage = base_damage * 2
        print("  ⚡ Critical hit! Double damage! 😱")
    return base_damage


def check_winner():
    # Check if either fighter has 0 HP
    end = False
    if hero_hp <= 0:
        print("\n💀 The hero has fallen! The enemy wins...\n")
        end = True
    if enemigo.enemy_hp <= 0:
        print(f"\n🏆 Victory! You defeated {enemigo.enemy_name}!\n")
        end = True
    return end


def player_turn():
    # Handle player action for this turn
    global hero_hp, potions

    valid_action = False

    while not valid_action:
        print(f"  🧪 Potions left: {potions}")
        print("\n  ⚔️  What will you do?\n")
        print("  1. 🗡️  Attack             (damage: 10-25)")
        print("  2. 💊  Heal               (recover 20 HP)")
        print("  3. 🌟  Special ability    (damage: 30-50, 50% chance to fail)\n")

        choice = input("  Your choice (1-3): ").strip()

        if choice == "1":
            damage = hero_critical(random.randint(10, 25))
            enemigo.enemy_hp = max(0, enemigo.enemy_hp - damage)
            print(f"\n  🗡️  {hero_name}  attacks for {damage} damage!")
            valid_action = True

        elif choice == "2":
            if potions <= 0:
                print("\n  ❌ No potions left! Choose another action.\n")

            elif hero_hp >= max_hero_hp:
                print("\n  ❌ HP is already full! Choose another action.\n")

            else:
                hero_hp = min(hero_hp + 20, max_hero_hp)
                potions -= 1
                print(f"\n  💊 You healed! +20 HP. Potions left: {potions} 🧪")
                valid_action = True

        elif choice == "3":
            if random.random() < 0.5:
                damage = hero_critical(random.randint(30, 50))
                enemigo.enemy_hp = max(0, enemigo.enemy_hp - damage)
                print(f"\n  🌟 Special ability! You deal {damage} damage! 💥")
            else:
                print("\n  😬 Special ability failed! Nothing happened.")
            valid_action = True

        else:
            print("\n  ⚠️  Invalid option. Choose 1, 2 or 3.\n")


def enemy_turn():
    # Enemy AI: try to heal, then attack
    global hero_hp

    enemigo.heal_enemy()

    damage = enemigo.critical_hit()
    hero_hp = max(0, hero_hp - damage)
    print(f"  🔥 {enemigo.enemy_name}  attacks for {damage} damage! 💢")


def play():
    # Main game loop
    turn = 1
    playing = True
    print("\n⚔️  Let the battle begin! 🥊\n")

    while playing:
        print(f"\n🎮 ══════ Turn {turn} ══════ 🎮")
        show_status()

        player_turn()
        if check_winner():
            playing = False

        if playing:
            enemy_turn()
            if check_winner():
                playing = False

        if playing:
            turn += 1


# Start the game
play()