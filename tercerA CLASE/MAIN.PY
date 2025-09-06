import pygame, sys, random
from pygame.math import Vector2

pygame.init()

BG_COLOR = (173, 204, 96)
SNAKE_COLOR = (43, 52, 24)

cell_size = 30
number_of_cells = 25

class Food:
    def _init_(self):
    self.position = Vector2(5. 6)
    
    def draw(self):
        food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, SNAKE_COLOR, food_rect)
        
    def generate_random_pos(self):
        x = randint(0, number_of_cells - 1)
        y = randint(0, number_of_cells - 1)
        position = Vector2(x,y)
        return position
    
class Snake:
    def _init_(self):
        self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]
        self.direction = Vector2(1, 0)
        
    def draw(self):
        for segment in self.body:
            segment_rect = pygame.Rect(segment.x * cell_size, segment.y * cell_size, cell_size)
            pygame.draw.rect(screen, SNAKE_COLOR, segment_rect, 0, 7)
            
    def update(self):
        self.body.insert(0, self.body[0] + self.direction)
        self.body.pop()

screen = pygame.display.set_mode((cell_size * number_of_cells, cell_size * number_of_cells))
pygame.display.set_mode("Retro Snake")

clock = pygame.time.Clock()

food = Food()

snake = Snake()



while True:
    for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    if event.type == SNAKE_UPDATE:
        snake.update()
        
        
    screen.fill(BG_COLOR)
    food.draw()
    
    pygame.display.update()
    clock.tick(60)
    
    
    
    
    
    
    
    
    
    
    