import numpy as np

class Maze:
    def __init__(self, wall_icon, path_icon, visited_icon, paths_tuple, start, end):
        self.size = (17, 36)
        self.width = self.size[1]
        self.height = self.size[0]
        self.wall_icon = wall_icon
        self.path_icon = path_icon
        self.visited_icon = visited_icon

        self.paths_tuple = paths_tuple
        self.start = start
        self.end = end

        self.maze = self.create_maze()

    def create_maze(self):
        maze = self.create_maze_as_list(self.wall_icon, self.width, self.height)
        return self.convert_string_list_to_numpy_matrix(maze)

    def create_maze_as_list(self, wall_icon, width, height):        
        maze = self.create_blank_maze_as_list(wall_icon, width, height)
        for path in self.paths_tuple:
            maze = self.draw_path_on_maze(maze, path[0], path[1], path[2])
        return maze

    @staticmethod
    def create_blank_maze_as_list(wall_icon, width, height):
        blankRow = wall_icon * width
        blankMaze = [blankRow for row in range(height)]
        return blankMaze

    def draw_path_on_maze(self, table, row, start, end):
        if self.is_start_or_end_out_of_range(self.width, start, end): return    
        if self.is_start_bigger_than_end(start, end): return

        table[row] = self.replace_cells_of_row_between(table[row], start, end, self.path_icon)
        return table
    
    @staticmethod
    def is_start_or_end_out_of_range(width, start, end):
        start_or_end_out_of_range = start < 0 or end > width
        if start_or_end_out_of_range:
            print("You idiot, index out of range!")
            return True
        return False

    @staticmethod
    def is_start_bigger_than_end(start, end):
        if start >= end:
            print("Why the fuck is start >= end?!")
            return True
        return False
    
    @staticmethod
    def replace_cells_of_row_between(row, start, end, icon):
        return row[:start] + icon * (end - start) + row[end:]

    def convert_string_list_to_numpy_matrix(self, list_of_string):
        nested_list = self.convert_string_list_to_nested_list(list_of_string)
        return np.array(nested_list)

    @staticmethod
    def convert_string_list_to_nested_list(list_of_string):
        return [list(row) for row in list_of_string]

    def get_neighboor_dic(self, y, x):
        neighboor = {}        
        neighboor["front"] = self.is_path(y - 1, x)
        neighboor["back"] = self.is_path(y + 1, x)
        neighboor["left"] = self.is_path(y, x - 1)
        neighboor["right"] = self.is_path(y, x + 1)
        return neighboor

    # I have no idea why i write this function this way but this may be the right way to write this
    # def get_neighboor_dic(self, y, x):
    #     on_top_border = y == 0
    #     on_bottom_border = y == self.height - 1
    #     on_left_border = x == 0
    #     on_right_border = x == self.width - 1

    #     neighboor = {}        
    #     if on_top_border:
    #         neighboor["front"] = False
    #     else: 
    #         neighboor["front"] = self.is_path(y - 1, x)

    #     if on_bottom_border:
    #         neighboor["back"] = False
    #     else: 
    #         neighboor["back"] = self.is_path(y + 1, x)

    #     if on_left_border:
    #         neighboor["left"] = False
    #     else: 
    #         neighboor["left"] = self.is_path(y, x - 1)

    #     if on_right_border:
    #         neighboor["right"] = False
    #     else: 
    #         neighboor["right"] = self.is_path(y, x + 1)

    #     return neighboor

    # return False used to be return None this may cause unnotace bug 
    def is_path(self, y, x):
        if self.is_cell_out_of_table_error(y, x):
            return False
        return self.maze[y, x] == self.path_icon

    # return False used to be return None this may cause unnotace bug 
    def is_wall(self, y, x):
        if self.is_cell_out_of_table_error(y, x):
            return False
        return self.maze[y, x] == self.wall_icon
        
    def is_cell_out_of_table_error(self, y, x):
        if self.cell_out_of_table(y, x):
            print("Hey, what the fuck is this. One of these numer is out of range of the table")
            return True
        return False

    def cell_out_of_table(self, y, x):
        return not (0 <= y < self.size[0]) or not (0 <= x < self.size[1])