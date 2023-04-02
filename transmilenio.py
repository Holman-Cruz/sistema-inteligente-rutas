# Importación de librerías
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk

# Definición de variables de tipo array
# La variable hora, representa las horas del día en las que transmilenio presta servicio
hora = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
# La variable B11, es el promedio de tiempo del recorrido de el punto A al punto B ruta B11
B11 = [17,19,24,27,28,29,26,25,27,31,28,26,28,31,33,32,30,25,23,20]
# La variable B72, es el promedio de tiempo del recorrido de el punto A al punto B ruta B72
B72 = [20,18,28,23,22,27,25,25,24,31,30,25,27,32,35,30,28,27,25,22]


# Primera sección

# Calculo y creación de regresión lineal
poly_fit1 = np.polyfit(hora, B11, 1)
poly_fn1 = np.poly1d(poly_fit1)

poly_fit2 = np.polyfit(hora, B72, 1)
poly_fn2 = np.poly1d(poly_fit2)

# Creación de la gráfica
fig, ax = plt.subplots()
ax.scatter(hora, B11, c='blue', label='Ruta B11')
ax.scatter(hora, B72, c='red', label='Ruta B72')
ax.plot(hora, poly_fn1(hora), '-k', label='Ajuste lineal de B11')
ax.plot(hora, poly_fn2(hora), '-y', label='Ajuste lineal de B72')
ax.set_xlabel('Hora del día')
ax.set_ylabel('Tiempo en minutos')
ax.set_title('Tiempo de Recorrido de un Transmilenio del Punto A al B')
ax.legend(loc='upper left')
plt.show()


# Segunda sección

# Calculo de dispersión polinomial
poly_fit1 = np.polyfit(hora, B11, 3)
poly_fn1 = np.poly1d(poly_fit1)

# Creación de dispersión polinomial
poly_fit2 = np.polyfit(hora, B72, 3)
poly_fn2 = np.poly1d(poly_fit2)

# Creación de la gráfica
fig, ax = plt.subplots()
ax.scatter(hora, B11, c='blue', label='Ruta B11')
ax.scatter(hora, B72, c='red', label='Ruta B72')
ax.plot(hora, poly_fn1(hora), '-k', label='Ajuste polinomial de B11')
ax.plot(hora, poly_fn2(hora), '-y', label='Ajuste polinomial de B72')
ax.set_xlabel('Hora del día')
ax.set_ylabel('Tiempo en minutos')
ax.set_title('Tiempo de Recorrido de un Transmilenio del Punto A al B')
ax.legend(loc='upper left')
plt.show()


# Tercera sección

# Función para elegir la ruta
def mejor_ruta():
    input_hora = int(combo_hora.get())

    for i in range(len(hora)):
        if hora[i] == input_hora:
            if B11[i] < B72[i]:
                resultado_label.config(text="La ruta más rápida es la B11, el tiempo aproximado del reccorrido es de " + str(B11[i]) + " minutos.")
            else:
                resultado_label.config(text="La ruta más rápida es la B72, el tiempo aproximado del reccorrido es de " + str(B72[i]) + " minutos.")

# Creación de ventana emergente
root = Tk()
root.geometry("700x350")
root.title("Ruta más rápida entre los puntos A y B")

label_hora = Label(root, text="Selecciona la hora en la que te vas a transportar, puede ser entre las 4 y 23 horas:")
label_hora.pack(pady=30)

combo_hora = ttk.Combobox(root, values=hora)
combo_hora.pack(pady=20)
combo_hora.current(0)

# Botón para calcular la ruta
calcular_button = Button(root, text="Buscar la ruta más rápida", command=mejor_ruta)
calcular_button.pack(pady=20)

# Mensaje resultado
resultado_label = Label(root, text="")
resultado_label.pack(pady=10)

# Abrir la ventana
root.mainloop()