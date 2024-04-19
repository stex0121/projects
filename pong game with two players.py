import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 1280, 720

FONT = pygame.font.SysFont('Consolas', int(WIDTH / 20))
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong_game')
CLOCK = pygame.time.Clock()
player1_score = 0
player2_score = 0

player1 = pygame.Rect(WIDTH - 110, HEIGHT / 2 - 50, 10, 100)
player2 = pygame.Rect(110, HEIGHT / 2 - 50, 10, 100)

ball = pygame.Rect(WIDTH / 2 - 10, HEIGHT / 2 - 10, 20, 20)
x_speed, y_speed = 1, 1

while True:
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_UP]:
        if player1.top > 0:
            player1.top -= 2
    if key_pressed[pygame.K_DOWN]:
        if player1.bottom < HEIGHT:
            player1.bottom += 2

    if key_pressed[pygame.K_w]:
        if player2.top > 0:
            player2.top -= 2
    if key_pressed[pygame.K_s]:
        if player2.bottom < HEIGHT:
            player2.bottom += 2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if ball.y >= HEIGHT:
        y_speed = -1
    if ball.y <= 0:
        y_speed = 1
    if ball.x <= 0:
        player1_score += 1
        ball.center = (WIDTH / 2, HEIGHT / 2)
        x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])
    if ball.x >= WIDTH:
        player2_score += 1
        ball.center = (WIDTH / 2, HEIGHT / 2)
        x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])

    if player1.colliderect(ball) or player2.colliderect(ball):
        x_speed *= -1

    player1_score_text = FONT.render(str(player1_score), True, 'white')
    player2_score_text = FONT.render(str(player2_score), True, 'white')
    ball.x += x_speed * 2
    ball.y += y_speed * 2

    SCREEN.fill('black')
    pygame.draw.rect(SCREEN, 'white', player1)
    pygame.draw.rect(SCREEN, 'white', player2)
    pygame.draw.circle(SCREEN, 'white', ball.center, 10)
    SCREEN.blit(player1_score_text, (WIDTH / 2 + 50, 50))
    SCREEN.blit(player2_score_text, (WIDTH / 2 - 50, 50))
    pygame.display.update()
    CLOCK.tick(300)