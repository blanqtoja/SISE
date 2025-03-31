# długość znalezionego rozwiązania

# 1. średnie arytmetyczne wyznaczone dla strategii BFS (dla wszystkich porządków przeszukiwania łącznie), DFS (dla wszystkich porządków przeszukiwania łącznie) oraz A* (dla obu heurystyk łącznie) względem głębokości rozwiązania;

#zrób wykres słupkowy z wynikami z punktu 1
import matplotlib.pyplot as plt
import numpy as np
import os
import re 
import generate_plot as gp
import pandas as pd
import numpy as np
import seaborn as sns

#jesli nie ma folderu puzzle_solved to przerwij program
if not os.path.exists("puzzle_solved"):
    print("Brak folderu puzzle_solved")
    exit()

#podbranie sciezek plikow z folderu puzzle
puzzleFiles = os.listdir("puzzle_solved")

# posortownaie plików wedlug strategii (po tytule)
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

# podzial na listy ze wzgledu na glebokosc rozwiazania
bfs_files_lvl = [[], [], [], [], [], [], []]
dfs_files_lvl = [[], [], [], [], [], [], []]
astr_files_lvl = [[], [], [], [], [], [], []]

# kazdy ppoziom ma byc podzielony na osobne permutacje ruchow
bfs_files_lvl_perm = [[], [], [], [], [], [], [], []] # 8 perm
dfs_files_lvl_perm = [[], [], [], [], [], [], [], []] # 8 perm
astr_files_lvl_perm = [[], []] # 2 perm


for file in bfs_files:
    if re.search(r"_01_", file):
        bfs_files_lvl[0].append(file)
    elif re.search(r"_02_", file):
        bfs_files_lvl[1].append(file)
    elif re.search(r"_03_", file):
        bfs_files_lvl[2].append(file)
    elif re.search(r"_04_", file):
        bfs_files_lvl[3].append(file)
    elif re.search(r"_05_", file):
        bfs_files_lvl[4].append(file)
    elif re.search(r"_06_", file):
        bfs_files_lvl[5].append(file)
    elif re.search(r"_07_", file):
        bfs_files_lvl[6].append(file)

for file in dfs_files:
    if re.search(r"_01_", file):
        dfs_files_lvl[0].append(file)
    elif re.search(r"_02_", file):
        dfs_files_lvl[1].append(file)
    elif re.search(r"_03_", file):
        dfs_files_lvl[2].append(file)
    elif re.search(r"_04_", file):
        dfs_files_lvl[3].append(file)
    elif re.search(r"_05_", file):
        dfs_files_lvl[4].append(file)
    elif re.search(r"_06_", file):
        dfs_files_lvl[5].append(file)
    elif re.search(r"_07_", file):
        dfs_files_lvl[6].append(file)

for file in astr_files:
    if re.search(r"_01_", file):
        astr_files_lvl[0].append(file)
    elif re.search(r"_02_", file):
        astr_files_lvl[1].append(file)
    elif re.search(r"_03_", file):
        astr_files_lvl[2].append(file)
    elif re.search(r"_04_", file):
        astr_files_lvl[3].append(file)
    elif re.search(r"_05_", file):
        astr_files_lvl[4].append(file)
    elif re.search(r"_06_", file):
        astr_files_lvl[5].append(file)
    elif re.search(r"_07_", file):
        astr_files_lvl[6].append(file)


# średnie arytmetyczne dlugosci znalezionego rozwiazania 

#z pliku wyciagamy pierwsza linie, doliczamy do sumy (tylko jeśli jest rozne od -1) i zliczamy ilosc plikow

avg_len = [] #tutaj przechowujemy srednie arytmetyczne dla kkazdej strategii

for filesList_lvl in [bfs_files_lvl, dfs_files_lvl, astr_files_lvl]:
    tmp = []
    for i in filesList_lvl:
    
        avg_len_per_level = 0
        sum = 0
        count = 0
        for file in i:
            with open(f"puzzle_solved/{file}", "r") as f:
                
                line = f.readline()
                # if(int(line) < 7 ): #sprawdzenie ktory plik ma bledna informacje
                #     print(file)

                if line != "-1":
                    sum += int(line)
                    count += 1
        if(count == 0):
            avg_len_per_level = -1
        else:
            avg_len_per_level = sum / count

        tmp.append(avg_len_per_level)
    avg_len.append(tmp)

print(avg_len)



# średnie arytmetyczne liczba stanów odwiedzonych

#z pliku wyciagamy druga linie, doliczamy do sumy i zliczamy ilosc plikow

avg_visited = [] #tutaj przechowujemy srednie arytmetyczne dla kkazdej strategii

for filesList_lvl in [bfs_files_lvl, dfs_files_lvl, astr_files_lvl]:
    tmp = []
    for i in filesList_lvl:
    
        avg_visited_per_level = 0
        sum = 0
        count = 0
        for file in i:
            with open(f"puzzle_solved/{file}", "r") as f:
                line = f.readline() # pomijamy pierwsza linie
                line = f.readline()
                # if(int(line) < 7 ): #sprawdzenie ktory plik ma bledna informacje
                #     print(file)

                if line != "-1":
                    sum += int(line)
                    count += 1
        if(count == 0):
            avg_visited_per_level = -1
        else:
            avg_visited_per_level = sum / count 

        tmp.append(avg_visited_per_level)
    avg_visited.append(tmp)

