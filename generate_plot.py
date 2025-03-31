import numpy as np
import matplotlib.pyplot as plt

# Genruje wykres dla wszystkich strategii
# x - kategorie
# y - dane dla BFS
# z - dane dla DFS
# w - dane dla A*
# def getAllStraategies(x, y, z, w):
#     # Parametry wykresu
#     width = 0.2  # Szerokość słupków

#     # Tworzenie wykresu
#     fig, ax = plt.subplots()
#     ax.bar(x - width, y, width, label="BFS", color="blue")
#     ax.bar(x, z, width, label="DFS", color="orange")
#     ax.bar(x + width, w, width, label="A*", color="green")

#     # Opisy osi i tytuł
#     ax.set_xlabel("Kategorie")
#     ax.set_ylabel("Kryterium")
#     ax.set_title("Ogółem")

#     # Etykiety na osi X
#     ax.set_xticks(x)
#     ax.set_xticklabels(x)

#     # Legenda
#     ax.legend()

#     # Wyświetlenie wykresu
#     plt.show()



# Generuje wykres dla wszystkich strategii
# x - kategorie
# y - dane dla BFS
# z - dane dla DFS
# w - dane dla A*
def getAllStraategies(x, y, z, w):
    # Parametry wykresu
    width = 0.2  # Szerokość słupków

    # Tworzenie wykresu
    fig, ax = plt.subplots()
    # kazda kategoria ma 3 słupki -> BFS, DFS, A*
   
    for i in range (len(x)):
    

        ax[i].bar(x - width, y, width, label="BFS", color="blue")
        ax[i].bar(x, z, width, label="DFS", color="orange")
        ax[i].bar(x + width, w, width, label="A*", color="green")

    # Opisy osi i tytuł
    ax.set_xlabel("Kategorie")
    ax.set_ylabel("Kryterium")
    ax.set_title("Ogółem")

    # Etykiety na osi X
    ax.set_xticks(x)
    ax.set_xticklabels(x)

    # Legenda
    ax.legend()

    # Wyświetlenie wykresu
    plt.show()


# import numpy as np
# import matplotlib.pyplot as plt

# def plot_permutations(data, labels, x_labels, title="Wykres", xlabel="X", ylabel="Y"):
#     """
#     Tworzy wykres słupkowy dla różnych permutacji ruchów.

#     Parametry:
#     - data: słownik {nazwa_permutacji: lista_wartości}
#     - labels: lista nazw permutacji (np. ["RDUL", "RDLU", ...])
#     - x_labels: etykiety dla osi X (np. [1, 2, 3, ...])
#     - title: tytuł wykresu
#     - xlabel: etykieta osi X
#     - ylabel: etykieta osi Y
#     """
#     x = np.arange(len(x_labels))  # Pozycje kategorii
#     width = 0.1  # Szerokość słupków
#     colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray']  # Kolory dla permutacji

#     fig, ax = plt.subplots()

#     # Dodawanie słupków dla każdej permutacji
#     for i, label in enumerate(labels):
#         ax.bar(x + i * width - (width * len(labels) / 2), data[label], width, label=label, color=colors[i % len(colors)])

#     # Konfiguracja osi i legendy
#     ax.set_xlabel(xlabel)
#     ax.set_ylabel(ylabel)
#     ax.set_title(title)
#     ax.set_xticks(x)
#     ax.set_xticklabels(x_labels)
#     ax.legend()

#     plt.show()

# # 🔹 PRZYKŁAD UŻYCIA:
# labels = ["RDUL", "RDLU", "DRUL", "DRLU", "LUDR", "LURD", "ULDR", "ULRD"]
# data = {
#     "RDUL": [1, 2, 3, 4, 5, 6, 7],
#     "RDLU": [1, 2, 3, 4, 5, 6, 7],
#     "DRUL": [1, 2, 3, 4, 5, 6, 7],
#     "DRLU": [1, 2, 3, 4, 5, 6, 7],
#     "LUDR": [1, 2, 3, 4, 5, 6, 7],
#     "LURD": [1, 2, 3, 4, 5, 6, 7],
#     "ULDR": [1, 2, 3, 4, 5, 6, 7],
#     "ULRD": [1, 2, 3, 4, 5, 6, 7],
# }
# x_labels = [1, 2, 3, 4, 5, 6, 7]  # Głębokości

# plot_permutations(data, labels, x_labels, title="BFS", xlabel="Głębokość", ylabel="Kryterium")


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Dane
df = pd.DataFrame({
    "Kategoria": ["A", "B", "A", "B", "A", "B", "C", "C", "C"],
    "Grupa": ["BFS", "DFS", "A*"] * 3,
    "Wartość": [10, 15, 7, 12, 20, 13, 8, 14, 18]
})

# Wykres
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="Kategoria", y="Wartość", hue="Grupa", dodge=True)

# Opisy
plt.title("Grupowane słupki w Seaborn")
plt.xlabel("Kategoria")
plt.ylabel("Wartość")
plt.legend(title="Grupa")

# plt.show()