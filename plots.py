import os
import re

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Jeśli nie ma folderu puzzle_solved, zakończ program
if not os.path.exists("puzzle_solved"):
    print("Brak folderu puzzle_solved")
    exit()

# Pobranie ścieżek plików z folderu puzzle
puzzleFiles = os.listdir("puzzle_solved")

# Posortowanie plików według strategii (po tytule)
bfs_files = []
dfs_files = []
astr_files = []

for file in puzzleFiles:
    if re.search(r"bfs_[a-zA-Z]{4}_stats", file): 
        bfs_files.append(file)
    elif re.search(r"dfs_[a-zA-Z]{4}_stats", file):
        dfs_files.append(file)
    elif re.search(r"astar_[a-zA-Z]{4}_stats", file):
        astr_files.append(file)

# Podział na listy ze względu na głębokość rozwiązania oraz permutacje/heurystyki
bfs_files_lvl_perm = {i: {perm: [] for perm in ["drlu", "drul", "ludr", "lurd", "rdul", "rdlu", "ulrd", "uldr"]} for i in range(1, 8)}
dfs_files_lvl_perm = {i: {perm: [] for perm in ["drlu", "drul", "ludr", "lurd", "rdul", "rdlu", "ulrd", "uldr"]} for i in range(1, 8)}
astr_files_lvl_perm = {i: {heur: [] for heur in ["manh", "hamm"]} for i in range(1, 8)}

# Podział plików na głębokości i permutacje / heurystyki
for file in bfs_files:
    for i in range(1, 8):
        if re.search(rf"_0{i}_", file):
            for perm in bfs_files_lvl_perm[i].keys():
                if perm in file:
                    bfs_files_lvl_perm[i][perm].append(file)

for file in dfs_files:
    for i in range(1, 8):
        if re.search(rf"_0{i}_", file):
            for perm in dfs_files_lvl_perm[i].keys():
                if perm in file:
                    dfs_files_lvl_perm[i][perm].append(file)

for file in astr_files:
    for i in range(1, 8):
        if re.search(rf"_0{i}_", file):
            for heur in astr_files_lvl_perm[i].keys():
                if heur in file:
                    astr_files_lvl_perm[i][heur].append(file)




# Podział na listy ze względu na głębokość rozwiązania
bfs_files_lvl = {i: [] for i in range(1, 8)}
dfs_files_lvl = {i: [] for i in range(1, 8)}
astr_files_lvl = {i: [] for i in range(1, 8)}

# Podział plików na głębokości
for file in bfs_files:
    for i in range(1, 8):
        if re.search(rf"_0{i}_", file):
            bfs_files_lvl[i].append(file)

for file in dfs_files:
    for i in range(1, 8):
        if re.search(rf"_0{i}_", file):
            dfs_files_lvl[i].append(file)

for file in astr_files:
    for i in range(1, 8):
        if re.search(rf"_0{i}_", file):
            astr_files_lvl[i].append(file)

            

# Funkcja do obliczania średniej wartości z określonej linii pliku
def calculate_avg_value(files_list, line_number):
    avg_values = {}
    for key, files in files_list.items():
        total_sum = 0.0
        count = 0
        for file in files:
            with open(f"puzzle_solved/{file}", "r") as f:
                lines = f.readlines()
                if len(lines) > line_number:
                    value = lines[line_number].strip()
                    if value != "-1":
                        total_sum += float(value)
                        count += 1
        avg_value = total_sum / count if count > 0 else -1
        avg_values[key] = avg_value
    return avg_values



# Obliczanie średniej długości rozwiązania (1 linia w pliku)

# Obliczanie średniej długości rozwiązania
all_avg_len_bfs = calculate_avg_value(bfs_files_lvl, 0)
all_avg_len_dfs = calculate_avg_value(dfs_files_lvl, 0)
all_avg_len_astr = calculate_avg_value(astr_files_lvl, 0)


avg_len_bfs = {i: calculate_avg_value(bfs_files_lvl_perm[i], 0) for i in range(1, 8)}
avg_len_dfs = {i: calculate_avg_value(dfs_files_lvl_perm[i], 0) for i in range(1, 8)}
avg_len_astr = {i: calculate_avg_value(astr_files_lvl_perm[i], 0) for i in range(1, 8)}



