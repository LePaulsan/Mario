from Graph import Graph
from MazeData import MazeData
from MazeMaker import MazeMaker
from PathFinder import PathFinder
from Mario import Mario


mazeData = MazeData()
mazeMaker = MazeMaker(mazeData.WALL, mazeData.PATH, mazeData.PATHTUPLE, mazeData.START, mazeData.END)
graph = Graph(mazeMaker)
pathFinder = PathFinder(graph, mazeData.START, mazeData.END)
mario = Mario(mazeMaker.maze, mazeData.WENTPATH, mazeData.MARIO, mazeData.START)


def display():
    for row in range(mazeMaker.height):
        tempR = ""
        for column in range(mazeMaker.width):
            tempR = tempR + mazeMaker.maze[row, column] + " "
        print(tempR)


def solveMaze():
    for i in range(len(pathFinder.solutionPath) - 1):
        mario.walkBetween(pathFinder.solutionPath[i], pathFinder.solutionPath[i + 1])


def putMarioAtStart():
    mazeMaker.maze[mazeData.START] = mario.icon


if __name__ == "__main__":
    putMarioAtStart()
    solveMaze()
    display()
