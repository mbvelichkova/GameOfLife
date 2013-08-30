import pygame
import configs
from game_of_life import GameOfLife, Cell
from settings import Settings
from vector import Vec2D


class GUIGameOfLife:
    def __init__(self, settings=Settings()):
        pygame.init()
        self.generation = {}
        self.game = GameOfLife(self.generation, settings)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((configs.SCREENWIDTH, configs.SCREENHEIGHT))
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill(configs.BLACK)
        pygame.display.set_caption('Game of Life')

        while self.play_game():
            pass

    def play_game(self):
        while True:
            pygame.time.wait(1000)
            self.clock.tick(10)
            self.draw_cells()
            pygame.display.update()
            for event in pygame.event.get():
                print(event)
                escape = event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == escape:
                    pass
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.restart()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mousebuttondown = True
                    while mousebuttondown:
                        pos = pygame.mouse.get_pos()
                        self.new_cell(Vec2D(pos[0]/configs.PIXEL_SIZE, pos[1]/configs.PIXEL_SIZE))
                        self.game = GameOfLife(self.generation)
                        self.draw_cells()
                        pygame.display.update()

                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONUP:
                                mousebuttondown = False
            self.generation = self.game.next_generation()
            self.game = GameOfLife(self.generation)

    def draw_cells(self):
        self.screen.fill(configs.BLACK)
        for coords, cell in self.game.alive_cells.items():
            if cell.new_born:
                color = configs.GREEN
            else:
                color = configs.WHITE
            x, y = coords.x*configs.PIXEL_SIZE, coords.y*configs.PIXEL_SIZE
            pygame.draw.rect(self.screen, color, (x, y, configs.PIXEL_SIZE, configs.PIXEL_SIZE))

    def new_cell(self, coords):
        cell = {coords: Cell(True)}
        self.generation.update(cell)

    def restart(self):
        self.generation = {}
        self.game = GameOfLife(self.generation)
        self.screen.fill(configs.BLACK)
        pygame.display.update()
