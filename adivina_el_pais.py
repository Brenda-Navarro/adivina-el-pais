
import random

# Lista de países
paises = ['argentina', 'portugal', 'tailandia', 'ucrania', 'canada', 'kenia', 'vietnam', 'suecia', 'egipto', 'paraguay']

def elegir_palabra():
    return random.choice(paises)

def mostrar_palabra(palabra, letras_adivinadas):
    return " ".join([letra if letra in letras_adivinadas else "_" for letra in palabra])

def jugar():
    palabra = elegir_palabra()
    letras_adivinadas = set()
    letras_incorrectas = set()
    vidas = 6

    print("\n🌎 ¡Bienvenido a Adivina el País!")

    while vidas > 0:
        print("\nPaís:", mostrar_palabra(palabra, letras_adivinadas))
        print(f"❤️ Vidas: {vidas}")
        print(f"❌ Letras incorrectas: {', '.join(sorted(letras_incorrectas))}")

        intento = input("🔤 Ingresa una letra: ").lower()

        if len(intento) != 1 or not intento.isalpha():
            print("⚠️ Por favor, ingresa una sola letra válida.")
            continue

        if intento in letras_adivinadas or intento in letras_incorrectas:
            print("⚠️ Ya has intentado esa letra.")
            continue

        if intento in palabra:
            letras_adivinadas.add(intento)
            print("✅ ¡Bien! Esa letra está en el país.")
        else:
            letras_incorrectas.add(intento)
            vidas -= 1
            print("❌ Esa letra no está en el país.")

        if all(letra in letras_adivinadas for letra in palabra):
            print(f"\n🎉 ¡Ganaste! El país era: {palabra.upper()}")
            break
    else:
        print(f"\n💀 ¡Perdiste! El país era: {palabra.upper()}")

def menu():
    while True:
        jugar()
        opcion = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
        if opcion != "s":
            print("👋 ¡Gracias por jugar! Hasta la próxima.")
            break

if __name__ == "__main__":
    menu()
