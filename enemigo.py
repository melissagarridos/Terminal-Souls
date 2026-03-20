import random

# Stats
enemigo_hp = 120
story = ""

# Type of enemy according to story

def tipo_enemigo():

    path = False

    while not path:

        print("""These are your path options, Hero:
              
            1. Shadow Dungeon: A cold, stone prison.
            2. Eternal Forest: Where the Werewolves howl.
            3. Old Graveyard: Resting place of the restless.
            4. Vampire Castle: The final challenge.    
        """)
        
        story = random.random()

        if story < 0.2:
            nombre_enemigo = "Dragon 🐉"
            escenario = "Special Event! Shadow Dungeon"
            path = True

        elif story < 0.35:
            nombre_enemigo = "Werewolf 🐺🌕"
            escenario = "Eternal Forest"
            path = True

        elif story < 0.65:
            nombre_enemigo = "Zombie 🧟"
            escenario = "Old Graveyard"
            path = True

        else:
            nombre_enemigo = "Vampire 🧛"
            escenario = "Vampire Castle"
            path = True

    return nombre_enemigo, escenario

    
print(tipo_enemigo())


# Attacks

ataque_heroe = random.randint(10, 25)
ataque_enemigo = random.randint(10, 25)

# Function: generate enemy damage between min and max range
def generar_daño_enemigo(min_damage, max_damage):
    return random.randint(15,25)


# print(f"Enemy's damage: {generar_daño_enemigo()}") 

# Function: calculate and apply hero's damage to enemy
def turno_enemigo():
    global enemigo_hp
    enemigo_hp = enemigo_hp - ataque_heroe
    return enemigo_hp

# Function: display current enemy health bar on screen
def mostrar_estado_enemigo():
    global enemigo_hp

    ancho = 12
    hp_max = 120
    nombre_enemigo, escenario = tipo_enemigo() 
    llenos = (enemigo_hp * ancho) // hp_max
    vacio = ancho - llenos
    barra = "[" + "█" * llenos + "░" * vacio + "]"
    
    estado = f"Status {nombre_enemigo}: {barra} {enemigo_hp} / 120 HP"

    return estado
    

print(mostrar_estado_enemigo())

# Function: basic AI - enemy heals if HP drops below 20%
def aumentar_enemigohp():
    global enemigo_hp

    if enemigo_hp <= 24:
        curarse = random.choice([True, False])

        if curarse is True:
            enemigo_hp = enemigo_hp + 20
            print("Enemy decided to heal! +20 HP")  # <-- print nuevo

    return enemigo_hp

# Function: 10% chance any attack deals double damage (critical hit)
def daño_critico():
    local_ataque = ataque_enemigo  # 

    if random.random() < 0.1:
        local_ataque = local_ataque * 2
        print("Critical hit! Double damage!")  

    return local_ataque
