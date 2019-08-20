import matplotlib.pyplot as plt
import numpy as np

def plot_two_variables(a11, a21, a12, a22, a13, a23, b1, b2, b3, c1, c2):
    fig = plt.figure(figsize=(12, 6))

    x_1 = np.linspace(0, 45, 100)

    # Mano de Obra
    x_2 = b1/a21 - a11/a21 * x_1
    plt.plot(x_1, x_2, label="Mano de Obra")
    x_4 = x_2

    # Materia Prima
    x_2 = b2/a22 - a12/a22 * x_1
    plt.plot(x_1, x_2, label="Materia Prima")
    x_4 = np.minimum(x_4, x_2)

    # Demanda
    x_2 = b3/a23 + a13/a23 * x_1
    plt.plot(x_1, x_2, label="Demanda")
    x_4 = np.minimum(x_4, x_2)

    # Sombrear area de interés
    plt.fill_between(x_1, 0, x_4, color='grey', alpha=0.5)


    # Optimo
    z = c1 * x_1 + c2 * x_4
    z_x_2 = np.max(z)
    z_x_1 = np.argmax(z)
    
    plt.scatter(x_1[z_x_1], x_4[z_x_1], label="Óptimo", s=100, color="black")

    # Fijar ticks
    plt.xticks(np.arange(0, 46, 5))
    plt.yticks(np.arange(0, 51, 5))

    # Fijar Límites de X e Y
    plt.ylim(0, 50)
    plt.xlim(0, 45)

    plt.legend()
    plt.tight_layout()