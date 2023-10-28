import numpy as np
import tkinter as tk

def solve_cramer(matrix_A, vector_b):
    n = len(vector_b)
    solutions = []

    det_A = np.linalg.det(matrix_A)

    for i in range(n):
        A_copy = np.copy(matrix_A)
        A_copy[:, i] = vector_b
        solutions.append(np.linalg.det(A_copy) / det_A)

    return solutions

def solve_equations():
    matrix_size = int(matrix_size_entry.get())
    matrix_A = np.zeros((matrix_size, matrix_size))
    vector_b = np.zeros(matrix_size)

    for i in range(matrix_size):
        for j in range(matrix_size):
            matrix_A[i, j] = float(matrix_entries[i][j].get())

    for i in range(matrix_size):
        vector_b[i] = float(vector_entries[i].get())

    solutions = solve_cramer(matrix_A, vector_b)

    result_label.config(text="Soluciones: " + " ".join([f"x{i+1} = {solutions[i]:.2f}" for i in range(matrix_size)]))

# Crear la ventana de la aplicación
app = tk.Tk()
app.title("Resolución de Ecuaciones por Cramer")

# Etiqueta para seleccionar el tamaño de la matriz
size_label = tk.Label(app, text="Tamaño de la matriz (2, 3 o 4):")
size_label.pack()

matrix_size_entry = tk.Entry(app)
matrix_size_entry.pack()

# Botón para confirmar el tamaño de la matriz
size_confirm_button = tk.Button(app, text="Confirmar Tamaño", command=solve_equations)
size_confirm_button.pack()

# Listas para las entradas de la matriz A y el vector b
matrix_entries = []
vector_entries = []

# Crear entradas para la matriz A
for i in range(4):
    matrix_entries.append([tk.Entry(app) for _ in range(4)])

for row in matrix_entries:
    for entry in row:
        entry.pack()

# Etiqueta para el vector b
vector_label = tk.Label(app, text="Vector b:")
vector_label.pack()

# Crear entradas para el vector b
for i in range(4):
    vector_entries.append(tk.Entry(app))
    vector_entries[i].pack()

# Etiqueta para mostrar las soluciones
result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