# Obliczanie średniej liczby odwiedzonych stanów
all_avg_states_bfs = calculate_avg_value(bfs_files_lvl, 1)
all_avg_states_dfs = calculate_avg_value(dfs_files_lvl, 1)
all_avg_states_astr = calculate_avg_value(astr_files_lvl, 1)
# Obliczanie średniej liczby odwiedzonych stanów (2 linia w pliku)
avg_states_bfs = {i: calculate_avg_value(bfs_files_lvl_perm[i], 1) for i in range(1, 8)}
avg_states_dfs = {i: calculate_avg_value(dfs_files_lvl_perm[i], 1) for i in range(1, 8)}
avg_states_astr = {i: calculate_avg_value(astr_files_lvl_perm[i], 1) for i in range(1, 8)}




# Obliczanie średniej  liczba stanów przetworzonych (3 linia w pliku)
all_avg_proc_bfs = calculate_avg_value(bfs_files_lvl, 2)
all_avg_proc_dfs = calculate_avg_value(dfs_files_lvl, 2)
all_avg_proc_astr = calculate_avg_value(astr_files_lvl, 2)


avg_proc_bfs  = {i: calculate_avg_value(bfs_files_lvl_perm[i], 2) for i in range(1, 8)}
avg_proc_dfs  = {i: calculate_avg_value(dfs_files_lvl_perm[i], 2) for i in range(1, 8)}
avg_proc_astr = {i: calculate_avg_value(astr_files_lvl_perm[i], 2) for i in range(1, 8)}



# Obliczanie średniej   maksymalna osiągnięta głębokość rekursj (4 linia w pliku)
all_avg_max_depth_bfs  = calculate_avg_value(bfs_files_lvl, 3)
all_avg_max_depth_dfs  = calculate_avg_value(dfs_files_lvl, 3)
all_avg_max_depth_astr = calculate_avg_value(astr_files_lvl, 3)


avg_max_depth_bfs  = {i: calculate_avg_value(bfs_files_lvl_perm[i], 3) for i in range(1, 8)}
avg_max_depth_dfs  = {i: calculate_avg_value(dfs_files_lvl_perm[i], 3) for i in range(1, 8)}
avg_max_depth_astr = {i: calculate_avg_value(astr_files_lvl_perm[i], 3) for i in range(1, 8)}



# Obliczanie średniej  zas trwania procesu obliczeniowego (5 linia w pliku)
all_avg_time_bfs  = calculate_avg_value(bfs_files_lvl, 4)
all_avg_time_dfs  = calculate_avg_value(dfs_files_lvl, 4)
all_avg_time_astr = calculate_avg_value(astr_files_lvl, 4)


avg_time_bfs  = {i: calculate_avg_value(bfs_files_lvl_perm[i], 4) for i in range(1, 8)}
avg_time_dfs  = {i: calculate_avg_value(dfs_files_lvl_perm[i], 4) for i in range(1, 8)}
avg_time_astr = {i: calculate_avg_value(astr_files_lvl_perm[i], 4) for i in range(1, 8)}



# Wyświetlanie wyników
print("Średnia długość rozwiązania:")
for depth in range(1, 8):
    print(f"Głębokość {depth}:")
    print(f"  BFS: {all_avg_len_bfs[depth]}")
    print(f"  DFS: {all_avg_len_dfs[depth]}")
    print(f"  A*: {all_avg_len_astr[depth]}")


# Wyświetlanie wyników
print("Średnia długość rozwiązania dla BFS:")
for depth, perm_lengths in avg_len_bfs.items():
    print(f"Głębokość {depth}:")
    for perm, avg_length in perm_lengths.items():
        print(f"  Permutacja {perm}: {avg_length}")

print("\nŚrednia długość rozwiązania dla DFS:")
for depth, perm_lengths in avg_len_dfs.items():
    print(f"Głębokość {depth}:")
    for perm, avg_length in perm_lengths.items():
        print(f"  Permutacja {perm}: {avg_length}")

print("\nŚrednia długość rozwiązania dla A*:")
for depth, heur_lengths in avg_len_astr.items():
    print(f"Głębokość {depth}:")
    for heur, avg_length in heur_lengths.items():
        print(f"  Heurystyka {heur}: {avg_length}")





print("\nŚrednia liczba odwiedzonych stanów:")
for depth in range(1, 8):
    print(f"Głębokość {depth}:")
    print(f"  BFS: {all_avg_states_bfs[depth]}")
    print(f"  DFS: {all_avg_states_dfs[depth]}")
    print(f"  A*: {all_avg_states_astr[depth]}")

