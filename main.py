from board import Board
from enum import Enum
from button import Button
import pygame

class GameState(Enum):
    MainMenu = 0
    GameRunning = 1
    GameOver = 2

class MAIN ():
    def __init__(self, screen, w, h):
        self.board = Board(screen,w,h)
        self.game_state = GameState.MainMenu
        self.start_button = Button(
            w // 2 - 75, h // 2 -100, 150, 50, "Start",
            (255, 255, 255), (0, 0, 0) )
        self.quit_button = Button(
            w // 2 - 75, h // 2 + 25, 150, 50, "Quit",
            (255, 255, 255), (0, 0, 0) )
        self.highlighted_button = self.start_button
        self.screen = screen
        self.w = w
        self.h = h

        
    def update(self):
        self.checkGameState()
    
    def draw(self):
        match self.game_state:
            case GameState.MainMenu:
                self.start_button.draw(self.screen)
                self.quit_button.draw(self.screen)
            case GameState.GameRunning:
                self.board.make_board()
                self.board.draw_marks(self.board.board)
            case GameState.GameOver:
                self.board.make_board()
                self.board.draw_marks(self.board.board)
                
                if self.board.checkWin():
                    font = pygame.font.Font(None, 36)
                    text_surface = font.render("Game Over! {} WON!".format(self.board.winner), True, (255, 0, 0))
                    text_rect = text_surface.get_rect(center=(self.w // 2, self.h // 2))
                    
                    self.screen.blit(text_surface, text_rect)
                elif self.board.checkTie():
                    font = pygame.font.Font(None, 36)
                    text_surface = font.render("IT'S A TIE!!", True, (255, 0, 0))
                    text_rect = text_surface.get_rect(center=(self.w // 2, self.h // 2))
                    
                    self.screen.blit(text_surface, text_rect)
                    
                
        
    def checkGameState(self):
        if self.game_state == GameState.MainMenu:
            for button in [self.start_button, self.quit_button]:
                if button == self.highlighted_button:
                    button.highlighted = True
                else:
                    button.highlighted = False
                button.draw(self.screen)
                
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                    self.highlighted_button = self.start_button
                elif keys[pygame.K_DOWN]:
                    self.highlighted_button = self.quit_button
                elif keys[pygame.K_RETURN]:
                    if self.highlighted_button == self.start_button:
                        self.reset_game()
                        self.game_state = GameState.GameRunning
                    elif self.highlighted_button == self.quit_button:
                        exit()
                        
        elif self.game_state == GameState.GameRunning:
            if self.board.checkWin():
                self.game_state = GameState.GameOver
            elif self.board.checkTie():
                self.game_state = GameState.GameOver
                
        elif self.game_state == GameState.GameOver:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    self.reset_game()
                    self.game_state = GameState.GameRunning
                
                
            
    
    def reset_game(self):
        self.board.reset()