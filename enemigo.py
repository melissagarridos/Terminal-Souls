import random

# Stats
nombre_enemigo = "Dragon 🐉"
enemigo_hp = 120

# Function generate damage - enemy between 15 and 20
def generar_daño_enemigo(min_damage, max_damage):

    return random.randint(min_damage, max_damage)

print(f"Enemy's Damage: {generar_daño_enemigo(15,20)}")

# Calculate and apply hero's damage
def turno_enemigo(enemigo_hp):

    ataque_heroe = random.randint(10, 25)
    enemigo_hp = enemigo_hp - ataque_heroe

    return enemigo_hp

# Function show HP - enemy
def mostrar_estado_enemigo(enemigo_hp):

    ancho = 12
    hp_max = 120
    llenos = (enemigo_hp * ancho) // hp_max
    vacio = ancho - llenos
    barra = "[" + "█" * llenos + "░" * vacio + "]"

    print(f"Status {nombre_enemigo}: {barra} {enemigo_hp} / 120 HP")

# AI system to heal enemy
def aumentar_enemigohp():

    global enemigo_hp

    if enemigo_hp <= 24:
        curarse = random.choice([True, False])

        if curarse is True:
            enemigo_hp = enemigo_hp + 20
 
    return enemigo_hp

# # --- Simulación de turnos ---
# enemigo_hp = turno_enemigo(enemigo_hp)   # turno 1 — guarda el nuevo HP
# mostrar_estado_enemigo(enemigo_hp)

# enemigo_hp = aumentar_enemigohp()        # el enemigo intenta curarse
# mostrar_estado_enemigo(enemigo_hp)

# enemigo_hp = turno_enemigo(enemigo_hp)   # turno 2 — parte del HP anterior
# mostrar_estado_enemigo(enemigo_hp)