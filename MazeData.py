class MazeData:
    def __init__(self):
        self.WALL = "#"
        self.PATH = " "
        self.WENTPATH = "~"
        self.MARIO = "@"
        self.PATHTUPLE = (
            (1, 13, 32),
            (2, 10, 14), (2, 18, 19), (2, 31, 32),
            (3, 4, 8), (3, 11, 12), (3, 18, 19), (3, 24, 25), (3, 31, 36),
            (4, 3, 12), (4, 22, 25),
            (5, 11, 12), (5, 18, 25),
            (6, 11, 32),
            (7, 16, 19), (7, 27, 33),
            (8, 3, 22), (8, 30, 31),
            (9, 10, 15), (9, 30, 32),
            (10, 13, 15), (10, 24, 32),
            (11, 13, 19), (11, 24, 25),
            (12, 9, 15), (12, 24, 30),
            (13, 24, 25),
            (14, 8, 25),
            (15, 0, 9), (15, 15, 30),
            (16, 0, 1)
        )
        self.START = (16, 0)
        self.END = (3, 35)