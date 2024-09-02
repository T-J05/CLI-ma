# Creación de la Aplicación CLI
# Usa una librería adecuada para gestionar los argumentos y comandos de la CLI.
from dotenv import load_dotenv
import os
import requests
import argparse
import json
# Carga el archivo .env
load_dotenv()
# Accede a la API key usando el mismo nombre de variable
api_key = os.getenv('API_KEY')


def clima():
    parser = argparse.ArgumentParser(description="Aplicacion para ver el clima desde la linea de comando" )

    parser.add_argument("ciudad",type=str,help="Ingrese la ciudad")
    parser.add_argument("tipo",type=str, nargs="?",default="json",help="Ingrese el formato json/texto")

    argumentos = parser.parse_args()

    ciudad = argumentos.ciudad
    tipo = argumentos.tipo
    # creamos un diccionario que con los parametros para la url
    parametros = {
        "q": ciudad,
        "units": "metric",
        "APPID": api_key
    }
    try:
        # Realizamos la peticion, indicando la url y los parametros
        respuesta= requests.get("http://api.openweathermap.org/data/2.5/weather",params=parametros)
        # si la respuesta devuelve 200 es por que todo salio bien
        if respuesta.status_code == 200:
            # La respuesta json se convierte en un diccionario
            datos = respuesta.json()
            datos_json = datos["main"]  # nos adentramos a la clave main del diccionario
            # traducimos todo a espanhol
            jsonn = { 
                    "temperatura": f"{datos_json['temp']} ºC",
                    "sensacion_termica": f"{datos_json['feels_like']} ºC",
                    "temperatura_minima": f"{datos_json['temp_min']} ºC",
                    "temperatura_maxima": f"{datos_json['temp_max']} ºC",
                    "presion": f"{datos_json['pressure']} hPa",
                    "humedad": f"{datos_json['humidity']}%"
            }
            json_simple = json.dumps(jsonn, ensure_ascii=False, indent=4)  # convertimos el diccionario en json simple para su lectura
            if tipo == "json":  # imprime en json
                print(json_simple)

            elif tipo == "texto":  # imprime en texto
                texto = "\n".join([f"{clave}: {valor}" for clave, valor in jsonn.items()]) 
                print(texto)
            else:
                print('Error formato no admitido o malcescrito.')
        else:
            print("No tengo datos sobre esa ciudad revisa si la ortografia es correcta")
    except requests.RequestException as e:
        print(f"Error en la solicitud {e}")


if __name__ == "__main__":  # para evitar que si se importa el archivo se ejecute
    clima()