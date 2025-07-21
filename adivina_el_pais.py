import random

# ========= 1. Diccionario con 20 países y sus pistas =========
paises = {
    "ITALIA": "País europeo con forma de bota.",
    "PERU": "Tiene Machu Picchu y está en Sudamérica.",
    "JAPON": "Isla asiática famosa por su tecnología.",
    "EGIPTO": "Conocido por las pirámides y el Nilo.",
    "CANADA": "País muy frío en América del Norte.",
    "INDIA": "Tiene el Taj Mahal y muchas especias.",
    "CHILE": "País largo y angosto en Sudamérica.",
    "KENIA": "Famoso por sus safaris africanos.",
    "GRECIA": "Cuna de la democracia.",
    "AUSTRALIA": "Donde viven los canguros.",
    "MEXICO": "Tiene mariachi, tacos y tequila.",
    "CHINA": "Gran Muralla y dragones.",
    "ESPAÑA": "Flamenco, paella y siesta.",
    "FRANCIA": "La Torre Eiffel y el vino.",
    "ALEMANIA": "Cuna de Beethoven y los autos.",
    "ARGENTINA": "Famosa por el tango y Messi.",
    "BRASIL": "Samba, carnaval y Amazonía.",
    "COLOMBIA": "Café, arepas y flores.",
    "TURQUIA": "Cruce entre Europa y Asia.",
    "COREA": "Del K-pop y alta tecnología."
}

# ========= 2. Decorador para imprimir separadores =========
def separar(func):
    def wrapper(*args, **kwargs):
        print("\n" + "-" * 45)
        resultado = func(*args, **kwargs)
        print("-" * 45 + "\n")
        return resultado
    return wrapper

# ========= 3. Generador para mostrar progreso =========
def generar_ocultas(palabra, letras):
    return (letra if letra in letras else "_" for letra in palabra)

# ========= 4. Función anidada para validar la letra =========
def obtener_letra():
    def es_valida(letra):
        return letra.isalpha() and len(letra) == 1
    while True:
        entrada = input("Ingresa una letra: ").upper()
        if es_valida(entrada):
            return entrada
        print("❌ Solo se acepta UNA letra válida del alfabeto.")

# ========= 5. Mostrar estado del juego =========
@separar
def mostrar_estado(palabra, letras_correctas, letras_erradas, vidas, pista):
    progreso = " ".join(generar_ocultas(palabra, letras_correctas))
    print(f"📌 Pista: {pista}")
    print(f"🔤 Palabra: {progreso}")
    print(f"❤️ Vidas restantes: {vidas}")
    if letras_erradas:
        print(f"❌ Letras incorrectas: {', '.join(sorted(letras_erradas))}")

# ========= 6. Juego principal con *args y **kwargs =========
def jugar_adivina_el_pais(*args, **kwargs):
    palabra, pista = random.choice(list(paises.items()))
    letras_correctas = set()
    letras_erradas = set()
    vidas = kwargs.get("vidas", 6)

    while True:
        mostrar_estado(palabra, letras_correctas, letras_erradas, vidas, pista)
        letra = obtener_letra()

        if letra in letras_correctas or letra in letras_erradas:
            print("⚠️ Ya ingresaste esa letra.")
            continue

        if letra in palabra:
            letras_correctas.add(letra)
        else:
            letras_erradas.add(letra)
            vidas -= 1

        if set(palabra) <= letras_correctas:
            mostrar_estado(palabra, letras_correctas, letras_erradas, vidas, pista)
            print("🎉 ¡Felicidades! Adivinaste el país correctamente.")
            break
        elif vidas == 0:
            mostrar_estado(palabra, letras_correctas, letras_erradas, vidas, pista)
            print(f"💀 ¡Perdiste! El país era: {palabra}")
            break

# ========= 7. Recursividad para repetir el juego =========
def iniciar_juego():
    jugar_adivina_el_pais(vidas=6)
    otra = input("¿Deseas jugar otra vez? (s/n): ").lower()
    if otra == "s":
        iniciar_juego()
    else:
        print("👋 ¡Gracias por jugar 'Adivina el País'!")

# ========= 8. Inicio del juego =========
if __name__ == "__main__":
    print("🌍 Bienvenido a 'Adivina el País'")
    print("Adivina letra por letra el país oculto.")
    print("Tienes 6 vidas. Cada error te cuesta una vida.")
    iniciar_juego()