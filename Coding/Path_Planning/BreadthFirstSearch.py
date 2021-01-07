import queue
import os
import colorama

def createMaze():
    maze = []
    maze.append(["#","#", "#", "#", "#", "O","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", " ", " ","#"])
    maze.append(["#"," ", "#", "#", "#", " ","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#","#", "#", "#", "#", "X","#"])

    return maze

def createMaze1():
    maze = []
    maze.append(["#","O", "#", "#", "#", "#", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", "#", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", "#", "#", "#", "#", " ", "#"])
    maze.append(["#"," ", " ", " ", "#", " ", " ", "X", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", " ", " ", "#"])
    maze.append(["#","#", "#", "#", "#", "#", "#", "#", "#"])

    return maze

def createMaze2():
    maze = []
    maze.append(["#","#", "#", "#", "#", "O", "#", "#", "#", "#", "#", "#", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#"," ", "#", "#", " ", "#", "#", " ", " ", " ", " ", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#", "#", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#", " ", "#", "#", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", "#", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#","#", "#", "#", "#", " ", "#", " ", "#", " ", "#", " ", " ", " ", "#"])
    maze.append(["#"," ", " ", " ", "#", " ", "#", " ", "#", "#", "#", "#", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", " ", "#", " ", "#", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", "#", " ", "#", " ", "#", "#", " ", "#"])
    maze.append(["#","X", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", "#"])
    maze.append(["#","#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"])

    return maze


def printMaze(maze, path=""):
    print(CLEAR_SCREEN + RED + 'Welcome!' + RESET)
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))
    
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print( RED + "+ ", end=""+ RESET)
            else:
                print(col + " ", end="")
        print()
        


def valid(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False

    return True


def findEnd(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if maze[j][i] == "X":
        print("Found: " + moves)
        printMaze(maze, moves)
        return True

    return False


# MAIN ALGORITHM
colorama.init()
nums = queue.Queue()
nums.put("")
add = ""
maze  = createMaze1()
CLEAR_SCREEN = '\033[2J'
RED = '\033[31m'   # mode 31 = red forground
RESET = '\033[0m'  # mode 0  = reset

while not findEnd(maze, add): 
    add = nums.get()
    #print(add)
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(maze, put):
            nums.put(put)
