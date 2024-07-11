import matplotlib.pyplot as plt
import numpy as np

def test_matplotlib():
    # Générer des données pour une sinusoïde
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)

    # Créer une figure et un axe
    fig, ax = plt.subplots()

    # Tracer les données
    ax.plot(x, y, label='sin(x)')

    # Ajouter un titre et des labels aux axes
    ax.set_title('Test Matplotlib: Sinusoidal Wave')
    ax.set_xlabel('x')
    ax.set_ylabel('sin(x)')

    # Ajouter une légende
    ax.legend()

    # Afficher le graphique
    plt.show()

# Appeler la fonction pour tester matplotlib
test_matplotlib()

plt.ioff()
plt.ion()
plt.rcdefaults()

import matplotlib.pyplot as plt

def simple_plot():
    plt.plot([1, 2, 3, 4])
    plt.ylabel('some numbers')
    plt.show(block=True)  # Forcer le blocage jusqu'à ce que la fenêtre soit fermée

simple_plot()

    plt.draw()
    plt.pause(0.0001)
    plt.clf()