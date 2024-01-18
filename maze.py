import random

SIZE = 8
PLAYER_POSITION = [1, 1]
EXIT_POSITION = [SIZE, SIZE]


def add_random_treasures(maze):
    for i in range(1, SIZE + 1):
        for j in range(1, SIZE + 1):
            if maze[i][j] == '   ' or maze[i][j] == ' * ':
                if random.choice([True, False]) == True:
                    maze[i][j] = f" {random.randint(1, 5)} "
    return maze


def add_random_paths(maze):
    for i in range(1, SIZE + 1):
        for j in range(1, SIZE + 1):
            if random.choice([True, False]) == True:
                maze[i][j] = '   '
    return maze


def init_maze(maze):
    for i in range(SIZE+2):
        row = []
        for j in range(SIZE+2):
            row.append(" * ")
        maze.append(row)
    return maze


def create_paths(maze):
    for i in range(1, SIZE+1):
        maze[1][i] = "   "
        maze[SIZE][i] = "   "
        maze[i][1] = "   "
        maze[i][SIZE] = "   "
    return maze


def generate_maze(maze):
    init_maze(maze)
    create_paths(maze)
    add_random_treasures(maze)
    add_random_paths(maze)
    return maze


def maze_printing(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            print(maze[i][j], end=" ")
        print()



def main():
    seed_number = input("Enter a seed:\n")
    random.seed(seed_number)
    maze = []
    generate_maze(maze)

    starting_treasure = maze[1][1]
    maze[1][1] = " P "
    maze[SIZE][SIZE] = " E "
    maze_printing(maze)

    points = 0
    move_count = 0

    while move_count < 1:
        move = input("Enter your move (W/A/S/D):\n").lower()
        if move == "s":
            if maze[2][1] != " * ":
                move_count += 1
                if maze[2][1] != "   ":
                    points += int(maze[2][1])-1
                else:
                    points -= 1
                maze[2][1] = " P "
                maze[1][1] = starting_treasure
        elif move == "d":
            if maze[1][2] != " * ":
                move_count += 1
                if maze[1][2] != "   ":
                    points += int(maze[1][2])-1
                else:
                    points -= 1
                maze[1][2] = " P "
                maze[1][1] = starting_treasure
        maze_printing(maze)

    x = 0
    y = 0
    while maze[SIZE][SIZE] != " P ":
        move = input("Enter your move (W/A/S/D):\n").lower()
        for i in range(1, SIZE+2):
            for j in range(1, SIZE+2):
                if maze[i][j] == " P ":
                    x = i
                    y = j
        if move == "w":
            if maze[x-1][y] != " * ":
                move_count += 1
                if maze[x-1][y] != "   " and maze[x-1][y] != " E ":
                    points += int(maze[x-1][y])-1
                else:
                    points -= 1
                maze[x-1][y] = " P "
                maze[x][y] = "   "
        elif move == "a":
            if maze[x][y-1] != " * ":
                move_count += 1
                if maze[x][y-1] != "   " and maze[x][y-1] != " E ":
                    points += int(maze[x][y-1])-1
                else:
                    points -= 1
                maze[x][y-1] = " P "
                maze[x][y] = "   "
        elif move == "s":
            if maze[x+1][y] != " * ":
                move_count += 1
                if maze[x+1][y] != "   " and maze[x+1][y] != " E ":
                    points += int(maze[x+1][y])-1
                else:
                    points -= 1
                maze[x+1][y] = " P "
                maze[x][y] = "   "
        elif move == "d":
            if maze[x][y+1] != " * ":
                move_count += 1
                if maze[x][y+1] != "   " and maze[x][y+1] != " E ":
                    points += int(maze[x][y+1]) -1
                else:
                    points -= 1
                maze[x][y+1] = " P "
                maze[x][y] = "   "
        maze_printing(maze)
    print(f"Congratulations, you've escaped the maze with {points} points!")


main()