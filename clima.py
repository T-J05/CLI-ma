# Creación de la Aplicación CLI

# Usa una librería adecuada para gestionar los argumentos y comandos de la CLI.
from dotenv import load_dotenv
import os
import requests

# Carga el archivo .env
load_dotenv()
# Accede a la API key usando el mismo nombre de variable
api_key = os.getenv('API_KEY')

# Pedimos al usuario la ciudad del que quiere ver su pronostico
ciudad = input ("Ingrese la ciudad de la quiera ver su pronostico: ")

# creamos un diccionario que con los parametros para la url
parametros = {"q":ciudad,
              "units":"metric",
              "APPID":api_key}

# realizamos la peticion, indicando la url y los parametros
respuesta= requests.get("http://api.openweathermap.org/data/2.5/weather",params=parametros)

# si la respuesta devuelve 200 es por que todo salio bien
if respuesta.status_code == 200:
# La respuesta json se convierte en un diccionario
    datos = respuesta.json()

    # Se obtienen los valores del diccionario
    print("La temperatura actual es:",datos["main"]["temp"],"ºC")
    print("La sensación térmica es:",datos["main"]["feels_like"],"ºC")
    print("La temperatura mínima es:",datos["main"]["temp_min"],"ºC")
    print("La temperatura máxima es:",datos["main"]["temp_max"],"ºC")
    print("La presión es:",datos["main"]["pressure"],"hPa")
    print("La humedad es:",datos["main"]["humidity"],"%")
else:
    print("No tengo datos sobre esa ciudad")