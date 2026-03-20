# Terminal-Souls

Terminal Souls README
Terminal Souls is a turn-based battle game with 4 enemy options and one hero. Both Angelica and Melissa developed the code using python with functions and internal python functions such as Random and Colorama.

What each file does

main.py: This is the main file. It shows the logo, runs the battle loop, handles the hero's actions, and decides who wins. Made by Angelica.

enemigo.py — this file handles everything about the enemy: picking which one you fight, showing its HP bar, making it heal itself, and calculating its attacks. Made by Melissa.

Who made what

Melissa (March 19–20, 2025): wrote enemigo.py

made functions that calculate damage, attacks, and critical hits, and used colorama to create both the logo and health bars. Finally, merged both files together.

Angelica (March 19–20, 2025): wrote the entire main.py file, developed the main motor of the game, using functions for the hero, hits, health system, and menu options.

Blockers

Two files with different variables were causing merge conflicts. To fix this, we had to simplify the code and unify variables.

Finally, the game was running.

How to play
First, you pick your enemy from a list of four options. Then the battle starts with a menu that showcases 3 options. After that, you continue to play until one of the players reaches 0 HP.

