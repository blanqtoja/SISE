
# funkcja przesuwająca puste pole w danej planszy
# params: 
#   board - lista 2D 
#   direction - string, "L", "R", "U", "D"
# returns: true jeśli udało się przesunąć pole, false w przeciwnym wypadku
def switchField(board, direction):
    w = len(board) # liczba wierszy
    k = len(board[0]) # liczba kolumn
     
    # szukamy pustego pola
    x, y = 0, 0 # współrzędne pustego pola

    for i in range (0, w):
        for j in range(0, k):
            if board[i][j] == 0:
                x, y = i, j
                break

    # majac wspolrzedne pustego pola, mozemy go przesunac wedlug kierunku
    if(direction == "L"):
        if y == 0: #pole nie moze sie przesunac w relo, jesli jest juz na skraju
            return False
        else:
            board[x][y], board[x][y-1] = board[x][y-1], board[x][y] # zamieniamy puste pole z polem obok
    elif(direction == "R"):
        if(y == k-1):
            return False
        else:
            board[x][y], board[x][y+1] = board[x][y+1], board[x][y]
    elif(direction == "U"):
        if(x == 0):
            return False
        else:
            board[x][y], board[x-1][y] = board[x-1][y], board[x][y]
    elif(direction == "D"):
        if(x == w-1):
            return False
        else:
            board[x][y], board[x+1][y] = board[x+1][y], board[x][y]
    
    return True

