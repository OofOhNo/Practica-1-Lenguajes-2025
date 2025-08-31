#piedra-papel-tijera.py
#Juego simple contra la computadora: primera version

import random

opciones = ["piedra", "papel", "tijera"]
ronda_maxima = 1

print("¡Bienvenido! Vamos a jugar a Piedra, Papel o Tijera.")
print("Escribí la cantidad de rondas a jugar.")
while True:
    entrada = input("Cantidad de rondas: ")
    try:
        ronda_maxima = int(entrada)
        break
    except ValueError:
        print("Entrada no válida. Debe ser un numero.")
print("Escribí tu jugada (piedra/papel/tijera).")

ronda = 1
puntos_usuario = 0
puntos_pc = 0
puntos_para_ganar = (ronda_maxima // 2) + 1

while ronda <= ronda_maxima:
    print(f"\nRonda {ronda}")
    jugada_usuario = input("Tu jugada: ").strip().lower()



    while jugada_usuario not in opciones:
        print("Entrada no válida. Debe ser piedra, papel o tijera.")
        jugada_usuario = input("Tu jugada valida: ").strip().lower()


    jugada_pc = random.choice(opciones)
    print(f"La computadora eligió: {jugada_pc}")

    if jugada_usuario == jugada_pc:
        print("Empate.")
    elif (
        (jugada_usuario == "piedra" and jugada_pc == "tijera") or
        (jugada_usuario == "papel" and jugada_pc == "piedra") or
        (jugada_usuario == "tijera" and jugada_pc == "papel")
    ):
        print("¡Ganaste la ronda!")
        puntos_usuario += 1
    else:
        print("Perdiste la ronda.")
        puntos_pc += 1
    
    if ((puntos_pc >= puntos_para_ganar) or (puntos_usuario >= puntos_para_ganar)):
        break
    
    ronda += 1

print("\n=== Resultado final ===")
print(f"Tus puntos: {puntos_usuario} | Puntos de la pc: {puntos_pc}")

if puntos_usuario > puntos_pc:
    print("¡Ganaste el juego! 🎉")
elif puntos_usuario < puntos_pc:
    print("La computadora ganó el juego.")
else:
    print("Empate total.")