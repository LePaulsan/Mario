from Node import Node


class NodeListCreator:
    def __init__(self, maze):
        self.maze = maze

    def createNodeList(self):
        nodeList = []
        for i in range(self.maze.height):
            for j in range(self.maze.width):
                if self.maze.isNode(i, j):
                    nodeList.append(Node((i, j)))
        return nodeList