# Crear una app para saber el número de personas que hay en el espacio

# http://open-notify.org/Open-Notify-API/



import requests



def calcular():

  url = "http://api.open-notify.org/astros.json"

  req = requests.request("GET",url)

  responseJson = req.json()

  numeroPersonas = responseJson["number"]

  print("Número de personas en el espacio:",numeroPersonas)



aplicacionON = True

while (aplicacionON):

  try:

    print("HUMAN IN SPACE RIGHT NOW?")

    print("1.- Calcular")

    print("q.- Salir")

    opcion = input()

    if opcion == "1":

      calcular()

    elif opcion == "q":

      print("Saliendo...")

      aplicacionON = False

    else:

      print("Introduce una opción correcta")

  except:

    print("Se ha producido un error")