print("\nŚrednia liczba odwiedzonych stanów dla BFS:")
for depth, perm_states in avg_states_bfs.items():
    print(f"Głębokość {depth}:")
    for perm, avg_states in perm_states.items():
        print(f"  Permutacja {perm}: {avg_states}")

print("\nŚrednia liczba odwiedzonych stanów dla DFS:")
for depth, perm_states in avg_states_dfs.items():
    print(f"Głębokość {depth}:")
    for perm, avg_states in perm_states.items():
        print(f"  Permutacja {perm}: {avg_states}")

print("\nŚrednia liczba odwiedzonych stanów dla A*:")
for depth, heur_states in avg_states_astr.items():
    print(f"Głębokość {depth}:")
    for heur, avg_states in heur_states.items():
        print(f"  Heurystyka {heur}: {avg_states}")



print("\nŚrednia liczba przetworzonych stanów:")
for depth in range(1, 8):
    print(f"Głębokość {depth}:")
    print(f"  BFS: {all_avg_proc_bfs[depth]}")
    print(f"  DFS: {all_avg_proc_dfs[depth]}")
    print(f"  A*: {all_avg_proc_astr[depth]}")

print("\nŚrednia liczba przetworzonych stanów dla BFS:")
for depth, perm_states in avg_proc_bfs.items():
    print(f"Głębokość {depth}:")
    for perm, avg_proc in perm_states.items():
        print(f"  Permutacja {perm}: {avg_proc}")

print("\nŚrednia liczba przetworzonych stanów dla DFS:")
for depth, perm_states in avg_proc_dfs.items():
    print(f"Głębokość {depth}:")
    for perm, avg_proc in perm_states.items():
        print(f"  Permutacja {perm}: {avg_proc}")

print("\nŚrednia liczba przetworzonych stanów dla A*:")
for depth, heur_states in avg_proc_astr.items():
    print(f"Głębokość {depth}:")
    for heur, avg_proc in heur_states.items():
        print(f"  Heurystyka {heur}: {avg_proc}")




print("\nŚrednia głębokosc rekursji:")
for depth in range(1, 8):
    print(f"Głębokość {depth}:")
    print(f"  BFS: {all_avg_max_depth_bfs[depth]}")
    print(f"  DFS: {all_avg_max_depth_dfs[depth]}")
    print(f"  A*: {all_avg_max_depth_astr[depth]}")

print("\nŚrednia głębokosc rekursji dla BFS:")
for depth, perm_states in avg_max_depth_bfs.items():
    print(f"Głębokość {depth}:")
    for perm, avg_max_depth in perm_states.items():
        print(f"  Permutacja {perm}: {avg_max_depth}")

print("\nŚrednia głębokosc rekursji dla DFS:")
for depth, perm_states in avg_max_depth_dfs.items():
    print(f"Głębokość {depth}:")
    for perm, avg_max_depth in perm_states.items():
        print(f"  Permutacja {perm}: {avg_max_depth}")

print("\nŚrednia głębokosc rekursji dla A*:")
for depth, heur_states in avg_max_depth_astr.items():
    print(f"Głębokość {depth}:")
    for heur, avg_max_depth in heur_states.items():
        print(f"  Heurystyka {heur}: {avg_max_depth}")




print("\nŚrednia głębokosc rekursji:")
for depth in range(1, 8):
    print(f"Głębokość {depth}:")
    print(f"  BFS: {all_avg_max_depth_bfs[depth]}")
    print(f"  DFS: {all_avg_max_depth_dfs[depth]}")
    print(f"  A*: {all_avg_max_depth_astr[depth]}")

print("\nŚrednia liczba przetworzonych stanów dla BFS:")
for depth, perm_states in avg_max_depth_bfs.items():
    print(f"Głębokość {depth}:")
    for perm, avg_max_depth in perm_states.items():
        print(f"  Permutacja {perm}: {avg_max_depth}")

print("\nŚrednia liczba przetworzonych stanów dla DFS:")
for depth, perm_states in avg_max_depth_dfs.items():
    print(f"Głębokość {depth}:")
    for perm, avg_max_depth in perm_states.items():
        print(f"  Permutacja {perm}: {avg_max_depth}")

print("\nŚrednia liczba przetworzonych stanów dla A*:")
for depth, heur_states in avg_max_depth_astr.items():
    print(f"Głębokość {depth}:")
    for heur, avg_max_depth in heur_states.items():
        print(f"  Heurystyka {heur}: {avg_max_depth}")




