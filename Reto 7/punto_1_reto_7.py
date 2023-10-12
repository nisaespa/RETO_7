# Función para imprimir los números del 1 al 100 con su respectivo cuadrado
def uno_al_cien_con_su_cuadrado():
  numero = 1  # Declarar variable, en este caso para que comience desde 1
  cuadrado = 0  # Declarar variable
  while numero <= 100:  # Mientras el número sea menor o igual a 100, entonces
    cuadrado = numero**2  # Guardar en la variable cuadrado, el cuadrado del número
    print(numero, cuadrado)  # Imprimir el numero, y al frente su cuadrado
    numero += 1  # Actualizar para que vaya avanzando hasta 100


# Iniciar programa
if __name__ == '__main__':
  uno_al_cien_con_su_cuadrado()  # Llamar función