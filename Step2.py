import random, time, os

width = random.randint(20, 50)
height = random.randint(15, 35)

grid = [['#' for i in range(width)] for _ in range(height)]

max_steps = (width + height) / 1.3
current_steps = 0

start_position = (0, 0)
current_position = start_position
grid[start_position[1]][start_position[0]] = "."

directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def displayGrid():
    clear_screen()
    for y in grid:
        print(" ".join(y))
    print("--------------------")


def checkDestinationSurroundings(destination):
    neighbors = 0
    for direction in directions:
        newPos = (destination[0] + direction[0], destination[1] + direction[1])
        if newPos[0] < 0 or newPos[1] < 0 or newPos[0] >= width or newPos[1] >= height:
            continue
        
        if grid[newPos[1]][newPos[0]] == ".":
            neighbors += 1
    
    if neighbors <= 1:
        return False
    elif neighbors == 2:
        randomChance = random.randint(0, 100)
        if randomChance <= 20:
            return True
        
        return False
    else:
        return True


def randomWalk():
    global current_position

    randomChoice = random.choice(directions)
    newPos = (current_position[0] + randomChoice[0], current_position[1] + randomChoice[1])
    if newPos[0] < 0 or newPos[1] < 0 or newPos[0] >= width or newPos[1] >= height:
        return

    #if grid[newPos[1]][newPos[0]] == ".":
    #    return

    if checkDestinationSurroundings(newPos) or current_steps < 20:
        grid[newPos[1]][newPos[0]] = "."
        current_position = newPos
    
    displayGrid()


while True:
    time.sleep(0.02)
    randomWalk()
    if current_steps >= max_steps:
        print("Reached max steps")
        break
