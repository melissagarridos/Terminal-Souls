import random
import melisa

# ============================================================
# Stats del héroe - Mari
# ============================================================

heroe_hp = 100
hp_max_heroe = 100
pociones = 3
nombre_heroe = "Hero ⚔️"  #No pondre ningun nombre porque me daña todo y no tengo paciencia -_-

# ============================================================
#  MIS FUNCIONES
# ============================================================

# Barra de vida del héroe (Mari (me copie de Melisa pero la adapte al player))
def mostrar_estado_heroe():
    global heroe_hp
    ancho = 12
    llenos = max(0, (heroe_hp * ancho) // hp_max_heroe)
    vacio = ancho - llenos
    barra = "[" + "█" * llenos + "░" * vacio + "]"
    return f"Status {nombre_heroe}: {barra} {heroe_hp} / {hp_max_heroe} HP"

# Mostrar estado de ambos (Mari y Melisa)
def mostrar_estado():
    print("\n" + "═" * 40)
    print(mostrar_estado_heroe())
    print(melisa.mostrar_estado_enemigo()) # Mostrar estado del enemigo es de Melisa
    print("═" * 40 + "\n")

# Crítico del héroe: 10% de doble daño (Mari)
def daño_critico_heroe(daño_base):
    if random.random() < 0.1:
        daño_base = daño_base * 2
        print("  ⚡ ¡Golpe critico! ¡Doble daño! 😱")
    return daño_base

# Verificar si alguien murió (Mari y Melisa)

def verificar_ganador():
    end = False
    if heroe_hp <= 0:
        print("\n💀 ¡El héroe ha caído! El enemigo gana...\n")
        end = True
    if melisa.enemigo_hp <= 0:
        print(f"\n🏆 ¡Victoria! ¡Derrotaste al {melisa.nombre_enemigo}!\n")
        end = True
    return end

# Turno del jugador (Mari)

def turno_jugador():
    global heroe_hp, pociones

    accion_valida = False

    while not accion_valida:
        print(f"  🧪 Pociones restantes: {pociones}")
        print("\n  ¿Qué harás?\n")
        print("  1. Atacar             (daño: 10-25)")
        print("  2. Curar              (recupera 20 HP)")
        print("  3. Habilidad especial (daño: 30-50, 50% de fallar)\n")
        
        eleccion = input("  Tu elección (1-3): ").strip()

        if eleccion == "1":
            daño = daño_critico_heroe(random.randint(10, 25))
            melisa.enemigo_hp = max(0, melisa.enemigo_hp - daño)
            print(f"\n  ⚔️  ¡El héroe ataca por {daño} de daño!")
            accion_valida = True

        elif eleccion == "2":
            if pociones <= 0:
                print("\n  ❌ ¡No te quedan pociones! Elige otra acción.\n")
                continue

            elif heroe_hp >= 100:
                print("\n ¡Tienes la vida full!")
                continue
            
            else:
                heroe_hp = min(heroe_hp + 20, hp_max_heroe)
                pociones -= 1
                print(f"\n  💊 ¡Te curaste! +20 HP. Pociones restantes: {pociones}")
                accion_valida = True

        elif eleccion == "3":
            if random.random() < 0.5:
                daño = daño_critico_heroe(random.randint(30, 50))
                melisa.enemigo_hp = max(0, melisa.enemigo_hp - daño)
                print(f"\n  🌟 ¡Habilidad especial! ¡Causas {daño} de daño!")
            else:
                print("\n  😬 ¡La habilidad especial falló! No pasó nada.")
            accion_valida = True

        else:
            print("\n  ⚠️  Opción inválida. Elige 1, 2 o 3.\n")


# Turno del enemigo (IA básica: se cura si HP <= 20%, sino ataca con posibilidad de crítico)
def turno_enemigo_completo(): #Esto es de Melisa pero lo unifique con el mio
    global heroe_hp

    # IA MELISA: intenta curarse si HP <= 24
    melisa.aumentar_enemigohp()

    # Ataca con posibilidad de crítico (MELISA)
    daño = melisa.daño_critico()
    heroe_hp = max(0, heroe_hp - daño)
    print(f"  🔥 ¡{melisa.nombre_enemigo} ataca por {daño} de daño!")

# Bucle principal (Mari)

def jugar():
    turno = 1
    jugando = True
    print("\n⚔️  ¡Que comience el combate!\n")
    
    while jugando:
        print(f"\n============ Turno {turno} ============")
        mostrar_estado()

        turno_jugador()
        if verificar_ganador():
            jugando = False

        turno_enemigo_completo()
        if verificar_ganador():
            jugando = False

        turno += 1


# ============================================================
#  INICIO DEL JUEGO - Mari
# ============================================================

jugar()