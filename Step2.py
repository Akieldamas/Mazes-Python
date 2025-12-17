import random, time, os

width = random.randint(20, 50)
height = random.randint(15, 35)

grid = [['#' for i in range(width)] for _ in range(height)]

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


def randomWalk():
    global current_position

    randomChoice = random.choice(directions)
    newPos = (current_position[0] + randomChoice[0], current_position[1] + randomChoice[1])
    if newPos[0] < 0 or newPos[1] < 0 or newPos[0] >= width or newPos[1] >= height:
        return

    if grid[newPos[1]][newPos[0]] == ".":
        return

    grid[newPos[1]][newPos[0]] = "."
    current_position = newPos
    displayGrid()    


while True:
    time.sleep(0.3)
    randomWalk()
