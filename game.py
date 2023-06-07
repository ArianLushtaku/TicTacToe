import pygame
import random
from board import Board
from main import MAIN, GameState

w, h = 800, 800
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Tic-Tac-Toe")

# Create a clock
clock = pygame.time.Clock()

# Game loop
main = MAIN(screen, w, h)
running = True
while running:
    # Set the FPS
    clock.tick(60)

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        main.update()
        match main.game_state:
            case GameState.MainMenu:
                if event.type == pygame.MOUSEBUTTONUP:
                    if main.start_button.rect.collidepoint(event.pos):
                        main.game_state = GameState.GameRunning
                    elif main.quit_button.rect.collidepoint(event.pos):
                        running = False
            case GameState.GameRunning:
                if event.type == pygame.MOUSEBUTTONUP:
                    main.board.draw_board()
            case GameState.GameOver:
                if event.type == pygame.QUIT:
                    running = False
        
            

    # Update the display
    screen.fill((255, 255, 255))
    main.draw()
    
    
    # Draw the marks
    pygame.display.update()

# Quit the game
pygame.quit()
