# Aplicación para acceder a la API de las horas de salida y puesta del sol de la siguiente URL:

# https://api.sunrise-sunset.org/

# Mostrar las horas para una latitud y longitud concretas.

# Incluir un print con texto con los valores de latitud y longitud, y con las horas obtenidas.



import requests

# from pprint import pprint

from geopy.geocoders import Nominatim



geolocator = Nominatim(user_agent="Beca Digitaliza Cisco")



def coordenadas(ciudad):

  location = geolocator.geocode(ciudad)

  return location



def calculoSol(latitud, longitud):

  url = "https://api.sunrise-sunset.org/json"

  headers = {

    "content-type": "application/json"

  }

  body_json={

      "lat": latitud,

      "lng": longitud

  }

  response = requests.request("GET",url,headers=headers,params=body_json)

  # response = requests.post(url,json.dumps(body_json),headers=headers)

  if response.status_code == 200:

    # pprint (response.json())

    responseJson = response.json()

    horaSalida = responseJson["results"]["sunrise"]

    horaPuesta = responseJson["results"]["sunset"]

    print("La hora de salida del Sol es:",horaSalida)

    print("La hora de puesta del Sol es:",horaPuesta)

    print("NOTA: Horas en UTC.")

  else:

    print("Se ha producido un error")



aplicacionON = True



while (aplicacionON):

  try:

    print ("PUESTA Y SALIDA DE SOL")

    print ("Introduce el nombre de una ciudad o código postal")

    print ("q.- Finaliza la aplicación")

    ciudad =input("Ciudad: ")

    if (ciudad == "q"):

      print("Saliendo...")

      aplicacionON = False

    else:

      location = coordenadas(ciudad)

      latYlong = location[1]

      latitud = location[1][0]

      longitud = location[1][1]

      print("Ciudad seleccionada:",location[0])

      print("Latitud:",latitud)

      print("Longitud:",longitud)

      calculoSol(latitud, longitud)

  except:

    print ("Se ha producido un error")