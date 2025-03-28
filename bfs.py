from collections import deque
from BoardNode import BoardNode
import fieldSwitch as fs
import convertMatrix

def bfs(startNode, k, dirPermutation, maxLevel, stats):
    
    #set do przechowywania odwiedzonych plansz (nie wezlow, bo one moga sie różnić kierunkiem)
    visited = set()
    processed = set()

    stats.setMaxLevel(0)

    #kolejka fifo do przechowywania wezlow po szerokosci
    queue = deque()

    queue.append(startNode) #dodajemy wezel startowy do kolejki
    visited.add(tuple(map(tuple, currentNode.getBoard()))) #dodajemy plansze jako krotkę do zbioru odwiedzonych
    

    while(queue): #dopoki w kolejce sa wezly
        currentNode = queue.popleft() #pobieramy wezel z kolejki
        visited.add(tuple(map(tuple, currentNode.getBoard()))) #dodajemy plansze jako krotkę do zbioru odwiedzonych
        #krotka, bo lista nie jest hashowalna, a krotka jest

        #sprawdzamy czy nie przekroczylismy maksymalnej glebokosci
        # print(currentNode.getLevel())
        if(currentNode.getLevel() > stats.getMaxLevel()):
            stats.setMaxLevel(currentNode.getLevel())


        #sprawdzamyczy to jest rozwiazanie
        processed.add(tuple(map(tuple, currentNode.getBoard()))) #dodajemy plansze jjako przetworzona
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
            
            # row, col = fs.findZeroField(currentNode.getBoard()) 
            row, col = currentNode.getZeroField()
            
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
                queue.append(newNode)
                visited.add(tuple(map(tuple, currentNode.getBoard()))) #dodajemy plansze jako krotkę do zbioru odwiedzonych

                # if newNode.isSolution():
                #     stats.setVisited(len(visited))
                #     stats.setProcessed(len(visited))
                #     return newNode.getStringPath()

    stats.setVisited(len(visited))
    stats.setProcessed(len(visited))

    return None # nie znaleziono rozwiazania