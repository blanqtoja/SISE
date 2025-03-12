class stat:
    # Wymagania funkcjonalne:
    # długość znalezionego rozwiązania; X
    # liczbę stanów odwiedzonych; X
    # liczbę stanów przetworzonych; X
    # maksymalną osiągniętą głębokość rekursji; X
    # czas trwania procesu obliczeniowego. X
    def __init__(self):
        self.lenFound = None
        self.visited = None
        self.processed = None
        self.maxLevel = None
        self.time = None
        self.path = None

    def setLenFound(self, lenFound):
        self.lenFound = lenFound

    def setVisited(self, visited):
        self.visited = visited

    def setProcessed(self, processed):
        self.processed = processed

    def setMaxLevel(self, maxLevel):
        self.maxLevel = maxLevel

    def setTime(self, time):
        self.time = time

    def setPath(self, path):
        self.path = path

    def getLenFound(self):
        return self.lenFound

    def getVisited(self):
        return self.visited
    
    def getProcessed(self):
        return self.processed
    
    def getMaxLevel(self):
        return self.maxLevel
    
    def getTime(self):
        return self.time
    
    def getPath(self):
        return self.path
    
    def __str__(self):
        return "LenFound: " + str(self.lenFound) + "\nVisited: " + str(self.visited) + "\nProcessed: " + str(self.processed) + "\nMaxLevel: " + str(self.maxLevel) + "\nTime: " + str(self.time) + "\nPath: " + str(self.path)