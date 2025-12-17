import random, time

grid = [
    ["#", "#", "#", "#", "#",],
    ["#", "#", "#", "#", "#",],
    ["#", "#", "#", "#", "#",],
    ["#", "#", "#", "#", "#",],
    ["#", "#", "#", "#", "#",]
]

directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]

size = grid.__len__()
start_position = (0, 0)
current_position = start_position

def checkIfStuck():
    global current_position

    wallsAround = 0
    for direction in directions:
        newPos = (current_position[0] + direction[0], current_position[1] + direction[1])
        if (newPos[0] < 0 or newPos[1] < 0 or newPos[0] >= size or newPos[1] >= size):
            wallsAround += 1
        elif grid[newPos[1]][newPos[0]] == ".":
            wallsAround += 1
    
    if wallsAround >= 4:
        return True
    
    return False

def randomMovement():
    global current_position

    randomChoice = random.choice(directions)
    newPos = (current_position[0] + randomChoice[0], current_position[1] + randomChoice[1])
    if newPos[0] < 0 or newPos[1] < 0 or newPos[0] >= size or newPos[1] >= size:
        return

    if grid[newPos[1]][newPos[0]] == ".":
        return

    grid[newPos[1]][newPos[0]] = "."
    current_position = newPos
    displayGrid()

def displayGrid():
    for y in range(size):
        print("[", end=" ")
        for x in range(size):
            print(grid[y][x], end=" ")
        print("]")
    print("-------------")

while True:
    time.sleep(0.3)
    randomMovement()
    if checkIfStuck():
        print("stuck")
        break
