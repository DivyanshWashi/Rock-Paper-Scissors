import random
import time
import pygame

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")

# Load images
rock_img = pygame.image.load("rock.png")
paper_img = pygame.image.load("paper.png")
scissors_img = pygame.image.load("scissors.png")

# Resize images
rock_img = pygame.transform.scale(rock_img, (150, 150))
paper_img = pygame.transform.scale(paper_img, (150, 150))
scissors_img = pygame.transform.scale(scissors_img, (150, 150))

# Load sounds
click_sound = pygame.mixer.Sound("click.wav")
win_sound = pygame.mixer.Sound("win.wav")
lose_sound = pygame.mixer.Sound("meme_lose.wav")  # Meme sound for losing
draw_sound = pygame.mixer.Sound("draw.wav")
play_again_sound = pygame.mixer.Sound("play_again.wav")
quit_sound = pygame.mixer.Sound("quit.wav")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 100, 255)
GREEN = (100, 255, 100)
RED = (255, 100, 100)

# Font
font = pygame.font.Font(None, 36)

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player, computer):
    if player == computer:
        draw_sound.play()
        return "It's a draw!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        win_sound.play()
        return "You win! 🎉"
    else:
        lose_sound.play()
        return "You lose! 😢"

def draw_text(text, x, y):
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, (x, y))

def draw_buttons():
    pygame.draw.rect(screen, BLUE, (50, 300, 150, 50))
    pygame.draw.rect(screen, BLUE, (225, 300, 150, 50))
    pygame.draw.rect(screen, BLUE, (400, 300, 150, 50))
    draw_text("Rock", 100, 315)
    draw_text("Paper", 275, 315)
    draw_text("Scissors", 440, 315)

def draw_play_again_buttons():
    pygame.draw.rect(screen, GREEN, (150, 300, 150, 50))
    pygame.draw.rect(screen, RED, (325, 300, 150, 50))
    draw_text("Play Again", 165, 315)
    draw_text("Quit", 375, 315)

def show_images(player_choice, computer_choice):
    screen.fill(WHITE)
    images = {"rock": rock_img, "paper": paper_img, "scissors": scissors_img}
    screen.blit(images[player_choice], (50, 100))  # Player's choice
    screen.blit(images[computer_choice], (400, 100))  # Computer's choice
    pygame.display.flip()

def main():
    running = True
    while running:
        player_choice = None
        computer_choice = None
        result = ""
        
        while player_choice is None:
            screen.fill(WHITE)
            draw_buttons()
            draw_text("Rock Paper Scissors! Click a button to play.", 90, 50)
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_sound.play()
                    x, y = pygame.mouse.get_pos()
                    if 50 <= x <= 200 and 300 <= y <= 350:
                        player_choice = "rock"
                    elif 225 <= x <= 375 and 300 <= y <= 350:
                        player_choice = "paper"
                    elif 400 <= x <= 550 and 300 <= y <= 350:
                        player_choice = "scissors"
        
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)
        
        screen.fill(WHITE)
        show_images(player_choice, computer_choice)
        draw_text(result, 230, 270)
        draw_play_again_buttons()
        pygame.display.flip()
        
        play_again = None
        while play_again is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 150 <= x <= 300 and 300 <= y <= 350:
                        play_again_sound.play()
                        play_again = True
                    elif 325 <= x <= 475 and 300 <= y <= 350:
                        quit_sound.play()
                        pygame.time.delay(1000)  # Wait 1 second before quitting
                        pygame.quit()
                        return
    
if __name__ == "__main__":
    main()
