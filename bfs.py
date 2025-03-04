from collections import deque

def bfs(startNode):
    #kolejka fif do przechowywania wezlow po szerokosci
    queue = deque()

    queue.append(startNode) #dodajemy wezel startowy do kolejki

    #set do przechowywania odwiedzonych plansz (nie wezlow, bo one moga sie różnić kierunkiem)
    visited = set()

    while(queue): #dopoki w kolejce sa wezly
        currentNode = queue.popleft() #pobieramy wezel z kolejki
        visited.add(tuple(map(tuple, currentNode.getBoard()))) #dodajemy plansze jako krotkę do zbioru odwiedzonych
        #krotka, bo lista nie jest hashowalna, a krotka jest

        #sprawdzamyczy to jest rozwiazanie
        if currentNode.isSolution():
            return currentNode.getStringPath()
        
        #dla kazdego ruchu tworzymy nowy wezel
        for direction in ["L", "R", "U", "D"]:
            newNode = currentNode.addNode(direction)
            if(tuple(map(tuple, newNode.getBoard())) not in visited): # jesli plansza nie byla odwiedzona to dodajemy ja do kolejki
                queue.append(newNode)
                if newNode.isSolution():
                    return newNode.getStringPath()
                # print(newNode.getBoard())
                #czekaj na input
                # input()
    return None # nie znaleziono rozwiazania