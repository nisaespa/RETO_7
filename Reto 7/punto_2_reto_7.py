# Función para imprimir los números impares desde 1 a 999
def numeros_impares():
  numero1 = 1  # Declarar variable, en este caso para que comience desde 1
  print("Números impares del 1 al 999")
  while numero1 <= 999:  # Sí el número es menor que 999, entonces
    if numero1 % 2 != 0:  # Si el número es impar, entonces
      print(numero1)  # Imprimir número impar
    numero1 += 1  # Actualizar hasta que se llegue a 999


# Función para imprimir los números pares desde 2 a 1000
def numeros_pares():
  numero2 = 2  # Declarar variable, en este caso para que comience desde 2
  print("Números pares del 2 al 1000")
  while numero2 <= 1000:  # Sí el número es menor que 1000, entonces
    if numero2 % 2 == 0:  # Si el número es par, entonces
      print(numero2)  # Imprimir número par
    numero2 += 1  # Actualizar hasta que se llegue a 1000


# Iniciar programa
if __name__ == '__main__':
  numeros_impares()  # Llamar función
  numeros_pares()  # Llamar función