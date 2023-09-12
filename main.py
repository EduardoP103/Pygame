import pygame
import os

pygame.font.init()
pygame.mixer.init()
pygame.init()

# Configuración de la ventana y colores
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Evaluacion!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

# Variable para controlar la visibilidad del menú
show_menu = False

# Función para mostrar u ocultar el menú


def toggle_menu():
    global show_menu
    show_menu = not show_menu


def draw_menu():
    # Dibuja el fondo del menú
    menu_bg = pygame.Surface((WIDTH, HEIGHT))
    menu_bg.set_alpha(128)
    menu_bg.fill(BLACK)
    WIN.blit(menu_bg, (0, 0))

    # Dibuja los botones del menú
    restart_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50)
    exit_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50)

    pygame.draw.rect(WIN, RED, restart_button)
    pygame.draw.rect(WIN, RED, exit_button)

    restart_text = HEALTH_FONT.render("Reiniciar", 1, WHITE)
    exit_text = HEALTH_FONT.render("Exit", 1, WHITE)

    WIN.blit(restart_text, (restart_button.centerx - restart_text.get_width() //
             2, restart_button.centery - restart_text.get_height() // 2))
    WIN.blit(exit_text, (exit_button.centerx - exit_text.get_width() //
             2, exit_button.centery - exit_text.get_height() // 2))


def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)

    red_health_text = HEALTH_FONT.render(
        "Vida: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render(
        "Vida: " + str(yellow_health), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    if show_menu:
        draw_menu()

    pygame.display.update()


def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # LEFT
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:  # RIGHT
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  # UP
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15:  # DOWN
        yellow.y += VEL


def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # LEFT
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:  # RIGHT
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # UP
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15:  # DOWN
        red.y += VEL


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() //
                         2, HEIGHT/2 - draw_text.get_height()/2))

    # Mostrar el botón de reinicio
    WIN.blit(REMATCH_TEXT, (REMATCH_BUTTON.centerx - REMATCH_TEXT.get_width() // 2,
                            REMATCH_BUTTON.centery - REMATCH_TEXT.get_height() // 2))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if REMATCH_BUTTON.collidepoint(mouse_x, mouse_y):
                    reset_game()  # Restablece el juego al hacer clic en el botón de reinicio
                    return  # Sal del bucle


# Botón de reinicio
REMATCH_BUTTON = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50)
REMATCH_TEXT = HEALTH_FONT.render("Jugar otra vez", 1, WHITE)

# Variables globales para las balas y el estado del juego
red_bullets = []
yellow_bullets = []
red_health = 10
yellow_health = 10
game_over = False  # Variable de estado para controlar el reinicio


# Restablecer el juego
def reset_game():
    global red_bullets, yellow_bullets, red_health, yellow_health, red, yellow, game_over
    red_bullets = []
    yellow_bullets = []
    red_health = 10
    yellow_health = 10
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    game_over = False


def main():
    global show_menu, red, yellow, red_health, yellow_health, red_bullets, yellow_bullets, game_over
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)

                if event.key == pygame.K_ESCAPE:
                    toggle_menu()  # Muestra u oculta el menú

            if event.type == RED_HIT:
                red_health -= 1
                if red_health <= 0:
                    game_over = True

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                if yellow_health <= 0:
                    game_over = True

            # Manejar eventos del menú
            if show_menu:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    restart_button = pygame.Rect(
                        WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50)
                    exit_button = pygame.Rect(
                        WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50)

                    if restart_button.collidepoint(mouse_x, mouse_y):
                        show_menu = False
                        reset_game()  # Restablece el juego al hacer clic en el botón de reinicio

                    elif exit_button.collidepoint(mouse_x, mouse_y):
                        pygame.quit()

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(red, yellow, red_bullets, yellow_bullets,
                    red_health, yellow_health)

        if game_over:
            draw_winner("Rojo Gana!" if yellow_health <=
                        0 else "Amarillo Gana!")

    pygame.quit()


if __name__ == "__main__":
    main()