print("\nŚredni czas przetwarzania:")
for depth in range(1, 8):
    print(f"Głębokość {depth}:")
    print(f"  BFS: {all_avg_time_bfs[depth]}")
    print(f"  DFS: {all_avg_time_dfs[depth]}")
    print(f"  A*: {all_avg_time_astr[depth]}")

print("\nŚredni czas przetwarzania dla BFS:")
for depth, perm_states in avg_time_bfs.items():
    print(f"Głębokość {depth}:")
    for perm, avg_time in perm_states.items():
        print(f"  Permutacja {perm}: {avg_time}")

print("\nŚredni czas przetwarzania dla DFS:")
for depth, perm_states in avg_time_dfs.items():
    print(f"Głębokość {depth}:")
    for perm, avg_time in perm_states.items():
        print(f"  Permutacja {perm}: {avg_time}")

print("\nŚredni czas przetwarzania dla A*:")
for depth, heur_states in avg_time_astr.items():
    print(f"Głębokość {depth}:")
    for heur, avg_time in heur_states.items():
        print(f"  Heurystyka {heur}: {avg_time}")






#pierwszy
x_labels = np.array([1, 2, 3, 4, 5, 6, 7])

# Nazwy grup
# group_names = [1, 2, 3, 4, 5, 6, 7]

# # Zakładam, że klucze w słownikach to numery odpowiadające głębokości rozwiązania
# depth_levels = [1, 2, 3, 4, 5, 6, 7]  # Głębokości, które występują w danych

# df = pd.DataFrame({
#     "Kategoria": np.repeat(x_labels, 3),  # Powtarzamy etykiety dla BFS, DFS, A*
#     "Wartość": [all_avg_time_bfs[depth] for depth in depth_levels] +
#                [all_avg_time_dfs[depth] for depth in depth_levels] +
#                [all_avg_time_astr[depth] for depth in depth_levels],
#     "Grupa": np.tile(["BFS", "DFS", "A*"], len(depth_levels))  # Powtarzamy nazwy grup
# })



# Zakładam, że klucze w słownikach to numery odpowiadające głębokości rozwiązania
depth_levels = [1, 2, 3, 4, 5, 6, 7]  # Głębokości, które występują w danych

# Listy wartości i grup w odpowiedniej kolejności
values = []
groups = []
categories = []

for depth in depth_levels:
    values.extend([all_avg_len_bfs[depth], all_avg_len_dfs[depth], all_avg_len_astr[depth]])
    groups.extend(["BFS", "DFS", "A*"])
    categories.extend([depth] * 3)  # Powielamy głębokość 3 razy

# Tworzenie DataFrame
df = pd.DataFrame({
    "Kategoria": categories,  
    "Wartość": values,
    "Grupa": groups  
})



# Wykres
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="Kategoria", y="Wartość", hue="Grupa", dodge=True)

# Opisy
plt.title("Średnia długość rozwiązania")
plt.xlabel("Kategoria")
plt.ylabel("Wartość")
plt.legend(title="Grupa")

plt.show()








# Tworzenie DataFrame w formacie długim
data = []
for depth, moves in avg_len_bfs.items():
    for move, value in moves.items():
        data.append([depth, value, move])

df = pd.DataFrame(data, columns=["Głębokość", "Średnia długość rozwiązania", "Permutacja ruchów"])

# Wykres
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x="Głębokość", y="Średnia długość rozwiązania", hue="Permutacja ruchów", dodge=True)

# Opisy
plt.title("Średnia długość rozwiązania dla BFS")
plt.xlabel("Głębokość rozwiązania")
plt.ylabel("Średnia długość rozwiązania")
plt.legend(title="Permutacja ruchów")

# Pokazanie wykresu
plt.show()


# Tworzenie DataFrame w formacie długim
data = []
for depth, moves in avg_len_dfs.items():
    for move, value in moves.items():
        data.append([depth, value, move])

df = pd.DataFrame(data, columns=["Głębokość", "Średnia długość rozwiązania", "Permutacja ruchów"])

# Wykres
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x="Głębokość", y="Średnia długość rozwiązania", hue="Permutacja ruchów", dodge=True)

# Opisy
plt.title("Średnia długość rozwiązania dla DFS")
plt.xlabel("Głębokość rozwiązania")
plt.ylabel("Średnia długość rozwiązania")
plt.legend(title="Permutacja ruchów")

# Pokazanie wykresu
plt.show()