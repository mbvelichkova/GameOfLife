import unittest
from vector import Vec2D
from game_of_life import GameOfLife, Cell

class CellTest(unittest.TestCase):
    def test_new_born_cell(self):
        new_born_cell = Cell(True)
        self.assertEqual(new_born_cell.new_born, True)

    def test_old_cell(self):
        old_cell = Cell(False)
        self.assertEqual(old_cell.new_born, False)

class GameOfLifeTest(unittest.TestCase):
    def setUp(self):
        self.game = GameOfLife({(0, 0) : Cell(True), (0, 1) : Cell(True),
                                (1, 0) : Cell(True), (3, 3) : Cell(True) })

    def test_alive_cell_when_game_is_set_up(self):
        self.assertEqual(self.game.is_alive((1, 0)), True)
        self.assertEqual(self.game.is_alive((1, 1)), False)

    def test_number_of_alive_neighbours(self):
        self.assertEqual(self.game.number_of_alive_neighbours((0, 0)), 2)
        self.assertEqual(self.game.number_of_alive_neighbours((1, 1)), 3)
        self.assertEqual(self.game.number_of_alive_neighbours((4, 0)), 0)

    def test_neighbours_of(self):
        self.assertEqual(sorted(self.game.neighbours_of((0, 0))), sorted([(-1, -1),(-1, 0),(-1, 1),
                                                                          (0, -1),        (0, 1),
                                                                          (1, -1),(1, 0),(1, 1)]))
    def test_will_be_born(self):
        self.assertEqual(self.game.will_be_born((1, 1)), True)
        self.assertEqual(self.game.will_be_born((0, 1)), False)
    
    def test_will_servive(self):
        self.assertEqual(self.game.will_servive((0, 1)), True)
        self.assertEqual(self.game.will_servive((3, 3)), False)
    
    def test_stable_cells(self):
        stable_cells = self.game.stable_cells()
        self.assertEqual(sorted(stable_cells.keys()), sorted([(0, 0), (0, 1), (1, 0)]))
        self.assertEqual(stable_cells[(0, 0)].new_born, False)

    def test_new_born_cells(self):
        new_born_cells = self.game.new_born()
        self.assertEqual(sorted(new_born_cells.keys()), [(1, 1)])
        self.assertEqual(new_born_cells[(1, 1)].new_born, True)

    def test_next_generation(self):
        next_generation = self.game.next_generation()
        self.assertEqual(sorted(next_generation.keys()), sorted([(0, 0), (0, 1), (1, 0), (1, 1)]))
        
        game = GameOfLife(next_generation)
        
        
