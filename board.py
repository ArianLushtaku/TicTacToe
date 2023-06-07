import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Board:
    def __init__(self, screen, width, height):
        self.board = [['', '', ''],
                      ['', '', ''],
                      ['', '', '']]
        self.player1 = random.choice(['X', 'O'])
        self.player2 = 'O' if self.player1 == 'X' else 'X'
        self.winner = ''
        
        self.screen = screen
        self.width = width
        self.height = height
    
    def make_board(self):
        self.screen.fill(WHITE)
        pygame.draw.line(self.screen, BLACK, (self.width / 3, 0), (self.width / 3, self.height), 5)
        pygame.draw.line(self.screen, BLACK, (2 * self.width / 3, 0), (2 * self.width / 3, self.height), 5)
        pygame.draw.line(self.screen, BLACK, (0, self.height / 3), (self.width, self.height / 3), 5)
        pygame.draw.line(self.screen, BLACK, (0, 2 * self.height / 3), (self.width, 2 * self.height / 3), 5)
    
    def draw_marks(self, board):
        for row in range(3):
            for col in range(3):
                if board[row][col] == 'X':
                    x_pos = col * self.width // 3 + self.width // 6
                    y_pos = row * self.height // 3 + self.height // 6
                    pygame.draw.line(self.screen, BLACK, (x_pos - 40, y_pos - 40), (x_pos + 40, y_pos + 40), 5)
                    pygame.draw.line(self.screen, BLACK, (x_pos + 40, y_pos - 40), (x_pos - 40, y_pos + 40), 5)
                elif board[row][col] == 'O':
                    x_pos = col * self.width // 3 + self.width // 6
                    y_pos = row * self.height // 3 + self.height // 6
                    pygame.draw.circle(self.screen, BLACK, (x_pos, y_pos), 40, 5)
            
    def playerTurn(self):
        self.player1 = 'O' if self.player1 == 'X' else 'X'

    def checkWin(self):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != '':
                self.winner = self.board[row][0]
                return True

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '':
                self.winner = self.board[0][col]
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            self.winner = self.board[0][0]
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            self.winner = self.board[0][2]
            return True

        return False
        
    def checkTie(self):
        if self.checkWin() == False:
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == '':
                        return False
            return True
            
    def checkState(self):
        if self.checkWin:
            return False
        if self.checkTie:
            return False
        return True
            
        
        
    def draw_board(self):
            pos = pygame.mouse.get_pos()
            if pos[0] < self.width / 3:
                col = 0
            elif pos[0] < 2 * self.width / 3:
                col = 1
            else:
                col = 2
            if pos[1] < self.height / 3:
                row = 0
            elif pos[1] < 2 * self.height / 3:
                row = 1
            else:
                row = 2
            if self.board[row][col] == '':
                self.board[row][col] = self.player1
                self.playerTurn()
        
    
    def reset(self):
        self.board = [['', '', ''],
                      ['', '', ''],
                      ['', '', '']]
        self.player1 = random.choice(['X', 'O'])
        self.player2 = 'O' if self.player1 == 'X' else 'X'
        self.winner = ''