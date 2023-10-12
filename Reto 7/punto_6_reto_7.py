# Función para adivinar un número del 1 al 100
def adivinar_numero():
  print("Piensa en un número entre el 1 y el 100")
  maximo = 100  # Definir variable
  minimo = 1  # Definir variable
  
  while True:  # Bucle infinito, hasta que lo pare un "break" o un "continue"
    numero = (maximo + minimo) // 2  # Definir variable, en este caso el número es la mitad de la suma de los máximo y el mínimo, sin decimal
    pregunta_respuesta = (input(f"El número es: {numero}?, responde 'igual' si sí es, 'menor' si es menor o 'mayor' si es mayor "))  # Definir variable, pregunta al usuario si el número es igual, menor o mayor a la variable "numero" (en la primera iteración el numero es 50)
    if pregunta_respuesta == 'igual':  # Si la respuesta es igual
      print(f"Adiviné tu número, es {numero}")  # Imprimir que se adivinó el número
      break  # Romper ciclo
    elif pregunta_respuesta == 'menor':  # Sino, si la respuesta es menor, entonces
      maximo = numero - 1  # Actualizar la variable máximo, en este caso la variable máximo es el número menos 1 (Es decir que pasa de 100 a 49)
    elif pregunta_respuesta == 'mayor':  # Sino, si la respuesta es mayor, entonces
      minimo = numero + 1  # Actualizar la variable minimo, en este caso la variable mínimo es el número más 1 (Es decir que pasa de 1 a 51)
    else:  # Sino, entonces
      print("Escriba solamente 'mayor' , 'menor' e 'igual'")  # El usuario no escogío una de las respuestas válidas, entonces vuelve a empezar el bucle infinito, hasta que diga que es igual, menor o mayor


# Iniciar programa
if __name__ == '__main__':
  adivinar_numero()  # Llamar función