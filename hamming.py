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
            if board[i][j] == 0: # nie sprawdzamy zera
                continue
            # if(i == len(board)-1 and j == len(board[i])-1):
            #     break
            if board[i][j] != i*len(board) + j + 1:
                cnt += 1

    return cnt

def manhattan(board):
    cnt = 0

    #potrzebujemy x y danego pola -> i,j
    #potrzebujemy x y gdzie powinno byc dane pole 
    for i in range(len(board)):
        for j in range(len(board[i])):
            val = board[i][j]
            if val == 0: # nie sprawdzamy zera
                continue
            x = (val-1) // len(board)  # gdzie powinno byc dane pole
            y = (val-1) % len(board)
            cnt += abs(x-i) + abs(y-j)
    
    return cnt

#koszt = heurystyka + ilosc ruchow od startu
def cost(node, heurystyka):
    return heurystyka(node.getBoard()) + node.getLevel()


# podejmowanie decyzji o rozwoju węzła w algorytmie a*
def aStar(startNode, k, dirPermutation, maxLevel, stats, heurystyka):
        
    #set do przechowywania odwiedzonych plansz (nie wezlow, bo one moga sie różnić kierunkiem)
    visited = set()
    processed = set()

    stats.setMaxLevel(0)

    counter = itertools.count()  # licznik dla każdego węzła (eliminuje przypadek gdy dwa węzły mają taki sam priorytet)

    #tworzymy kopiec priorytetowy
    #kopiec jest szybszy od kolejki priorytetowaj
    #kolejka priorytetowa jest zaimplementowana na kopcu binarnym
    heapq = []

    #dodajemy wezel startowy do kopca -> (koszt, wezel)
    #koszt = heurystyka + ilosc ruchow od startu
    #przy wyciaganiu elementow z kopca, wybierane sa elementy wzgledem kosztu, a jesli koszt jest taki sam, to wzgledem licznika, nastepnie po wezle (nie dojdzie do tego bo licznik sie rozni zawsze)
    heappush(heapq, (cost(startNode, heurystyka), next(counter), startNode))
    visited.add(tuple(map(tuple, startNode.getBoard()))) #dodajemy plansze jjako odwiedzona
    #krotka, bo lista nie jest hashowalna, a krotka jest


    

    while(heapq): #dopoki w kolejce sa wezly

        #riorytet jest określany przez pierwszy element krotki, a kolejne elementy są używane jako tiebreakery, jeśli pierwszy element jest taki sam
        _, _, currentNode = heappop(heapq) #pobieramy wezel z kolejki

        #sprawdzamy czy nie przekroczylismy maksymalnej glebokosci
        # print(currentNode.getLevel())
        if(currentNode.getLevel() > stats.getMaxLevel()):
            stats.setMaxLevel(currentNode.getLevel())


        #sprawdzamyczy to jest rozwiazanie
        processed.add(tuple(map(tuple, currentNode.getBoard()))) #dodajemy plansze jjako przetworzona
        #krotka, bo lista nie jest hashowalna, a krotka jest
        if currentNode.isSolution():
            stats.setVisited(len(visited))
            stats.setProcessed(len(processed))
            return currentNode.getStringPath()
        

        if(currentNode.getLevel() == maxLevel):
            stats.setVisited(len(visited))
            stats.setProcessed(len(processed))
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
                visited.add(tuple(map(tuple, currentNode.getBoard()))) #dodajemy plansze jjako odwiedzona
                # processed.add(tuple(map(tuple, currentNode.getBoard()))) #dodajemy plansze jjako przetworzona

                # if newNode.isSolution():
                #     stats.setVisited(len(visited))
                #     stats.setProcessed(len(visited))
                #     return newNode.getStringPath()

    stats.setVisited(len(visited))
    stats.setProcessed(len(processed))

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