import numpy as np


class MazeMaker:
    def __init__(self, wallIcon, pathIcon, pathTuple, start, end):
        self.width = 36
        self.height = 17
        self.start = start
        self.end = end

        self.pathIcon = pathIcon
        self.maze = self.createMaze(wallIcon, pathTuple)

    def createMaze(self, wallIcon, pathTuple):
        blankMaze: list = [wallIcon * self.width for _ in range(self.height)]
        for row, start, end in pathTuple:
            blankMaze[row] = self.carvePath(blankMaze[row], start, end)
        return self.convertStringListToNumpyArray(blankMaze)

    def carvePath(self, row, start, end):
        startOrEndOutOfWidth = start < 0 or end > self.width
        if startOrEndOutOfWidth:
            print("You idiot, index out of range!")
            return

        if start >= end:
            print("Why the fuck is start larger or equal end?!")
            return

        row = self.replaceCellsInRowWithIcon(row, self.pathIcon, start, end)
        return row

    @staticmethod
    def replaceCellsInRowWithIcon(row, icon, start, end):
        return row[:start] + icon * (end - start) + row[end:]

    def isPath(self, yLoc, xLoc):
        cellInHeightRange = 0 <= yLoc < self.height
        cellInWidthRange = 0 <= xLoc < self.width
        if not cellInHeightRange or not cellInWidthRange:
            print("Hey, what the fuck is this. One of these numer is out of range of the table")
            return None

        return self.maze[yLoc, xLoc] == self.pathIcon

    def isCorner(self, yLoc, xLoc):
        neighboor = self.getNeighboorsDic(yLoc, xLoc)
        hasHorizontalNeighboor = neighboor["left"] or neighboor["right"]
        hasVerticalNeighboor = neighboor["front"] or neighboor["back"]
        return hasHorizontalNeighboor and hasVerticalNeighboor

    def isNode(self, y, x):
        return self.isPath(y, x) and (self.isCorner(y, x) or (y, x) == self.start or (y, x) == self.end)

    # If feed y and x in directly, isPath function will return error if y, x in border
    # so this function gonna stay
    def getNeighboorsDic(self, yLoc, xLoc):
        # default value of neighboor is False
        neighboors = {
            "front": False,
            "back": False,
            "left": False,
            "right": False
        }
        # if node is not on the border then check if there is there is path near it
        # if on border then don't check outside that border and remain False     
        if yLoc != 0:
            neighboors["front"] = self.isPath(yLoc - 1, xLoc)
        if yLoc != self.height - 1:
            neighboors["back"] = self.isPath(yLoc + 1, xLoc)
        if xLoc != 0:
            neighboors["left"] = self.isPath(yLoc, xLoc - 1)
        if xLoc != self.width - 1:
            neighboors["right"] = self.isPath(yLoc, xLoc + 1)

        return neighboors

    # convert a list of list to numpy array
    @staticmethod
    def convertStringListToNumpyArray(lst):
        return np.array([[item for item in string] for string in lst])
