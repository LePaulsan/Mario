class Mario:
    def __init__(self, maze, wentPath, icon, loc):
        self.maze = maze
        self.wentPath = wentPath
        self.icon = icon
        self.loc = loc

    def takeStep(self, y, x):
        self.maze[self.loc] = self.wentPath
        self.maze[y, x] = self.icon
        self.loc = (y, x)

    # this function suck but fuck it i'm done refactoring
    def walkBetween(self, node1, node2):
        vel = (node2[0] - node1[0], node2[1] - node1[1])
        if vel[0] != 0:
            if vel[0] == 1:
                self.takeStep(node1[0] + 1, node1[1])
                return
            if vel[0] > 1:
                for i in range(vel[0]):
                    self.takeStep(node1[0] + i + 1, node1[1])
                return
            if vel[0] == -1:
                self.takeStep(node1[0] - 1, node1[1])
                return
            if vel[0] < -1:
                for i in range(-vel[0]):
                    self.takeStep(node1[0] - i - 1, node1[1])
                return

        elif vel[1] != 0:
            if vel[1] == 1:
                self.takeStep(node1[0], node1[1] + 1)
                return
            if vel[1] > 1:
                for i in range(vel[1]):
                    self.takeStep(node1[0], node1[1] + i + 1)
                return
            if vel[1] == -1:
                self.takeStep(node1[0], node1[1] - 1)
                return
            if vel[1] < -1:
                for i in range(-vel[1]):
                    self.takeStep(node1[0], node1[1] - i - 1)
                return