
## CS131 Exerise/Assignment 12
## Prajwal Bhandari
## April 2024


def isin(a, b:list) ->bool:
    for _ in range(len(b)):
        if b[_] == a:
            return True
    return False


def load_data(fn:str) ->dict:   
    d = {}
    file = open(fn,"r")

    #first line of file gives us the name of the maze.
    line = file.readline()

    #set the "name" entry in d to our filename.
    d["name"] = line.strip()
    
    #read and split the second line, then temp[0] gives us our size, and temp[1] gives us the number of exits that exist
    temp = file.readline()
    temp=temp.strip().split(",")
    d["size"] = int(temp[0])
    d["numexits"] = int(temp[1])

    temp=file.readline()
    #this line gives us our starting position, temp.strip().split(), which is a list of integers
    d["start"]=[]
    for i in range(len(temp.strip().split(","))):
        d["start"].append(int(temp.strip().split(",")[i]))
    
    #method of storing all the exits as a list of lists in our dictionary.
    exits = []
    for _ in range(d["numexits"]):
        temp = file.readline()
        tempe=[]
        for i in range(len(temp.strip().split(","))):
           tempe.append(int(temp.strip().split(",")[i]))
        exits.append(tempe)
    d["exits"] = exits

    #method of storing the board as a list of lists in our dictionary 
    board=[]
    for _ in range(int(d.get("size"))):
        temp = file.readline()
        bline=[]
        for z in range(len(temp.split(","))):
            bline.append(int(temp.split(",")[z]))
        board.append(bline)
    d["board"] = board  

    file.close() #dont need file anymore.

    #best path/steps
    d["steps"] = []
    #the potential path we might take
    d["potential"] = [] 
    #keep track of the visited squares
    d["visited"] = []
    return d


def save_data(fn:str, data:dict) ->None: 
    if isinstance(data.get("steps", []), list):
        file=open(fn,"w")

        file.write("Name: " + data["name"] + "\n")
        file.write("Size: " + str(data["size"]) + "\n")
        file.write("Number of Exits: "  + str(data["numexits"]) + "\n")
        for i in range(data["numexits"]):
            file.write('\t Exit ' + str(i+1) + ": " + str(data["exits"][i]) + "\n")
        file.write("Steps: " +str(len(data["steps"])) + "\n")
        file.write("Start: " + str(data["start"]) + "\n")
        file.write("\n")
        file.write("***************************************** \n")
        file.write("Solution: \n")
        
        #set a map from which we will get what words to write from via letters
        steps = {'U':'UP','R': 'RIGHT','L':'LEFT','D': 'DOWN'}
        sol = data["steps"]
        for _ in range(len(sol)):
            file.write(steps[str(sol[_])] + "\n")
    else: 
        print("data[\"steps\"] must be a list!"); return
    

    file.close()


def can_move(data:dict, col:int, row:int) ->bool:
    #maze is a 2d matrix called by data["board"]
    if (0 <= col < data["size"] and 0 <= row < data["size"]) and (data["board"][row][col] == 0):
        return True
    return False


def solve_helper(data:dict, col:int, row:int) ->None: #=d 
    
    #check if we are already on an exit (base case)
    for _ in range(len(data["exits"])):
        if (row == data["exits"][_][1] and col == data["exits"][_][0]):
            print("at an exit:", [row,col])
            if data["steps"]==[]:
                data["steps"] = data["potential"]
            elif data["potential"]!=[] and len(data["potential"]) < len(data["steps"]):
                data["steps"] = data["potential"].copy() #again, copy the VALUES
                print(data["steps"])
                return
    
    # moves and directions
    directions=["L", "R", "U", "D"]
    moves= [[-1,0], [1,0], [0,-1], [0,1]]  #have to move in col,row format

    for i in range(len(moves)):
        newrow = row + moves[i][1]
        newcol = col + moves[i][0]
        if can_move(data, newcol, newrow) and not isin([newrow,newcol],data["visited"]): 
            # set square we are on to 2 and add the direction to our potential list
            data["board"][row][col] = 2
            data["potential"].append(directions[i])
            data["visited"].append([newrow,newcol])
          
            #recusion time 
            solve_helper(data,newcol,newrow)

            #backtracking
            data["board"][row][col] = 0
            data["potential"].pop()      #pop both the visited and potential list


def solve(input_fn:str, output_fn:str) ->None:
    data = load_data(input_fn)
    col = data["start"][0]
    row = data["start"][1]
    #get our board data and the starting position 
    solve_helper(data,row,col)
    print(data)
    #write down our data into another text file
    save_data(output_fn,data)
    pass


def main():
    solve("HW12\\empty.csv", "HW12\\Maze Solution.txt")
    # print(load_data("HW12\\empty.csv"))


if __name__=="__main__":
    main()