print(avg_visited)



# średnie arytmetyczne liczba stanów przetworzonych

#z pliku wyciagamy trzecia linie, doliczamy do sumy i zliczamy ilosc plikow

avg_processed = [] #tutaj przechowujemy srednie arytmetyczne dla kkazdej strategii

for filesList_lvl in [bfs_files_lvl, dfs_files_lvl, astr_files_lvl]:
    tmp = []
    for i in filesList_lvl:
    
        avg_processed_per_level = []
        sum = 0
        count = 0
        for file in i:
            with open(f"puzzle_solved/{file}", "r") as f:
                line = f.readline() # pomijamy pierwsza linie
                line = f.readline() # pomijamy pierwsza linie
                line = f.readline()
                # if(int(line) < 7 ): #sprawdzenie ktory plik ma bledna informacje
                #     print(file)

                if line != "-1":
                    sum += int(line)
                    count += 1
        if(count == 0):
            avg_processed_per_level = -1
        else:
            avg_processed_per_level = sum / count 

        tmp.append(avg_processed)
    avg_processed.append(tmp)

print(avg_processed)




# średnie arytmetyczne maksymalna osiągnięta głębokość rekursji 

#z pliku wyciagamy trzecia linie, doliczamy do sumy i zliczamy ilosc plikow

avg_max_depth = [] #tutaj przechowujemy srednie arytmetyczne dla kkazdej strategii

for filesList_lvl in [bfs_files_lvl, dfs_files_lvl, astr_files_lvl]:
    tmp = []
    for i in filesList_lvl:
    
        avg_max_depth_per_level = []
        sum = 0
        count = 0
        for file in i:
            with open(f"puzzle_solved/{file}", "r") as f:
                line = f.readline() # pomijamy pierwsza linie
                line = f.readline() # pomijamy pierwsza linie
                line = f.readline() # pomijamy pierwsza linie
                line = f.readline()
                # if(int(line) < 7 ): #sprawdzenie ktory plik ma bledna informacje
                #     print(file)

                if line != "-1":
                    sum += int(line)
                    count += 1
        if(count == 0):
            avg_max_depth_per_level = -1
        else:
            avg_max_depth_per_level = sum / count

        tmp.append(avg_max_depth_per_level)
    avg_max_depth.append(tmp)

print(avg_max_depth)




# średnie arytmetyczne czas trwania procesu obliczeniowego

#z pliku wyciagamy trzecia linie, doliczamy do sumy i zliczamy ilosc plikow

avg_time = [] #tutaj przechowujemy srednie arytmetyczne dla kkazdej strategii

for filesList_lvl in [bfs_files_lvl, dfs_files_lvl, astr_files_lvl]:
    tmp = []
    for i in filesList_lvl:
    
        avg_time_per_level = 0
        sum = 0
        count = 0
        for file in i:
            with open(f"puzzle_solved/{file}", "r") as f:
                line = f.readline() # pomijamy pierwsza linie
                line = f.readline() # pomijamy pierwsza linie
                line = f.readline() # pomijamy pierwsza linie
                line = f.readline()
                # if(int(line) < 7 ): #sprawdzenie ktory plik ma bledna informacje
                #     print(file)

                if line != "-1":
                    sum += int(line)
                    count += 1
        if(count == 0):
            avg_time_per_level = -1
        else:
            avg_time_per_level = sum / count

        tmp.append(avg_time_per_level)
    avg_time.append(tmp)

print(avg_time)


#DLA KAZDEGO KRYTERIUM WYKRESY

# pierwszy wykres zbiera wszystkie strategie WZGLEDEM głębokości rozwiązania
    #inne dzielimy wzgledem permutacji ruchow

    # drugi wykres zbiera bfs
    # trzeci wykres zbiera dfs
    # czwarty wykres zbiera astr

x_labels = np.array([1, 2, 3, 4, 5, 6, 7])

# Nazwy grup
group_names = ["BFS", "DFS", "A*"]

# Tworzenie DataFrame w formacie długim
df = pd.DataFrame({
    "Kategoria": np.tile(x_labels, len(avg_len)),  # Powielamy etykiety X dla każdej grupy
    "Wartość": np.concatenate(avg_len),  # Spłaszczamy listę podlist
    "Grupa": np.repeat(group_names, len(x_labels))  # Powtarzamy nazwy grup odpowiednią ilość razy
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




#drugi
print("BFS")
x_labels = np.array([1, 2, 3, 4, 5, 6, 7])

# Nazwy grup
group_names = [1, 2, 3, 4, 5, 6, 7]
print(len(avg_len[0]))
# Tworzenie DataFrame w formacie długim
df = pd.DataFrame({
    "Kategoria": x_labels,  # Powielamy etykiety X dla każdej grupy
    "Wartość": avg_len[0],  # Spłaszczamy listę podlist
    "Grupa": group_names  # Powtarzamy nazwy grup odpowiednią ilość razy
})

# Wykres
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="Kategoria", y="Wartość", hue="Grupa", dodge=True)

# Opisy
plt.title("Grupowane słupki w Seaborn")
plt.xlabel("Kategoria")
plt.ylabel("Wartość")
plt.legend(title="Grupa")

plt.show()