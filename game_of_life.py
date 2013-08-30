from settings import Settings

class GameOfLife:
 #   STAY_ALIVE = [2, 3]
#    REPRODUCE = [3]
    NEIGHBOUR_CELLS = [(-1, 1), (0, 1), (1, 1),
                       (-1, 0)        , (1, 0),
                       (-1, -1),(0, -1),(1, -1)]

    def __init__(self, cells, settings = Settings()):
        self.settings = settings
        self.alive_cells = {cell_coords: Cell(True) for cell_coords in cells.keys()}

    def next_generation(self):
        next_generation = self.stable_cells()
        new_born = self.new_born()
        next_generation.update(new_born)
        return next_generation
        
    def stable_cells(self):      
        return {cell: Cell(False) for cell in self.alive_cells.keys() if self.will_servive(cell)}

    def new_born(self):
        new_born = {}
        for cell in self.alive_cells.keys():
            for neighbour in self.neighbours_of(cell):
                if self.will_be_born(neighbour):
                    new_born[neighbour] = Cell(True)
        return new_born

    def will_servive(self, cell_coords):
        if self.number_of_alive_neighbours(cell_coords) in self.settings.cell_stay_alive_list:
            return True
        else:
            return False

    def will_be_born(self, cell_coords):
        if self.number_of_alive_neighbours(cell_coords) in self.settings.reproduce_cell_list:
            return True
        else:
            return False

    def neighbours_of(self, cell_coords):
        x, y = cell_coords
        return [(x + position[0], y + position[1]) for position in self.NEIGHBOUR_CELLS]

    def number_of_alive_neighbours(self, cell_coords):
        count = 0
        for neighbour in self.neighbours_of(cell_coords):
            if self.is_alive(neighbour):
                count += 1 
        return count
    
    def is_alive(self, cell_coords):
        return cell_coords in self.alive_cells.keys()

class Cell:
    def __init__(self, new_born):
        self.new_born = new_born
        
        