# Función para calcular el factorial de un número natural, sin importar
def factorial():
  numero_natural = int(
      input("Ingrese un número natural: "))  # Definir variable, que el usuario ingrese un número natural
  factorial = 1  # Definir variable que almacene el factorial del número
  multiplicador = 1  # Definir variable que almacene el multiplicador del factorial

  while multiplicador <= numero_natural:  # Mientras que el multiplicador sea menor o igual al número natural
    factorial *= multiplicador  # Actualizar el factorial (factorial = factorial * multiplicador)
    multiplicador += 1  # Actualizar el multiplicador (multiplicador = multiplicador + 1)
  print("El factorial de", numero_natural, "es", factorial)  # Imprimir el factorial del número natural


# Iniciar programa
if __name__ == '__main__':
  factorial()  # Llamar programa