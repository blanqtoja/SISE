import copy
import convertMatrix
import fieldSwitch as fs

class BoardNode:

    # pola klassy
    board = [] # plansza
    parent = None # rodzic w drzewie
    direction = "" # kierunek w jakim przesunieto pusty punkt
    level = 0 # poziom w drzewie
    xZero = 0
    yZero = 0

    # konstruktor 
    # parametry:
    #   board - plansza 2D, stan układanki
    #   parent - BoardNode, rodzic w drzewie
    #   direction - string, kierunek w jakim przesunieto pusty punkt (potrzebne do optymalizacji)
    def __init__(self, board, parent, direction, xZero, yZero): 
        self.board = board
        self.parent = parent
        self.direction = direction
        if(parent != None):
            self.level = parent.getLevel() + 1
        else:
            self.level = 0
        
        self.xZero = xZero
        self.yZero = yZero

    # funkcja zwracająca współrzędne pustego pola
    # zwraca:
    #   int, współrzędna x
    #   int, współrzędna y
    def getZeroField(self):
        return self.xZero, self.yZero

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

    def addNode(self, newDirection, col):
        # tworzymy nową planszę na podstawie aktualnej
        # newBoard = []
        # for row in self.board:
        #     newBoard.append(row.copy())
        newBoard = copy.deepcopy(self.board)

        # tworzymy nowy węzeł

        # if(fs.switchField(convertMatrix.to2D(newBoard, col), newDirection) == False): # przesuwamy puste pole
        #     return None # jesli nie udało się przesunąć pola, to zwracamy None

        newXZero, newYzero = fs.switchField(newBoard, newDirection)
        return BoardNode(newBoard, self, newDirection, newXZero, newYzero)
        
    
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
        # return len(self.board)
        return len(self.board), len(self.board[0])
    
    # funkcja sprawdzająca czy plansza jest rozwiązaniem
    # zwraca:
    #   bool, True jeśli plansza jest rozwiązaniem, False w przeciwnym wypadku

    def isSolution(self):
        w, k = self.getSize()

        if(self.board[w-1][k-1] != 0): #ostatni element to 0, wiec jesli nie jest to nie jest to rozwiazanie
            return False       

        #przeszukujemy planszę, przerywamy jesli spotkamy element, ktory nie jest na swoim miejscu
        for i in range(w-1): #wiersze - mnozymy przez k (ilosc elementow w wierszu)
            for j in range(k-1): 
                if(i == w-1 and j == k-1):
                    break
                if(self.board[i][j] != i*k + j +1):
                    return False
        
        # k = self.getSize()

        # if(self.board[k-1] != 0): #ostatni element to 0, wiec jesli nie jest to nie jest to rozwiazanie
        #     return False

        # #przeszukujemy planszę, przerywamy jesli spotkamy element, ktory nie jest na swoim miejscu
        # for i in range(k-2): #wiersze - mnozymy przez k (ilosc elementow w wierszu)
        #     if(self.board[i] != i+1):
        #         return False
            
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