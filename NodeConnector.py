from dictFunctions import (addThisToDicOfThat,
                           getNodeIdWithLoc)


class NodeConnector:
    def __init__(self, maze, nodeList):
        self.maze = maze
        self.nodeList = nodeList
        self.typeRow = "row"
        self.typeColumn = "column"

    def combinedListOfNodePairs(self):
        return self.createListOfNodePairs(self.typeRow) + self.createListOfNodePairs(self.typeColumn)

    def createListOfNodePairs(self, sort_direction):
        edges = []
        for key, value in self.createDicWithNode(sort_direction).items():
            if len(value) - 1 > 0:
                edges = edges + self.connectWithNearbyNode(sort_direction, value, key)
        return edges

    def createDicWithNode(self, sort_direction):
        return dict(sorted(self.convertListOfNodeToDicOfSet(sort_direction).items()))

    def convertListOfNodeToDicOfSet(self, sort_direction):
        if sort_direction == self.typeRow:
            dic = {}
            for y, x in [nodeLoc.loc for nodeLoc in self.nodeList]:
                addThisToDicOfThat(y, x, dic)
            return dic

        elif sort_direction == self.typeColumn:
            dic = {}
            for y, x in [nodeLoc.loc for nodeLoc in self.nodeList]:
                addThisToDicOfThat(x, y, dic)
            return dic

    def connectWithNearbyNode(self, sort_direction, value, key):
        temp = []
        for i in range(len(value) - 1):
            if self.haveANeighboorNode(sort_direction, key, value, i):
                temp.append(self.nearbyNodeAt(sort_direction, key, value, i))
        return temp

    def haveANeighboorNode(self, sort_direction, key, value, i):
        if sort_direction == self.typeRow:
            return self.maze.getNeighboorsDic(key, value[i])["right"]
        elif sort_direction == self.typeColumn:
            return self.maze.getNeighboorsDic(value[i], key)["back"]

    def nearbyNodeAt(self, sort_direction, key, value, i):
        if sort_direction == self.typeRow:
            return getNodeIdWithLoc((key, value[i]), self.nodeList), getNodeIdWithLoc((key, value[i + 1]), self.nodeList)
        elif sort_direction == self.typeColumn:
            return getNodeIdWithLoc((value[i], key), self.nodeList), getNodeIdWithLoc((value[i + 1], key), self.nodeList)