# plik z danymi wygląda tak:
#est to plik tekstowy, w którym liczba linii zależy od rozmiaru ramki. 
# Pierwsza linia zawiera dwie liczby całkowite w oraz k, 
# oddzielone od siebie spacją, które określają odpowiednio pionowy (liczbę wierszy) i poziomy (liczbę kolumn) rozmiar ramki. 
# Każda z pozostałych w linii zawiera k oddzielonych spacjami liczb całkowitych,
#  które opisują położenie poszczególnych elementów układanki, przy czym wartość 0 oznacza wolne pole.

# zaczynamy od wczytania danych z pliku

# wczytujemy dane z pliku
from hamming import aStar, hamming, manhattan
from stats import stat
from BoardNode import BoardNode
from bfs import bfs
from dfs import dfs
import time
import sys

# wczytujemy dane z parametru wejściowego
# akronim określający wybraną strategię zgodnie z poniższą tabelą:
strategy = sys.argv[1]

# dodatkowy parametr wybranej strategii zgodnie z poniższą tabelą:
strategyParam = sys.argv[2]

#nazwa pliku tekstowego z zadanym układem początkowym układanki;
originalBoardFile = sys.argv[3]

#nazwa pliku tekstowego, w którym ma zostać zapisane rozwiązanie;
solvedBoardFile = sys.argv[4]

#nazwa pliku tekstowego, w którym mają zostać zapisane dodatkowe informacje dotyczące przeprowadzonego procesu obliczeniowego.
statsFile = sys.argv[5]


#otweiramy plik do odczytu
fileOrginal = open(originalBoardFile, "r")
data = fileOrginal.read().split("\n")

#dwie pierwsze liczby to rozmiar planszy
w, k = map(int, data[0].split())

# tworzymy planszę ze stanem początkowym
board = []
for i in range(1, w+1): #liczby mamy podane dopiero w drugim wierszu 
    board.append(list(map(int, data[i].split()))) # do kazdego wiersza dopisujemy listę liczb wczytanych z pliku - i-ty wierszy zawiera i-ty wiersz z pliku

# zamykamy plik
fileOrginal.close()

print(board)


# Wymagania funkcjonalne:
# długość znalezionego rozwiązania; X
# liczbę stanów odwiedzonych; X
# liczbę stanów przetworzonych; X
# maksymalną osiągniętą głębokość rekursji; X
# czas trwania procesu obliczeniowego. X


# 
# tworzymy węzeł początkowy
startNode = BoardNode(board, None, "")


# strategia BFS
if(strategy == "bfs" or strategy == "dfs"):
    # wspolne zmienne dla obu strategii
    maxLevel = 20 # maksymalna glebokosc drzewa
    dirPermutation = list(strategyParam) # permutacja kierunków

    #podzial na strategie
    if(strategy == "bfs"):
        bfsStats = stat()

        start = time.time()
        # uruchamiamy algorytm
        path = bfs(startNode, k, dirPermutation, maxLevel, bfsStats)

        # czas zakonczenia bfs
        end = time.time()
        bfsStats.setTime((end-start)*1000)
        bfsStats.setPath(path)

        # wypisujemy wynik
        if path is None:
            print("Brak rozwiązania")
            bfsStats.setLenFound("-1")

        else:
            print(path)
            bfsStats.setLenFound(len(path))


        print("BFS statistics:\n")
        print(bfsStats)

        
        # zapisujemy wyniki do pliku
        fileStats = open(statsFile, "w")
        # fileStats.write("BFS statistics:\n")
        fileStats.write(str(bfsStats))
        fileStats.close()

    else:               
        dfsStats = stat()

        # uruchamiamy algorytm
        start = time.time()

        path = dfs(startNode, k, dirPermutation, maxLevel, dfsStats)

        end = time.time()

        dfsStats = stat()

        dfsStats.setTime((end-start)*1000)
        dfsStats.setPath(path)


        # wypisujemy wynik
        if path is None:
            print("Brak rozwiązania")
            dfsStats.setLenFound("-1")

        else:
            print(path)
            dfsStats.setLenFound(len(path))

        # print("DFS statistics:\n")
        print(dfsStats)


        # zapisujemy wyniki do pliku
        fileStats = open(statsFile, "w")
        # fileStats.write("DFS statistics:\n")
        fileStats.write(str(dfsStats))
        fileStats.close()


elif (strategy == "astr"): # strategia A*
    print("A*")
    if(strategyParam == "hamm"):
        print("Hamming")

        hammStats = stat()

        # uruchamiamy algorytm
        start = time.time()

        dirPermutation = ["U", "D", "L", "R"]
        maxLevel = 200
        path = aStar(startNode, k, dirPermutation, maxLevel, hammStats, hamming)

        end = time.time()

        hammStats = stat()

        hammStats.setTime((end-start)*1000)
        hammStats.setPath(path)


        # wypisujemy wynik
        if path is None:
            print("Brak rozwiązania")
            hammStats.setLenFound("-1")
        else:
            print(path)
            hammStats.setLenFound(len(path))


        print("A* Hamming statistics:\n")
        print(hammStats)


        # zapisujemy wyniki do pliku
        fileStats = open(statsFile, "w")
        # fileStats.write("A* Hamming statistics:\n")
        fileStats.write(str(hammStats))
        fileStats.close()
        
    elif strategyParam=="manh":
        print("Manhattan")

        manhStats = stat()

        # uruchamiamy algorytm
        start = time.time()

        dirPermutation = ["U", "D", "L", "R"]
        maxLevel = 200
        path = aStar(startNode, k, dirPermutation, maxLevel, manhStats, manhattan)

        end = time.time()

        manhStats = stat()

        manhStats.setTime((end-start)*1000)
        manhStats.setPath(path)


        # wypisujemy wynik
        if path is None:
            print("Brak rozwiązania")
            manhStats.setLenFound("-1")
        else:
            print(path)
            manhStats.setLenFound(len(path))

        print("A* Hamming statistics:\n")
        print(manhStats)


        # zapisujemy wyniki do pliku
        fileStats = open(statsFile, "w")
        # fileStats.write("A* Hamming statistics:\n")
        fileStats.write(str(manhStats))
        fileStats.close()
else:
    print("Nieznana strategia")

