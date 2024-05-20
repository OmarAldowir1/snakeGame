import pygame
import sys
import random
from pygame import Vector2

pygame.init()  # pygame start


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

        self.head_up = pygame.image.load('/Users/omaraldowir/Desktop/Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('/Users/omaraldowir/Desktop/Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('/Users/omaraldowir/Desktop/Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('/Users/omaraldowir/Desktop/Graphics/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('/Users/omaraldowir/Desktop/Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('/Users/omaraldowir/Desktop/Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('/Users/omaraldowir/Desktop/Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('/Users/omaraldowir/Desktop/Graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('/Users/omaraldowir/Desktop/Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load(
            '/Users/omaraldowir/Desktop/Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('/Users/omaraldowir/Desktop/Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('/Users/omaraldowir/Desktop/Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('/Users/omaraldowir/Desktop/Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('/Users/omaraldowir/Desktop/Graphics/body_bl.png').convert_alpha()

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if (previous_block.x == -1 and next_block.y == -1) or (
                            previous_block.y == -1 and next_block.x == -1):
                        screen.blit(self.body_tl, block_rect)
                    elif (previous_block.x == -1 and next_block.y == 1) or (
                            previous_block.y == 1 and next_block.x == -1):
                        screen.blit(self.body_bl, block_rect)
                    elif (previous_block.x == 1 and next_block.y == -1) or (
                            previous_block.y == -1 and next_block.x == 1):
                        screen.blit(self.body_tr, block_rect)
                    elif (previous_block.x == 1 and next_block.y == 1) or (previous_block.y == 1 and next_block.x == 1):
                        screen.blit(self.body_br, block_rect)

    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down


class TRAP:
    def __init__(self):
        self.randomize()

    def draw_trap(self):
        trap_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(trap_image, trap_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)  # rand places of the fruit
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.traps = []  # Initialize traps list

    def update(self):
        self.snake.move_snake()
        self.check_collision()  # calling the method of checking on the fruit if it is eaten
        self.check_fail()  # calling a method that tells if the snake hit the wall

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        for trap in self.traps:
            trap.draw_trap()  # Draw each trap
        self.draw_score()

    def draw_score(self):
        score_tex = str(len(self.snake.body)-3)
        score_surface = game_font.render(score_tex,True,(56,74,12))
        score_x = int(cell_size*cell_number-60)
        score_y = int(cell_size*cell_number-40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        apple_rect = apple.get_rect(midright= (score_rect.left,score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width + 6,apple_rect.height)

        pygame.draw.rect(screen,(167,209,61),bg_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(apple,apple_rect)
        pygame.draw.rect(screen,(56,74,12),bg_rect,2)

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:  # check if the snake is eating fruit
            self.fruit.randomize()
            self.snake.new_block = True
            # Place a trap every 5 fruits eaten
            if (len(self.snake.body) - 3) % 5 == 0:
                trap = TRAP()
                # Ensure trap doesn't overlap with the snake body or existing traps
                while trap.pos in self.snake.body or any(trap.pos == t.pos for t in self.traps):
                    trap.randomize()
                self.traps.append(trap)
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()
    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

        # Check if snake hits a trap
        for trap in self.traps:
            if trap.pos == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()

    def draw_grass(self):
        grass_color = (167, 209, 61)
        for row in range(cell_number):
            for col in range(cell_number):
                if (row + col) % 2 == 0:
                    grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                    pygame.draw.rect(screen, grass_color, grass_rect)


cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_size * cell_number))  # window
apple = pygame.image.load('/Users/omaraldowir/Desktop/Graphics/apple.png').convert_alpha()
trap_image = pygame.image.load('/Users/omaraldowir/Desktop/Graphics/trap.png').convert_alpha()
clock = pygame.time.Clock()  # consist frames = 60
main_game = MAIN()

try:
    game_font = pygame.font.Font('/Users/omaraldowir/Desktop/font/PoetsenOne-Regular.ttf', 25)
except FileNotFoundError:
    print("Font file not found, using default font.")
    game_font = pygame.font.SysFont(None, 25)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)

    screen.fill((175, 215, 70))
    main_game.draw_elements()
    pygame.display.update()

    clock.tick(60)
