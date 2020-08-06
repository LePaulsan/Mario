from NodeListCreator import NodeListCreator
from NodeConnector import NodeConnector
from dictFunctions import addThisToDicOfThat


class Graph:
    def __init__(self, maze):
        self.maze = maze
        self.nodeList = NodeListCreator(maze).createNodeList()
        self.graph = self.createGraph(NodeConnector(maze, self.nodeList).combinedListOfNodePairs())

    @staticmethod
    def createGraph(node_connection):
        tempD = {}
        for node0, node1 in node_connection:
            addThisToDicOfThat(node0, node1, tempD)
            addThisToDicOfThat(node1, node0, tempD)
        return tempD
