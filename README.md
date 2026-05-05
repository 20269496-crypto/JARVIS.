import datetime
import webbrowser

print("JARVIS ONLINE")

while True:

    comando = input("Tú: ").lower()

    if comando == "hola":

        print("JARVIS: Buenos días, señor.")

    elif comando == "hora":

        hora = datetime.datetime.now().strftime("%H:%M")

        print("JARVIS: La hora actual es", hora)

    elif comando == "youtube":

        print("JARVIS: Abriendo YouTube...")
        webbrowser.open("https://youtube.com")

    elif comando == "google":

        print("JARVIS: Abriendo Google...")
        webbrowser.open("https://google.com")

    elif comando == "2+2":

        print("JARVIS: El resultado es 4.")

    elif comando == "nombre":

        print("JARVIS: Soy JARVIS, su asistente inteligente.")

    elif comando == "ayuda":

        print("""
COMANDOS:
- hola
- hora
- youtube
- google
- 2+2
- nombre
- ayuda
- salir
""")

    elif comando == "salir":

        print("JARVIS: Apagando sistemas.")
        break

    else:

        print("JARVIS: Comando no reconocido.")
