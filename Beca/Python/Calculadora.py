print ("************CALCULADORA************")

def introduce():

  numero = (float)(input("Escribe un número: "))

  return numero



def suma(numero1,numero2):

  print ("_El resultado de la suma es_ ",numero1 + numero2)
  





def resta(num1,num2):

  print ("_El resultado de la suma es_ ",numero1 - numero2)



def multiplicacion(numero1,numero2):

  print ("_El resultado de la multiplicación es_ ",numero1 * numero2)



def division(numero1,numero2):

  print ("_El resultado de la división es_ ",numero1 / numero2)



def exponencial(numero1,numero2):

  print ("_El resultado de la exponencial es_",numero1 ** numero2)



opciones={1:suma,2:resta,3:multiplicacion,4:division,5:exponencial}

calculadora = True



while (calculadora):

  try:



    print ("Selecciona la operación a realizar:")

    print ("1.- Suma")

    print ("2.- Resta")

    print ("3.- Multiplicacion")

    print ("4.- División")

    print ("5.- Exponencial")

    print ("6.- Salir")

    eleccion =input("Escoge una opción: ")

    if (eleccion == "6"):

      print("Slitz Bai!!")

      calculadora = False

    else:

      eleccion = int(eleccion)

      if (0 < eleccion <= 5):

        numero1 = introduce()

        numero2 = introduce()

        opciones[eleccion](numero1,numero2)

      else:

        print("OPCIÓN INCORRECTA")

  except ZeroDivisionError:

    print ("Imposible dividir entre 0")

