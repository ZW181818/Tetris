import pygame
import numpy as np

COL = 10 #列
ROW = 18 #行
SIZE = 45
SCORE_FEILD = 6
COLOR_NONE = '#3c3c3c'

class Board():
    def __init__(self):
        super().__init__()
        self.board = np.zeros((COL,ROW))

    def Load_Game(self,surface):
        for j in range(COL):
            for i in range(ROW):
                if self.board[j][i] == 0:
                    pygame.draw.rect(surface,COLOR_NONE,(j*SIZE,i*SIZE,SIZE-1,SIZE-1))
                if self.board[j][i] == 1:
                    pygame.draw.rect(surface,'red',(j*SIZE,i*SIZE,SIZE-1,SIZE-1))
    
    def Update(self,surface):
        self.Load_Game(surface)