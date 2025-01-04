import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600

# colors
matte_black = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

# display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# title
title = "Addy Executes - Game 1"
pygame.display.set_caption(title)

# time and fps
clock = pygame.time.Clock()
FPS = 60

# mainloop variable
running = True


# Font
font = pygame.font.SysFont(None, 28)
font_large = pygame.font.SysFont(None, 56)


# Sound effects
pygame.mixer.music.load("Assets/bg.mp3")
pygame.mixer.music.play(-1)

oops_sound = pygame.mixer.Sound("Assets/oops.mp3")
score_sound = pygame.mixer.Sound("Assets/score.wav")

oops_sound.set_volume(1)
score_sound.set_volume(1)


# Score function
score = 0
score_inc_rate = 1


def show_score():
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))




# Game over
game_over = True

def game_over_screen():

    global running
    global game_over, score, slider_X, slider_X_change, ball_X, ball_X_change, ball_Y, ball_Y_change

    game_over_text = font_large.render("Start the game", True, red)
    player_score = font.render("Your score is : "+str(score), True, green)
    press_to_play_text = font.render("Enter to play | Esc to quit", True, white)
    
    screen.blit(game_over_text, (WIDTH/2 - game_over_text.get_width()/2, HEIGHT/2-100))
    if score != 0:
        screen.blit(player_score, (WIDTH/2 - player_score.get_width()/2, HEIGHT/2-20))
    screen.blit(press_to_play_text, (WIDTH/2 - press_to_play_text.get_width()/2, HEIGHT/2+60))

    slider_X_change = 0
    
    if event.type == pygame.KEYDOWN:

        # Continue the game
        if event.key == pygame.K_RETURN:
            game_over = False

            score = 0
            slider_X = WIDTH / 2 - slider_width / 2
            slider_X_change = 0

            ball_X = WIDTH / 2 - ball_width / 2
            ball_Y = HEIGHT / 2 - ball_height / 2
            while ball_X_change == 0:
                ball_X_change = random.randint(-int(ball_speed), int(ball_speed))
            while ball_Y_change == 0:
                ball_Y_change = random.randint(-int(ball_speed), int(ball_speed))
        
        # Quit the game
        if event.key == pygame.K_ESCAPE:
            running = False



# Slider function

slider_color = red

slider_width = 100
slider_height = 10

slider_speed = FPS/6

slider_X = WIDTH / 2 - slider_width / 2
slider_X_change = 0

slider_Y = HEIGHT - slider_height
slider_Y_change = 0

def slider():

    global slider_X, slider_X_change

    slider_X += slider_X_change

    if not game_over:

        if slider_X <= 0:
            slider_X = 0
        elif slider_X >= WIDTH - slider_width:
            slider_X = WIDTH - slider_width

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                slider_X_change = -slider_speed
            if event.key == pygame.K_RIGHT:
                slider_X_change = slider_speed
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                slider_X_change = 0

    pygame.draw.rect(screen, (255, 255, 255), (slider_X, slider_Y, slider_width, slider_height))





# Ball function

ball_loc = pygame.image.load("Assets/ball.png")

ball_width = 64
ball_height = 64

ball_speed = FPS/12

ball_X = WIDTH / 2 - ball_width / 2
ball_X_change = 0
while ball_X_change == 0:
    ball_X_change = random.randint(-int(ball_speed), int(ball_speed))

ball_Y = HEIGHT / 2 - ball_height / 2
ball_Y_change = 0
while ball_Y_change == 0:
    ball_Y_change = random.randint(-int(ball_speed), int(ball_speed))

def ball():

    global ball_X, ball_Y, ball_X_change, ball_Y_change, ball_speed
    global slider_X, slider_X_change
    global score
    global game_over

    if not game_over:
        ball_X += ball_X_change
        ball_Y += ball_Y_change

        if ball_X <= 0:
            ball_X_change = ball_speed
        elif ball_X >= WIDTH - ball_width:
            ball_X_change = -ball_speed

        if ball_Y <= 0:
            ball_Y_change = ball_speed
        elif ball_Y >= HEIGHT - slider_height - ball_height:
            ball_Y_change = -ball_speed

            # Adding score, playing the sound effect & increasing the speed of the ball
            if ball_X+(ball_width/2) >= slider_X and ball_X+(ball_width/2) <= slider_X + slider_width:
                score += score_inc_rate
                ball_speed += 1/3 # speed increases by 1 every 3 times the score increases by 1
                score_sound.play()
            
            else:
                oops_sound.play()
                game_over = True


    screen.blit(ball_loc, (ball_X, ball_Y))






def game():
    
    slider()
    ball()
    show_score()

    if game_over:
        game_over_screen()


# mainloop
while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(matte_black)

    game()


    pygame.display.update()



# quitting the game
pygame.quit()