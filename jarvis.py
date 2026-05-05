import datetime

print("JARVIS ONLINE")

while True:

    comando = input("Tú: ").lower()

    if comando == "hola":
        print("JARVIS: Buenos días, señor.")

    elif comando == "hora":

        hora = datetime.datetime.now().strftime("%H:%M")

        print("JARVIS: La hora actual es", hora)

    elif comando == "nombre":
        print("JARVIS: Soy JARVIS, su asistente inteligente.")

    elif comando == "ayuda":

        print("""
Comandos:
- hola
- hora
- nombre
- ayuda
- salir
""")

    elif comando == "salir":

        print("JARVIS: Apagando sistemas.")
        break

    else:

        print("JARVIS: Comando no reconocido.")
