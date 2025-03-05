import fieldSwitch as fs

class BoardNode:

    # pola klassy
    board = [] # plansza
    parent = None # rodzic w drzewie
    direction = "" # kierunek w jakim przesunieto pusty punkt
    level = 0 # poziom w drzewie

    # konstruktor 
    # parametry:
    #   board - plansza 2D, stan układanki
    #   parent - BoardNode, rodzic w drzewie
    #   direction - string, kierunek w jakim przesunieto pusty punkt (potrzebne do optymalizacji)
    def __init__(self, board, parent, direction): 
        self.board = board
        self.parent = parent
        self.direction = direction
        if(parent != None):
            self.level = parent.getLevel() + 1
        else:
            self.level = 0

    # funkcja zwracająca poziom w drzewie
    # zwraca:
    #   int, poziom
    def getLevel(self):
        return self.level

    # funckja dodająca nowy węzeł do drzewa
    # parametry:
    #   direction - string, kierunek w jakim przesunieto pusty punkt
    # zwraca:  
    #   BoardNode, nowy węzeł

    def addNode(self, newDirection):
        # tworzymy nową planszę na podstawie aktualnej
        newBoard = []
        for row in self.board:
            newBoard.append(row.copy())
        
        # tworzymy nowy węzeł
        #todo: moze to zły pomysl
        if(fs.switchField(newBoard, newDirection) == False): # przesuwamy puste pole
            return None # jesli nie udało się przesunąć pola, to zwracamy None
        return BoardNode(newBoard, self, newDirection)
        
    
    # funkcja zwracająca rodzica węzła
    # zwraca:
    #   BoardNode, rodzic węzła
    def getParent(self):
        return self.parent
    
    # funkcja zwracająca kierunek w jakim przesunięto pusty punkt
    # zwraca:
    #   string, kierunek
    def getDirection(self):
        return self.direction
    
    # funkcja zwracająca planszę
    # zwraca:
    #   lista 2D, plansza
    def getBoard(self):
        return self.board
    
    # funkcja zwracająca rozmiar planszy
    # zwraca:
    #   int, liczba wierszy 
    #   int, liczba kolumn
    def getSize(self):
        return len(self.board), len(self.board[0])
    
    # funkcja sprawdzająca czy plansza jest rozwiązaniem
    # zwraca:
    #   bool, True jeśli plansza jest rozwiązaniem, False w przeciwnym wypadku

    def isSolution(self):
        #pobieram rozmiar planszy
        # print("sprawdzam rozwiazanie")

        w, k = self.getSize()

        #przeszukujemy planszę, przerywamy jesli spotkamy element, ktory nie jest na swoim miejscu
        for i in range(w): #wiersze - mnozymy przez k (ilosc elementow w wierszu)
            for j in range(k): 
                if(i == w-1 and j == k-1): #ostatni element to 0
                    break
                if(self.board[i][j] != i*k + j +1):
                    return False
                

        
        return True
    
    # funkcja zwracajaca ścieżkę do rozwiązania
    # zwraca:
    #   list, ścieżka do rozwiązania
    def getPath(self):
        path=[] #sciezka do rozwiazania
        node = self 
        while(node != None): #dopóki nie dojdziemy do korzenia
            path.append(node) #dodajemy node do sciezki
            node = node.getParent() #przechodzimy do rodzica
        path.reverse() # odwracamy sciezke, bo zaczynalismy od konca
        return path
    
    # funkcja przetwarzajaca sciezke/lite wezlow na string liter (L, R, U, D)
    # parametry:
    #   path - list, ścieżka do rozwiązania
    # zwraca:
    #   string, sciezka w postaci liter
    def getStringPath(self):
        path = self.getPath()
        pathString = ""
        for node in path:
            pathString += node.getDirection()
        return pathString