# długość znalezionego rozwiązania

# 1. średnie arytmetyczne wyznaczone dla strategii BFS (dla wszystkich porządków przeszukiwania łącznie), DFS (dla wszystkich porządków przeszukiwania łącznie) oraz A* (dla obu heurystyk łącznie) względem głębokości rozwiązania;

#zrób wykres słupkowy z wynikami z punktu 1
import matplotlib.pyplot as plt
import numpy as np
import os

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
    
    if "bfs_stats" in file:
        bfs_files.append(file)
    elif "dfs_stats" in file:
        dfs_files.append(file)
    elif "astr_hamm_stats" or "astr_manh_stats" in file:
        astr_files.append(file)

# podzial na listy ze wzgledu na glebokosc rozwiazania
bfs_files_lvl = [[], [], [], [], [], [], []]
dfs_files_lvl = [[], [], [], [], [], [], []]
astr_files_lvl = [[], [], [], [], [], [], []]

for file in bfs_files:
    if "_01_" in file:
        bfs_files_lvl[0].append(file)
    elif "_02_" in file:
        bfs_files_lvl[1].append(file)
    elif "_03_" in file:
        bfs_files_lvl[2].append(file)
    elif "_04_" in file:
        bfs_files_lvl[3].append(file)
    elif "_05_" in file:
        bfs_files_lvl[4].append(file)
    elif "_06_" in file:
        bfs_files_lvl[5].append(file)
    elif "_07_" in file:
        bfs_files_lvl[6].append(file)

for file in dfs_files:
    if "_01_" in file:
        dfs_files_lvl[0].append(file)
    elif "_02_" in file:
        dfs_files_lvl[1].append(file)
    elif "_03_" in file:
        dfs_files_lvl[2].append(file)
    elif "_04_" in file:
        dfs_files_lvl[3].append(file)
    elif "_05_" in file:
        dfs_files_lvl[4].append(file)
    elif "_06_" in file:
        dfs_files_lvl[5].append(file)
    elif "_07_" in file:
        dfs_files_lvl[6].append(file)

for file in astr_files:
    if "_01_" in file:
        astr_files_lvl[0].append(file)
    elif "_02_" in file:
        astr_files_lvl[1].append(file)
    elif "_03_" in file:
        astr_files_lvl[2].append(file)
    elif "_04_" in file:
        astr_files_lvl[3].append(file)
    elif "_05_" in file:
        astr_files_lvl[4].append(file)
    elif "_06_" in file:
        astr_files_lvl[5].append(file)
    elif "_07_" in file:
        astr_files_lvl[6].append(file)


# średnie arytmetyczne dlugosci znalezionego rozwiazania dla strategii BFS dla wszystkich permutacji

#z pliku wyciagamy pierwsza linie, doliczamy do sumy (tylko jeśli jest rozne od -1) i zliczamy ilosc plikow

avg_len = [] #tutaj przechowujemy srednie arytmetyczne dla kkazdej strategii

for filesList_lvl in [bfs_files_lvl, dfs_files_lvl, astr_files_lvl]:
    for i in filesList_lvl:
    
        avg_len_per_level = []
        sum = 0
        count = 0
        for file in i:
            with open(f"puzzle_solved/{file}", "r") as f:
                line = f.readline()
                if(int(line) < 7 ): #sprawdzenie ktory plik ma bledna informacje
                    print(file)

                if line != "-1":
                    sum += int(line)
                    count += 1
        if(count == 0):
            avg_len_per_level.append(-1)
        else:
            avg_len_per_level.append( sum / count )

        avg_len.append(avg_len_per_level)

print(avg_len)