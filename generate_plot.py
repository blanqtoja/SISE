# from matplotlib import pyplot as plt
# import seaborn as sns
# import pandas as pd
# import numpy as np

# def plot_all_strategies(all_bfs, all_dfs, all_astr, title, xlabel, ylabel, log=False):
#     # Zakładam, że klucze w słownikach to numery odpowiadające głębokości rozwiązania
#     depth_levels = [1, 2, 3, 4, 5, 6, 7]  # Głębokości, które występują w danych

#     # Listy wartości i grup w odpowiedniej kolejności
#     values = []
#     groups = []
#     categories = []

#     for depth in depth_levels:
#         values.extend([all_bfs[depth], all_dfs[depth], all_astr[depth]])
#         groups.extend(["BFS", "DFS", "A*"])
#         categories.extend([depth] * 3)  # Powielamy głębokość 3 razy

#     # Tworzenie DataFrame
#     df = pd.DataFrame({
#         "Kategoria": categories,  
#         "Wartość": values,
#         "Grupa": groups  
#     })



#     # Wykres
#     plt.figure(figsize=(8, 5))
#     sns.barplot(data=df, x="Kategoria", y="Wartość", hue="Grupa", dodge=True)

#     if(log):
#         plt.yscale('log')
        
#     # Opisy
#     plt.title(title)
#     plt.xlabel(xlabel)
#     plt.ylabel(ylabel)
#     plt.legend(title="Strategia")

#     plt.show()





# def plot_permutations(arr, title, xlabel, ylabel):
    
#     # Tworzenie DataFrame w formacie długim
#     data = []
#     for depth, moves in arr.items():
#         for move, value in moves.items():
#             data.append([depth, value, move])

#     df = pd.DataFrame(data, columns=["Głębokość", "Średnia długość rozwiązania", "Permutacja ruchów"])

#     # Wykres
#     plt.figure(figsize=(10, 6))
#     sns.barplot(data=df, x="Głębokość", y="Średnia długość rozwiązania", hue="Permutacja ruchów", dodge=True)

#     # Opisy
#     plt.title(title)
#     plt.xlabel(xlabel)
#     plt.ylabel(ylabel)
#     plt.legend(title="Permutacja ruchów")

#     # Pokazanie wykresu
#     plt.show()

from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

def plot_all_strategies(all_bfs, all_dfs, all_astr, title, xlabel, ylabel, log=False, ax=None):
    depth_levels = [1, 2, 3, 4, 5, 6, 7]

    values = []
    groups = []
    categories = []

    for depth in depth_levels:
        values.extend([all_bfs[depth], all_dfs[depth], all_astr[depth]])
        groups.extend(["BFS", "DFS", "A*"])
        categories.extend([depth] * 3)

    df = pd.DataFrame({
        "Kategoria": categories,
        "Wartość": values,
        "Grupa": groups
    })

    if ax is None:
        ax = plt.gca()

    sns.barplot(data=df, x="Kategoria", y="Wartość", hue="Grupa", dodge=True, ax=ax)

    if log:
        ax.set_yscale('log')

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend(title="Strategia")


def plot_permutations(arr, title, xlabel, ylabel, ax=None):
    data = []
    for depth, moves in arr.items():
        for move, value in moves.items():
            data.append([depth, value, move])

    df = pd.DataFrame(data, columns=["Głębokość", "Średnia długość rozwiązania", "Permutacja ruchów"])

    if ax is None:
        ax = plt.gca()

    sns.barplot(data=df, x="Głębokość", y="Średnia długość rozwiązania", hue="Permutacja ruchów", dodge=True, ax=ax)

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend(title="Permutacja ruchów")


