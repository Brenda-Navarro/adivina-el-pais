import random

<<<<<<< HEAD
# 🎨 Decoradores visuales
def decorador_bienvenida(func):
    def wrapper():
        print("💫🌐 ¡Bienvenido, al ahorcado de países! 🌐💫")
        print("🧭🌍 Prepárate para recorrer el mundo adivinando países ocultos.")
        print("🏁 ¡Tu sabiduría geográfica será puesta a prueba!")
        print("🎮 Cada acierto suma puntos. ¿Podrás alcanzar la gloria global?")
        print("📌 Instrucciones:")
        print("🔢 1. Elige una región del mundo escribiendo su número.")
        print("🔡 2. Intenta adivinar el país letra por letra.")
        print("❤️ 3. Tienes 5 vidas. Con cada error... el ahorcado aparecerá.")
        print("💡 4. ¡Pistas aparecerán si estás en apuros!")
        print("🏆 5. Reconocimientos por cada hito alcanzado (de 10 a 1000 puntos)")
        print("🚀 ¡Buena suerte, explorador!\n")
        func()
    return wrapper

# 🎭 Muñeco del ahorcado progresivo
ahorcado_visual = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ========="""
]

# 🌎 Diccionario de países por región con pistas más complejas
paises_por_region = {
    "1": [  # Europa
        ("portugal", "Su capital es Lisboa y es famoso por su vino de Oporto."),
        ("alemania", "Es líder en la industria automotriz y su capital es Berlín."),
        ("francia", "Tiene la Torre Eiffel y es famoso por su gastronomía."),
        ("italia", "Tiene forma de bota y su capital es Roma."),
        ("noruega", "Conocido por sus fiordos y auroras boreales."),
        ("grecia", "Cuna de la democracia y del Partenón."),
        ("suecia", "Famoso por IKEA y los Premios Nobel."),
        ("polonia", "Su capital es Varsovia y sufrió mucho en la II Guerra Mundial."),
        ("suiza", "Neutral en guerras, famosa por sus relojes y chocolate."),
        ("austria", "Mozart nació aquí y su capital es Viena.")
    ],
    "2": [  # Asia
        ("japon", "Isla tecnológica con el Monte Fuji."),
        ("china", "Tiene la Gran Muralla y es la nación más poblada."),
        ("corea", "Hay del Norte y del Sur; una famosa por el K-pop."),
        ("india", "Tiene el Taj Mahal y una gran diversidad cultural."),
        ("tailandia", "Famosa por sus templos y playas."),
        ("vietnam", "Conocido por la bahía de Ha Long."),
        ("indonesia", "Conjunto de miles de islas, entre ellas Bali."),
        ("malasia", "Sus torres Petronas son muy conocidas."),
        ("arabia", "Produce mucho petróleo, su capital es Riad."),
        ("iran", "Antiguamente llamado Persia.")
    ],
    "3": [  # África
        ("nigeria", "Es el país más poblado de África."),
        ("kenia", "Famoso por sus safaris y el Valle del Rift."),
        ("egipto", "Hogar de las pirámides y el Nilo."),
        ("sudafrica", "Tiene tres capitales y fue sede del mundial 2010."),
        ("marruecos", "Famoso por sus zocos y la ciudad de Marrakech."),
        ("argelia", "El país más grande de África en superficie."),
        ("ghana", "Uno de los países más democráticos del oeste africano."),
        ("etiopia", "Nunca fue colonizado y su calendario es diferente."),
        ("senegal", "Conocido por el lago Rosa y su música."),
        ("tunez", "Tiene ruinas romanas y playas mediterráneas.")
    ],
    "4": [  # América (Norte, Centro y Sur)
        ("mexico", "Famoso por el Día de Muertos y los tacos."),
        ("canada", "Gran extensión, sirope de arce y hockey."),
        ("brasil", "Tiene el Amazonas y es hogar del Carnaval."),
        ("chile", "Estrecho y largo país con desierto de Atacama."),
        ("colombia", "Famoso por su café y diversidad."),
        ("peru", "Tiene Machu Picchu y la cultura inca."),
        ("argentina", "Tango, carne y el glaciar Perito Moreno."),
        ("uruguay", "Pequeño, tranquilo y con muchas playas."),
        ("panama", "Conecta dos océanos con su canal."),
        ("cuba", "Isla del Caribe con gran historia y música.")
    ],
    "5": [  # Oceanía
        ("australia", "Gran isla famosa por los canguros."),
        ("nueva zelanda", "Escenario de El Señor de los Anillos."),
        ("fiyi", "Archipiélago tropical famoso por sus playas."),
        ("samoa", "Pequeña isla con mucha cultura polinesia."),
        ("tonga", "Una monarquía en medio del Pacífico."),
        ("palaos", "Conocido por su biodiversidad marina."),
        ("kiribati", "Su territorio se dispersa en el Pacífico."),
        ("tuvalu", "Uno de los países más pequeños y bajos."),
        ("nauru", "El país insular más pequeño del mundo."),
        ("vanuatu", "Conocido por su cultura ancestral y volcanes.")
    ]
}

def obtener_reconocimiento(score):
    if score < 100:
        return "🌱 Principiante geográfico"
    elif score < 300:
        return "🌍 Explorador continental"
    elif score < 600:
        return "🚀 Aventurero global"
    elif score < 1000:
        return "🎓 Maestro geográfico"
    else:
        return "👑 Leyenda mundial del conocimiento"

@decorador_bienvenida
def iniciar_juego():
    puntaje = 0
    while True:
        print("\n📚 Regiones disponibles:")
        print("1. Europa 🌍")
        print("2. Asia 🕌")
        print("3. África 🌍")
        print("4. América 🌎")
        print("5. Oceanía 🐠")

        region = input("👉 Ingresa el número de la región que deseas jugar: ").strip()
        if region not in paises_por_region:
            print("⚠️ Región inválida. Intenta de nuevo.\n")
            continue

        palabra, pista = random.choice(paises_por_region[region])
        palabra_oculta = ["_" for _ in palabra]
        letras_adivinadas = set()
        vidas = 5

        while vidas > 0 and "_" in palabra_oculta:
            print(ahorcado_visual[5 - vidas])
            print("🧩 Palabra:", " ".join(palabra_oculta))
            print(f"❤️ Vidas restantes: {vidas} | 🎯 Puntos: {puntaje}")
            letra = input("🔠 Ingresa una letra: ").lower()

            if not letra.isalpha() or len(letra) != 1:
                print("⚠️ Por favor, ingresa solo una letra.")
                continue

            if letra in letras_adivinadas:
                print("🔁 Ya has usado esa letra.")
                continue

            letras_adivinadas.add(letra)

            if letra in palabra:
                for idx, char in enumerate(palabra):
                    if char == letra:
                        palabra_oculta[idx] = letra
            else:
                vidas -= 1
                if vidas == 3:
                    print(f"💡 Pista: {pista}")

        if "_" not in palabra_oculta:
            puntaje += 10
            print(f"🎉 ¡Correcto! La palabra era '{palabra.upper()}'.")
            print(f"🏆 Has ganado 10 puntos. Puntaje total: {puntaje}")
            print(f"🎖 Reconocimiento: {obtener_reconocimiento(puntaje)}")
        else:
            print(ahorcado_visual[6])
            print(f"😵 ¡Oh no! Perdiste. La palabra era: {palabra.upper()}")
            print(f"🎯 Puntaje actual: {puntaje}")
            print(f"🎖 Reconocimiento: {obtener_reconocimiento(puntaje)}")

        seguir = input("🔁 ¿Quieres continuar? (si / no): ").strip().lower()
        if seguir == "no":
            volver = input("🔄 ¿Quieres volver en otro momento? Escribe 'volver' para regresar: ").strip().lower()
            if volver == "volver":
                continue
            else:
                print("👋 ¡Gracias por jugar! Hasta la próxima.")
                break
        elif seguir != "si":
            print("❓ Entrada no reconocida. Saliendo del juego.")
            break

# 🧩 Iniciar el juego
iniciar_juego()
=======
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
>>>>>>> bbdc4c235d728bfd932b77e66986aa4f79041042
