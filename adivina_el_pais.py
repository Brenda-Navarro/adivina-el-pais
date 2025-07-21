import random

# Diccionario de países
paises = {
    "ALEMANIA": "Su capital fue dividida por un muro durante la Guerra Fría",
    "FRANCIA": "Su revolución marcó un antes y un después en la historia mundial",
    "ITALIA": "Su territorio forma una figura que recuerda una bota",
    "ESPAÑA": "Antiguo imperio cuya lengua es hoy una de las más habladas del mundo",
    "PORTUGAL": "Cuna de grandes navegantes de la era de los descubrimientos",
    "SUIZA": "País neutral, famoso por sus relojes, chocolate y bancos",
    "SUECIA": "Monarquía escandinava con premios de ciencia y paz",
    "NORUEGA": "Famoso por sus fiordos y haber rechazado unirse a la UE",
    "FINLANDIA": "Su sistema educativo está entre los mejores del mundo",
    "DINAMARCA": "Parte de Escandinavia, tiene una monarquía muy antigua",
    "GRECIA": "Cuna de la filosofía occidental y los Juegos Olímpicos",
    "PAISES BAJOS": "Conocido por sus tulipanes, molinos y políticas progresistas",
    "AUSTRIA": "Tierra de Mozart, montañas y cafés históricos",
    "BÉLGICA": "Sede de la Unión Europea y famosa por sus chocolates",
    "IRLANDA": "Isla esmeralda con gran tradición musical y literaria",
    "POLONIA": "Invadida en 1939, fue el inicio de la Segunda Guerra Mundial",
    "HUNGRÍA": "Ubicada en Europa Central, su idioma es uno de los más difíciles",
    "RUMANIA": "Lugar donde nació la leyenda de Drácula",
    "CHEQUIA": "Antes parte de Checoslovaquia, con capital en Praga",
    "CROACIA": "Destino turístico del Adriático con historia y playas"
}

#Función para construir la palabra con letras adivinadas
def mostrar_palabra(palabra, letras_adivinadas):
    return ' '.join([letra if letra in letras_adivinadas or letra == ' ' else '_' for letra in palabra])

#Mostrar estado del juego
def mostrar_estado(palabra, letras_adivinadas, vidas, letras_incorrectas, pista):
    print("\n🧠 Pista:", pista)
    print("🔤 Palabra:", mostrar_palabra(palabra, letras_adivinadas))
    print("❤️ Vidas restantes:", vidas)
    print("❌ Letras incorrectas:", ' '.join(letras_incorrectas) or "Ninguna")

#Jugar una partida
def jugar_partida():
    palabra, pista = random.choice(list(paises.items()))
    letras_adivinadas = set()
    letras_incorrectas = set()
    vidas = 5

    while vidas > 0:
        mostrar_estado(palabra, letras_adivinadas, vidas, letras_incorrectas, pista)
        intento = input("🔎 Ingresa una letra: ").strip().upper()

        if not intento.isalpha() or len(intento) != 1:
            print("⚠️ Ingresa solo UNA letra.")
            continue

        if intento in letras_adivinadas or intento in letras_incorrectas:
            print("🔁 Ya usaste esa letra.")
            continue

        if intento in palabra:
            letras_adivinadas.add(intento)
            print("✅ ¡Correcto!")
        else:
            letras_incorrectas.add(intento)
            vidas -= 1
            print("❌ ¡Incorrecto! Pierdes una vida.")

        if all(letra in letras_adivinadas or letra == ' ' for letra in palabra):
            print(f"\n🎉 ¡Ganaste! Adivinaste el país: {palabra}")
            return

    print(f"\n💀 ¡Perdiste! El país era: {palabra}")

#Bucle principal del juego
def jugar():
    print("🎮 Bienvenido al Ahorcado Europeo 🌍")
    print("🎯 Tu misión: Adivina el país europeo con ayuda de una pista.")
    print("🧩 Tienes 5 vidas, cada error resta una.")
    print("🔄 Puedes volver a jugar tras cada partida.\n")

    while True:
        jugar_partida()
        decision = input("\n🔁 ¿Deseas jugar otra partida? (s/n): ").strip().lower()

        if decision != 's':
            confirmar = input("❓ ¿Presiona 's' para seguir jugando o cualquier otra tecla para salir?: ").strip().lower()
            if confirmar != 's':
                print("\n👋 ¡Gracias por jugar al Ahorcado Europeo! Hasta la próxima.\n")
                break

# === Iniciar juego ===
if __name__ == "__main__":
    jugar()