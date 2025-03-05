# plik z danymi wygląda tak:
#est to plik tekstowy, w którym liczba linii zależy od rozmiaru ramki. 
# Pierwsza linia zawiera dwie liczby całkowite w oraz k, 
# oddzielone od siebie spacją, które określają odpowiednio pionowy (liczbę wierszy) i poziomy (liczbę kolumn) rozmiar ramki. 
# Każda z pozostałych w linii zawiera k oddzielonych spacjami liczb całkowitych,
#  które opisują położenie poszczególnych elementów układanki, przy czym wartość 0 oznacza wolne pole.

# zaczynamy od wczytania danych z pliku

# wczytujemy dane z pliku
from BoardNode import BoardNode
from bfs import bfs
import convertMatrix


file = open("data.txt", "r")
data = file.read().split("\n")

#dwie pierwsze liczby to rozmiar planszy
w, k = map(int, data[0].split())

# tworzymy planszę ze stanem początkowym
board = []
for i in range(1, w+1): #liczby mamy podane dopiero w drugim wierszu 
    board.append(list(map(int, data[i].split()))) # do kazdego wiersza dopisujemy listę liczb wczytanych z pliku - i-ty wierszy zawiera i-ty wiersz z pliku

print(board)
# 
# tworzymy węzeł początkowy
startNode = BoardNode(board, None, "")

# zmienne pomocnicze
dirPermutation = ["L", "R", "U", "D"] # permutacja kierunków
maxLevel = 20 # maksymalna glebokosc drzewa

# uruchamiamy algorytm
path = bfs(startNode, noLevels, maxLevel)

# wypisujemy wynik
if path is None:
    print("Brak rozwiązania")
else:
    print(path)

