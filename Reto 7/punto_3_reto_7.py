# Función para dado un numero natural, imprimir los números pares menores
def numeros_pares_descendente():
  numero = int(input("Escriba un número natural: "))  # Declarar variable
  while numero >= 2:  # Mientras que el numero sea mayor o igual a 2, entonces
    if numero % 2 == 0:  # Si el numero es par, entonces
      print(numero)  # Imprimir numero
    numero -= 1  # Actualización para que vaya descendiendo hasta 2


# Iniciar programa
if __name__ == '__main__':
  numeros_pares_descendente()  # Llamar función
    