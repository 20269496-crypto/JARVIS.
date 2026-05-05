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

elif comando == "fecha":

fecha = datetime.datetime.now().strftime("%d/%m/%Y")

print("JARVIS: La fecha actual es", fecha)

elif comando == "como estas":

print("JARVIS: Todos los sistemas están operativos, señor.")

elif comando == "quien creo jarvis":

print("JARVIS: Usted está construyendo este sistema.")

 elif comando == "youtube":

print("JARVIS: Abriendo YouTube...")
        webbrowser.open("https://youtube.com")

 elif comando == "google":

print("JARVIS: Abriendo Google...")
        webbrowser.open("https://google.com")

elif "buscar" in comando:

 busqueda = comando.replace("buscar", "")

 print("JARVIS: Buscando", busqueda)

webbrowser.open(
            "https://www.google.com/search?q=" + busqueda
        )

elif "cuanto es" in comando:

 operacion = comando.replace("cuanto es", "")

try:

 resultado = eval(operacion)

print("JARVIS:", resultado)

 except:

print("JARVIS: No pude calcular eso.")

elif comando == "nombre":

print("JARVIS: Soy JARVIS, su asistente inteligente.")

elif comando == "ayuda":

print("""

COMANDOS DISPONIBLES:

- hola
- hora
- fecha
- como estas
- quien creo jarvis
- youtube
- google
- buscar inteligencia artificial
- cuanto es 5+5
- nombre
- ayuda
- salir

""")

elif comando == "salir":

 print("JARVIS: Apagando sistemas.")
        break
        
else:

 print("JARVIS: Comando no reconocido.")
