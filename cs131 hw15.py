
## CS131 Assignment/Exercise 15
## Prajwal Bhandari
## April 2024


def render(board: list[list[str]], winner: set[tuple[int, int]] | None) -> None:
    """Renders the game board to the console.
    Args:
        board (list[list[str]]): A column-major list of the tokens to render.
        winner (set[tuple[int, int]] | None): A set of row/column pairs marking\
            the winning cells of the board. Each tuple should be a (row, col)\
            pair, where the `row` and `col` are the respective values **in the\
            list, not render**. If there is no winner, this should be `None`.

    Exceptions:
        Asserts if the size of the board is not at least 4.
    """
    size = len(board)  # Make sure length makes sense...
    assert size >= 4, f"The board size must be >= 4, not {size}"

    # Make winner an empty set it if was None
    if not isinstance(winner, set):
        winner = set[tuple[int, int]]()

    for R in range(size - 1, -1, -1):  # Rows (for printing)
        print("    ", "+---" * size, "+", sep="")

        print("    ", end="")
        for C in range(size):  # Columns (for printing)
            if R < len(board[C]):  # Check if there's really data
                # Note that `C` is first; column-major order!
                token = board[C][R]

                # Note that `(R, C)` is about the list itself, not the render!
                if winner.issuperset(((C, R),)):
                    print(f"|({token:1})", end="")  # Winner!
                else:
                    print(f"|{token:^3}", end="")

            else:  # Jagged; assume blank
                print("|   ", end="")
        print("|")
    print("    ", "+---" * size, "+", sep="")

def isin(a,b):
    for item in b:
        if item==a:
            return True
    return False

def min(a:int,b:int) -> int:
    if a<b: return a
    return b 

## The Gane 

def mark_winner(player: int, cells: set[tuple[int, int]] | None) -> None:
    """A special function for the Ag to know who won a match. If no one won as
    there was a tie, you should indicate player `0` won and provide an empty
    set.

    For your code, this doesn't do anything, but it will have special meaning to
    the Ag. You do not need to write any code for this function.

    Args:
        player (int): The player who won; either `1` or `2`. If no one won,\
            this should be `0`.
        cells (set[tuple[int, int]] | None): The cells that caused the win, as\
            a set of (row, col) pairs into the list, not the rendered board. If
            no one won, this should be `None`.
    """
    pass

def check_winner(board: list[list[str]], pos:tuple[int]) -> set | None :
    '''
    check a col by initializing the token and connections
    if the next item matches token, add 1 to connections, else reset connection to 1 and reset winning squares
    if we ever get to connection==4 return the value of the token key
    we know the dictionary will work since the only tokens being inserted to the list are "X" and "O"
    '''
    # Initialize which token corresponds to which player and the position
    player={"X":1, "O": 2}
    c, r = pos
    connection=0
    token = board[c][r]
    winning_squares=[]         
    
    #check through the column
    for i in range(min(len(board[c]), 4)):
        if board[c][r-i] == token:
            connection+=1
            winning_squares.append((c,r-i)) 

    if connection >= 4 and len(winning_squares)>=4:
        print(f"Congratulations player {player[token]}, you win!")
        return set(winning_squares)
    
    #check row
    
    #check to the right 
    connection=1
    try:
        winning_squares=[(c,r)]
        for i in range(1,4):
            if c+i<len(board) and board[c+i][r] == token and isin((c+i-1,r), winning_squares):
                connection+=1
                winning_squares.append((c+i,r))
    except IndexError:
        pass
        
    if connection >= 4 and len(winning_squares)>=4:
        print(f"Congratulations player {player[token]}, you win!")
        return set(winning_squares)
    
    #check left
    try:
        for i in range(1,4):
            if c-i>=0 and board[c-i][r] == token and isin((c-i+1,r),winning_squares):
                connection+=1
                winning_squares.append((c-i,r))
    except IndexError:
        pass
    
    if connection >= 4 and len(winning_squares)>=4:
        print(f"Congratulations player {player[token]}, you win!")
        return set(winning_squares)
    
    #check diagonal 

    # up-right, down-left diagonal
    connection =1
    try:
        winning_squares=[(c,r)]
        for i in range(1,4):
            if c+i<len(board) and r+i<len(board) and board[c+i][r+i] == token  and isin((c+i-1,r+i-1),winning_squares):
                connection+=1
                winning_squares.append((c+i,r+i))
    except IndexError:
        pass
        
    if connection >= 4 and len(winning_squares)>=4:
        print(f"Congratulations player {player[token]}, you win!")
        return set(winning_squares)
    
    try:
        for i in range(1,4):
            if c-i>=0 and r-i>=0 and board[c-i][r-i] == token and isin((c-i+1,r-i+1),winning_squares):
                connection+=1
                winning_squares.append((c-i,r-i))
    except IndexError:
        pass

    if connection >= 4 and len(winning_squares)>=4:
        print(f"Congratulations player {player[token]}, you win!")
        # render(board,winning_squares)
        return set(winning_squares)
    
    # up-left, down-right diagonal
    connection=1
    try:
        winning_squares=[(c,r)]
        for i in range(1,4):
            if c-i>=0 and r+i<len(board) and board[c-i][r+i] == token and isin((c-i+1,r+i-1),winning_squares):
                connection+=1
                winning_squares.append((c-i,r+i))
    except IndexError:
        pass 
    
    if connection >= 4 and len(winning_squares)>=4:
        print(f"Congratulations player {player[token]}, you win!")
        return set(winning_squares)
    
    try:
        for i in range(1,4):
            if c+i<len(board) and r-i>=0 and board[c+i][r-i] == token and isin((c+i-1,r-i+1),winning_squares):
                connection+=1
                winning_squares.append((c+i,r-i))
    except IndexError:
        pass
            
    if connection >= 4 and len(winning_squares)>=4:
        print(f"Congratulations player {player[token]}, you win!")
        return set(winning_squares)

    return None

