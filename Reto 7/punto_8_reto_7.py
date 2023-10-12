# Función para números primos desde 1 hasta 100
def numeros_primos_hasta_cien():
  primo1 = 2  # Definir variable
  primo2 = 2  # Definir variable
  while 2 <= primo1 < 8:  # Mientras que primo1 sea menor que 8 y mayor igual a 2
    if primo1 == 3:  # Sí primo1 es igual a 3
      print(primo1 - 1)  # Imprimir 2
      print(primo1)  # Imprimir 3
    elif primo1 % 2 != 0:  # Sí primo1 no es par
      print(primo1) # Imprimir los impares
    primo1 += 1 # Actualizar variable, hasta que llegue a 8
  while primo2 < 101: # Mientras que primo2 sea menor que 101
    if  primo2 % 2 != 0 and primo2 % 3 != 0 and primo2 % 5 != 0 and primo2 % 7 != 0: # Si se cumplen las condiciones primo2 es un número primo
      print(primo2) # Imprimir número primo
    primo2 += 1 # Actualizar variable, hasta que llegue a 101


# Iniciar programa
if __name__ == '__main__':
  print("Los números primos desde 1 hasta 100 son:")
  numeros_primos_hasta_cien() # Llamar función