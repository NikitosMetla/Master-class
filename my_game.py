import pygame
import random

# Инициализация Pygame
pygame.init()

# Параметры экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра: избегай врагов")

# Цвета
BLUE = (0, 128, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Параметры игрока
player_width, player_height = 50, 50
player_x, player_y = WIDTH // 2, HEIGHT // 2
player_speed = 5

# Параметры врагов
enemy_width, enemy_height = 50, 50
enemy_speed = 3
enemies = []

# Создание врагов
for i in range(5):
    enemy_x = random.randint(0, WIDTH - enemy_width)
    enemy_y = random.randint(0, HEIGHT - enemy_height)
    enemies.append([enemy_x, enemy_y])

# Игровой цикл
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получение состояния клавиш
    keys = pygame.key.get_pressed()

    # Управление игроком
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Ограничение игрока рамками экрана
    if player_x < 0:
        player_x = 0
    if player_x > WIDTH - player_width:
        player_x = WIDTH - player_width
    if player_y < 0:
        player_y = 0
    if player_y > HEIGHT - player_height:
        player_y = HEIGHT - player_height

    # Рисуем игрока
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    pygame.draw.rect(screen, BLUE, player_rect)

    # Обновление и рисование врагов
    for enemy in enemies:
        enemy[1] += enemy_speed  # Движение врагов вниз
        if enemy[1] > HEIGHT:  # Если враг выходит за нижнюю границу экрана
            enemy[0] = random.randint(0, WIDTH - enemy_width)  # Переместить врага на случайную позицию сверху
            enemy[1] = -enemy_height

        enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_width, enemy_height)
        pygame.draw.rect(screen, RED, enemy_rect)

        # Проверка на столкновение
        if player_rect.colliderect(enemy_rect):
            print("Game Over!")
            running = False

    # Обновление экрана
    pygame.display.flip()

    # Ограничение FPS
    clock.tick(60)

pygame.quit()
