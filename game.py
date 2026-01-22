import pygame
import sys
from board import COL,ROW,SIZE,SCORE_FEILD,Board
from tetri import Tetrimino,Game_Board
from trimino import L,J,I,O,T,S,Z

FPS = 30

pygame.init()

Main_Window = pygame.display.set_mode(((COL+SCORE_FEILD)*SIZE,ROW*SIZE))

my_tetrimino = Tetrimino()
clock = pygame.time.Clock()

while True:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a and (my_tetrimino.Index_left(my_tetrimino.tetrimino,my_tetrimino.rotation) + my_tetrimino.position) > 0 and not my_tetrimino.Collide_left(my_tetrimino.tetrimino,my_tetrimino.rotation):
                my_tetrimino.position -= 1

            if event.key == pygame.K_d and (my_tetrimino.Index_right(my_tetrimino.tetrimino,my_tetrimino.rotation) + my_tetrimino.position) < COL-1 and not my_tetrimino.Collide_left(my_tetrimino.tetrimino,my_tetrimino.rotation):
                my_tetrimino.position += 1

            if event.key == pygame.K_w:

                # S transform
                if my_tetrimino.tetrimino == S and my_tetrimino.rotation == 1 and my_tetrimino.Index_right(my_tetrimino.tetrimino, my_tetrimino.rotation) + my_tetrimino.position == 9:
                    my_tetrimino.rotation = my_tetrimino.rotation
                elif my_tetrimino.tetrimino == S and my_tetrimino.rotation == 3 and my_tetrimino.Index_right(my_tetrimino.tetrimino, my_tetrimino.rotation) + my_tetrimino.position == 9:
                    my_tetrimino.rotation = my_tetrimino.rotation

                # Z transform
                elif my_tetrimino.tetrimino == Z and my_tetrimino.rotation == 1 and my_tetrimino.Index_right(my_tetrimino.tetrimino, my_tetrimino.rotation) + my_tetrimino.position == 9:
                    my_tetrimino.rotation = my_tetrimino.rotation
                elif my_tetrimino.tetrimino == Z and my_tetrimino.rotation == 3 and my_tetrimino.Index_right(my_tetrimino.tetrimino, my_tetrimino.rotation) + my_tetrimino.position == 9:
                    my_tetrimino.rotation = my_tetrimino.rotation

                # LINE transform
                elif my_tetrimino.tetrimino == I and my_tetrimino.rotation == 1 and my_tetrimino.Index_right(my_tetrimino.tetrimino, my_tetrimino.rotation) + my_tetrimino.position >= 8:
                    my_tetrimino.rotation = my_tetrimino.rotation
                elif my_tetrimino.tetrimino == I and my_tetrimino.rotation == 1 and my_tetrimino.Index_left(my_tetrimino.tetrimino, my_tetrimino.rotation) + my_tetrimino.position == 0:
                    my_tetrimino.rotation = my_tetrimino.rotation
                elif my_tetrimino.tetrimino == I and my_tetrimino.rotation == 3 and my_tetrimino.Index_right(my_tetrimino.tetrimino, my_tetrimino.rotation) + my_tetrimino.position > 8:
                    my_tetrimino.rotation = my_tetrimino.rotation
                elif my_tetrimino.tetrimino == I and my_tetrimino.rotation == 3 and my_tetrimino.Index_left(my_tetrimino.tetrimino, my_tetrimino.rotation) + my_tetrimino.position == 0:
                    my_tetrimino.rotation = my_tetrimino.rotation

                # J transform
                elif my_tetrimino.tetrimino == J and my_tetrimino.rotation == 0 and my_tetrimino.Index_left(my_tetrimino.tetrimino, my_tetrimino.rotation) + my_tetrimino.position == 0:
                    my_tetrimino.rotation = my_tetrimino.rotation
                elif my_tetrimino.tetrimino == J and my_tetrimino.rotation == 2 and my_tetrimino.Index_left(my_tetrimino.tetrimino, my_tetrimino.rotation) + my_tetrimino.position == 0:
                    my_tetrimino.rotation = my_tetrimino.rotation

                # L transform
                elif my_tetrimino.tetrimino == L and my_tetrimino.rotation == 2 and my_tetrimino.Index_left(my_tetrimino.tetrimino, my_tetrimino.rotation) + my_tetrimino.position == 0:
                    my_tetrimino.rotation = my_tetrimino.rotation
                elif my_tetrimino.tetrimino == L and my_tetrimino.rotation == 0 and my_tetrimino.Index_right(my_tetrimino.tetrimino, my_tetrimino.rotation) + my_tetrimino.position == 9:
                    my_tetrimino.rotation = my_tetrimino.rotation

                # T transform
                elif my_tetrimino.tetrimino == T and my_tetrimino.rotation == 1 and my_tetrimino.Index_left(my_tetrimino.tetrimino, my_tetrimino.rotation) + my_tetrimino.position == 0:
                    my_tetrimino.rotation = my_tetrimino.rotation
                elif my_tetrimino.tetrimino == T and my_tetrimino.rotation == 3 and my_tetrimino.Index_right(my_tetrimino.tetrimino, my_tetrimino.rotation) + my_tetrimino.position == 9:
                    my_tetrimino.rotation = my_tetrimino.rotation
                
                # Rotation collided
                elif my_tetrimino.Collide_rotation(my_tetrimino.tetrimino,my_tetrimino.tetrimino):
                    my_tetrimino.rotation = my_tetrimino.rotation

                # normal transform
                else:
                    my_tetrimino.rotation += 1
                if my_tetrimino.rotation > 3:
                    my_tetrimino.rotation = 0
            if event.key == pygame.K_s:
                my_tetrimino.speed += 1

    Main_Window.fill("#ffffff")
    Game_Board.Update(Main_Window)
    my_tetrimino.Draw(Main_Window,my_tetrimino.tetrimino,'red',my_tetrimino.rotation)

    pygame.display.update()