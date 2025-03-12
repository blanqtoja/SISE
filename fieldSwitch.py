def findZeroField(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j
    return -1, -1



# funkcja przesuwająca puste pole w danej planszy
# 
# params: 
#   board - lista 2D, trzeba zapewnic, ze pole 0 da sie przesunac w podanym kierunku
#   direction - string, "L", "R", "U", "D"
# returns: true jeśli udało się przesunąć pole, false w przeciwnym wypadku
def switchField(board, direction):
    
    row, col = len(board), len(board[0])

    x, y = findZeroField(board) # znajdujemy wspolrzedne pustego pola

    # majac wspolrzedne pustego pola, mozemy go przesunac wedlug kierunku
    if(direction == "L"):
        if(y > 0):
            board[x][y], board[x][y-1] = board[x][y-1], board[x][y] # zamieniamy puste pole z polem obok
    elif(direction == "R"):
        if(y < col-1):
            board[x][y], board[x][y+1] = board[x][y+1], board[x][y]
    elif(direction == "U"):
        if(x >0):
            board[x][y], board[x-1][y] = board[x-1][y], board[x][y]
    elif(direction == "D"):
        if(x < row-1):
            board[x][y], board[x+1][y] = board[x+1][y], board[x][y]
    