def create_board() -> tuple[list[list], int]:
    # ask user
    boardsize = input("How big do you want the square board to be (N rows by N columns, N>=4)? ")
    # default size
    if boardsize == "":
        boardsize = 7
    elif not( boardsize.isdigit() and int(boardsize)>=4) :
        print(f"Board size must be an integer greater than or equal to 4, not {boardsize}.")
        boardsize=input("Enter another integer for the size of the board. ")
    boardsize=int(boardsize)
    # create board
    board=[]
    for i in range(boardsize):
        board.append([])
    
    return board,boardsize

def player_one_turn(board, boardsize) -> tuple[list[list[str]],int]:
    #set token for player
    token="X"
    #ask where they want to place token (gravity)
    p1_col = input(f"P1: Choose a column from 0 to {boardsize-1} to place your token. ")
    #checks if input is a number and that its in bounds of the board and if the column that the player requested is not already full
    while not (p1_col.isdigit() and 0<=int(p1_col)<boardsize and len(board[int(p1_col)])<boardsize):
        
        p1_col=input(f"P1: Enter a valid integer from 0 to {boardsize-1} to place your token. ")
        
    #append if able to append
    p1_col=int(p1_col)
    if 0<=p1_col<boardsize and  len(board[p1_col])<boardsize:
        board[p1_col].append(token)

    return board, p1_col

def player_two_turn(board, boardsize) -> tuple[list[list[str]],int]:
    #same as player_one_turn, but with a different token
    token="O"
    p2_col = input(f"P2: Choose a column from 0 to {boardsize-1} to place your token. ")
    
    while not (p2_col.isdigit() and 0<=int(p2_col)<boardsize and len(board[int(p2_col)])<boardsize):
        p2_col=input(f"P2:Enter a valid integer from 0 to {boardsize-1} to place your token. ")

    p2_col=int(p2_col)
    if 0<=p2_col<boardsize and len(board[p2_col])<boardsize:
        board[p2_col].append(token)

    return board, p2_col

def connect_four() -> None:
    board, boardsize=create_board()
    render(board,None)
    n=1
    winning_squares=None
    while winning_squares==None and n<=boardsize**2:
        if n%2 ==1:
            board, p1_col= player_one_turn(board,boardsize)
            winning_squares = check_winner(board,(p1_col, len(board[p1_col])-1))
            render(board,winning_squares)
            if winning_squares!= None:
                mark_winner(1,winning_squares)
        if n%2==0:
            board, p2_col = player_two_turn(board,boardsize)
            winning_squares = check_winner(board,(p2_col,len(board[p2_col])-1))
            render(board,winning_squares)
            if winning_squares != None:
                mark_winner(2,winning_squares)
        n+=1 
    
    
    if n>boardsize**2 and winning_squares==None:
        print("There has been a tie. Thanks for playing!")
        mark_winner(0,None) 
    return
    

def main():
    connect_four()
    
    pass

if __name__ == "__main__":
    main()
