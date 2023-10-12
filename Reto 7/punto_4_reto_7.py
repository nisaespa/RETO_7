# Función para calcular crecimiento de poblaciones
def poblaciones_crecimiento():
  A = 25.0  # Definir variable, en este caso la población es de 25 millones
  B = 18.9  # Definir variable, en este caso la población es de 18.9 millones
  año = 2022  # Definir variable, desde la "actualidad" en este caso 2022
  while A > B:  #  Mientras que la población de A sea  mayor que la población de B
    C = (A * 2) / 100  # Crecimiento de la población de A en un 2%
    A = A + C  # Actualizar población de A + su crecimiento anual (2%)
    D = (B * 3) / 100  # Crecimiento de la población de B en un 3%
    B = B + D  # Actualizar población de B + su crecimiento anual (3%)
    año += 1  # Actualizar el año (2022 + 1)
  # Se termina el buble hasta que B sea mayor que A
  Z = round(A,2)  # Para que la población de A, solo tenga sus dos primeros decimales
  X = round(B,2)  # Para que la población de B, solo tenga sus dos primeros decimales
  print("En el año", año, "la población de B es:", X,
        " millones, que supera a la población de A que es de:", Z, "millones.")
  # Se imprime el año en el que la población de B es mayor que la de A, además de la impresión de Z y X, con redondeo en decimales hasta 2.


# Iniciar programa
if __name__ == '__main__':
  poblaciones_crecimiento()  # Llamar programa