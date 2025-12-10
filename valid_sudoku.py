def isValidSudoku(board):
    # recorrer filas 
    for i in range(len(board)):
        numbers = set()
        for cell in board[i]:
            if cell == ".":
                continue
            if cell in numbers:
                return False
            numbers.add(cell)

    #  recorrer columnas
    for i in range(len(board)):
        numbers = set()
        for k in range(len(board)):
            if board[k][i] == ".":
                continue
            if board[k][i] in numbers:
                return False
            numbers.add(board[k][i])

    # recorrer cuadros de 3x3
    n = 0
    z = 0
    for i in range(3):
        for i in range(3):
            ## bloque inicia
            numbers = set()
            for i in range(n,n+3):
                for k in range(z,z+3):
                    if board[i][k] == ".":
                        continue
                    if board[i][k] in numbers:
                        return False
                    numbers.add(board[i][k])
            n += 3
            ## bloque termina
        n = 0
        z += 3

    return True

## llamar la funcion
board = [
 ["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]
 ]

print(isValidSudoku(board))
