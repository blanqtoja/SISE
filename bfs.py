from collections import deque
from BoardNode import BoardNode
import fieldSwitch as fs
import convertMatrix

def bfs(startNode, k, dirPermutation, maxLevel):
    #kolejka fif do przechowywania wezlow po szerokosci
    queue = deque()

    queue.append(startNode) #dodajemy wezel startowy do kolejki

    #set do przechowywania odwiedzonych plansz (nie wezlow, bo one moga sie różnić kierunkiem)
    visited = set()

    while(queue): #dopoki w kolejce sa wezly
        currentNode = queue.popleft() #pobieramy wezel z kolejki
        visited.add(tuple(currentNode.getBoard())) #dodajemy plansze jako krotkę do zbioru odwiedzonych
        #krotka, bo lista nie jest hashowalna, a krotka jest

        #sprawdzamyczy to jest rozwiazanie
        if currentNode.isSolution():
            return currentNode.getStringPath()
        
        #sprawdzamy czy nie przekroczylismy maksymalnej glebokosci
        print(currentNode.getLevel())
        if(currentNode.getLevel() == maxLevel):
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
            
            row, col = fs.findZeroField(convertMatrix.to2D(currentNode.getBoard(), k)) 
            
            #sprawdzamy czy puste pole jest na skraju i czy chcemy je przesunac w tym kierunku
            if(row == 0 and direction == "U"):
                continue
            if(row == (len(currentNode.getBoard())/k)-1 and direction == "D"):
                continue
            if(col == 0 and direction == "L"):
                continue
            if(col == k-1 and direction == "R"):
                continue
    
            newNode = currentNode.addNode(direction, k)
            if(tuple(newNode.getBoard()) not in visited): # jesli plansza nie byla odwiedzona to dodajemy ja do kolejki
                queue.append(newNode)
                if newNode.isSolution():
                    return newNode.getStringPath()
                # print(newNode.getBoard())
                #czekaj na input
                # input()
    return None # nie znaleziono rozwiazania