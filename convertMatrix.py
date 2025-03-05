#Convert a 1D array to a 2D array
def to2D (_1Darray, width):
    return [ _1Darray[i:i+width] for i in range(0, len(_1Darray), width) ]

#Convert a 2D array to a 1D array
def to1D (_2Darray):
    return [ elem for row in _2Darray for elem in row ]