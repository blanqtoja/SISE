#odległość pomiędzy ciągami 10011101 i 10111001 wynosi 2.
from heapq import heappop, heappush
import itertools
import fieldSwitch as fs

from BoardNode import BoardNode
from stats import stat


def hamming(board):
    cnt = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if(i == len(board)-1 and j == len(board[i])-1):
                break
            if board[i][j] != i*len(board) + j + 1:
                cnt += 1

    return cnt

def manhattan(board):
    cnt = 0

    #potrzebujemy x y danego pola -> i,j
    #potrzebujemy x y gdzie powinno byc dane pole 
    for i in range(len(board)):
        for j in range(len(board[i])):
            x = board[i][j] // len(board) -1 # gdzie powinno byc dane pole
            y = board[i][j] % len(board) -1
            cnt += abs(x-i) + abs(y-j)
    
    return cnt

#koszt = heurystyka + ilosc ruchow od startu
def cost(node, heurystyka):
    return heurystyka(node.getBoard()) + node.getLevel()


# podejmowanie decyzji o rozwoju węzła w algorytmie a*
def aStar(startNode, k, dirPermutation, maxLevel, stats, heurystyka):
        
    stats.setMaxLevel(0)

    counter = itertools.count()  # licznik dla każdego węzła (eliminuje przypadek gdy dwa węzły mają taki sam priorytet)

    #tworzymy kopiec priorytetowy
    heapq = []

    #dodajemy wezel startowy do kopca -> (koszt, wezel)
    #koszt = heurystyka + ilosc ruchow od startu
    heappush(heapq, (cost(startNode, heurystyka), next(counter), startNode))


    #set do przechowywania odwiedzonych plansz (nie wezlow, bo one moga sie różnić kierunkiem)
    visited = set()


    while(heapq): #dopoki w kolejce sa wezly
        _, _, currentNode = heappop(heapq) #pobieramy wezel z kolejki
        visited.add(tuple(map(tuple, currentNode.getBoard()))) #dodajemy plansze jako krotkę do zbioru odwiedzonych
        #krotka, bo lista nie jest hashowalna, a krotka jest

        #sprawdzamy czy nie przekroczylismy maksymalnej glebokosci
        # print(currentNode.getLevel())
        if(currentNode.getLevel() > stats.getMaxLevel()):
            stats.setMaxLevel(currentNode.getLevel())


        #sprawdzamyczy to jest rozwiazanie
        if currentNode.isSolution():
            stats.setVisited(len(visited))
            stats.setProcessed(len(visited))
            return currentNode.getStringPath()
        

        if(currentNode.getLevel() == maxLevel):
            stats.setVisited(len(visited))
            stats.setProcessed(len(visited))
            return None
        
        #dla kazdego ruchu tworzymy nowy wezel
        for direction in dirPermutation:
            
            #eliminujemy nadmiarowe ruchy

            # nie wracamy do poprzedniego stanu
            if(currentNode.getDirection() == "L" and direction == "R"):
                continue
            if(currentNode.getDirection() == "R" and direction == "L"):
                continue
            if(currentNode.getDirection() == "U" and direction == "D"):
                continue
            if(currentNode.getDirection() == "D" and direction == "U"):
                continue
            
            # jesli puste pole jest na skraju to nie mozemy go przesunac w tym kierunku
            
            row, col = fs.findZeroField(currentNode.getBoard()) 
            
            #sprawdzamy czy puste pole jest na skraju i czy chcemy je przesunac w tym kierunku
            if(row == 0 and direction == "U"):
                continue
            if(row == (len(currentNode.getBoard())-1 ) and direction == "D"):
                continue
            if(col == 0 and direction == "L"):
                continue
            if(col == k-1 and direction == "R"):
                continue
    
            newNode = currentNode.addNode(direction, k)
            if(tuple(map(tuple, newNode.getBoard())) not in visited): # jesli plansza nie byla odwiedzona to dodajemy ja do kolejki
                heappush(heapq, (cost(newNode, heurystyka), next(counter), newNode))
                if newNode.isSolution():
                    stats.setVisited(len(visited))
                    stats.setProcessed(len(visited))
                    return newNode.getStringPath()

    stats.setVisited(len(visited))
    stats.setProcessed(len(visited))

    return None # nie znaleziono rozwiazania





# fileOrginal = open("data.txt", "r")
# data = fileOrginal.read().split("\n")

# #dwie pierwsze liczby to rozmiar planszy
# w, k = map(int, data[0].split())

# # tworzymy planszę ze stanem początkowym
# board = []
# for i in range(1, w+1): #liczby mamy podane dopiero w drugim wierszu 
#     board.append(list(map(int, data[i].split()))) # do kazdego wiersza dopisujemy listę liczb wczytanych z pliku - i-ty wierszy zawiera i-ty wiersz z pliku

# # zamykamy plik
# fileOrginal.close()

# print(board)

# # 
# # tworzymy węzeł początkowy
# startNode = BoardNode(board, None, "")

# dirPermutation = ["U", "D", "L", "R"]
# maxLevel = 30
# bfsStats = stat()

# path = aStar(startNode, k, dirPermutation, maxLevel, bfsStats, hamming)
# print(path)

# path = aStar(startNode, k, dirPermutation, maxLevel, bfsStats, manhattan)
# print(path)