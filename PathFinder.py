from Stack import Stack
from dictFunctions import (getNodeIdWithLoc,
                           getNodeLocWithId)


class PathFinder:
    def __init__(self, graph, start, end):
        self.graph = graph.graph
        self.traversedStack = Stack()
        self.wentNode = set()
        self.reachedTheEnd = False
        self.takeStepFormTo(getNodeIdWithLoc(start, graph.nodeList), getNodeIdWithLoc(end, graph.nodeList))
        self.solutionPath = [getNodeLocWithId(node, graph.nodeList) for node in self.traversedStack.items]

    # This function traverse the graph, it is the best it can be for me now so it'll stay
    def takeStepFormTo(self, start, end):
        if start in self.wentNode:
            return
        self.traversedStack.push(start)
        self.wentNode.add(start)

        if start == end:
            self.reachedTheEnd = True
            return

        for node in self.graph[start]:
            if self.reachedTheEnd:
                return
            self.takeStepFormTo(node, end)
            if self.reachedTheEnd:
                return

        self.traversedStack.pop()
        return
