# Función para calcular los divisores de un número natural dado entre 2 a 50
def divisores():
  numero_natural = int(
      input("Escriba número natural desde 2 a 50: "))  # Definir variable, que el usuario elija un número natural entre 2 a 50
  divisor = 1  # Definir variable, que es el divisor que empieza desde 1
  # Crear un bucle que cumpla con 3 condiciones, si alguna es False, no se inicia el bucle
  while numero_natural >= 2 and numero_natural <= 50 and divisor <= numero_natural:
    if numero_natural % divisor == 0:  # Si el residuo es 0, entonces el divisor cuenta como divisor (si comienza la variable divisor desde 1, siempre imprimira 1, ya que es divisor de cualquier número natural entre 2 a 50)
      print("El número", numero_natural, "es divisible por: ",
            divisor)  # Imprime el número y el divisor
      divisor += 1  # Actualiza el divisor, en este caso empieza desde 1 hasta 50
    else:
      divisor += 1  # Actualiza el divisor, en este caso empieza desde 1 hasta 50


# Iniciar programa
if __name__ == '__main__':
  divisores()  # Llamar Función
