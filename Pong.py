# ====================== imports =======================

import pygame

# ======================================================
# ===================== game setup =====================

pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong: FPS: 0")

clock = pygame.time.Clock()
current_FPS = 0
FPS_limit = 60

ball_position = pygame.Vector2(screen_width / 2, screen_height / 2)
ball_speed = 400
ball_size = 20
ball_colided_x = False
ball_colided_y = False

pong_size = pygame.Vector2(20, 100)
left_pong_position = pygame.Vector2(10, screen_height / 2)
right_pong_position = pygame.Vector2(screen_width - (pong_size.x + left_pong_position.x), screen_height / 2)
pong_speed = 400
right_pong_move = True

running = True

# ======================================================
# ======================= game =========================

while running:

    # ======================================================
    # ======================= setup ========================

    delta_time = clock.tick(FPS_limit) / 1000
    keys=pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # ======================================================
    # ==================== main script =====================

    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(left_pong_position.x, left_pong_position.y - (pong_size.y / 2), pong_size.x, pong_size.y))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(right_pong_position.x, right_pong_position.y - (pong_size.y / 2), pong_size.x, pong_size.y))
    pygame.draw.circle(screen, (255, 255, 255), ball_position, ball_size)

    # ======================================================
    # ==================== ball script =====================  

    # move by X
    if ball_colided_x and not ball_position.x <= ball_size:
        ball_position.x -= ball_speed * delta_time
    elif not ball_colided_x and not ball_position.x >= (screen_width - ball_size):
        ball_position.x += ball_speed * delta_time

    if ball_position.x <= ball_size or ball_position.x >= (screen_width - ball_size):
        screen.fill((0, 0, 0))
        lose_text = (pygame.font.Font(None, 128)).render("GAME OVER", True, (255, 100, 100))
        screen.blit(lose_text, lose_text.get_rect(center=(screen_width / 2, screen_height / 2)))

    # move by Y
    if ball_colided_y and not ball_position.y <= ball_size:
        ball_position.y -= ball_speed * delta_time
        if ball_position.y <= ball_size:
            ball_position.y = ball_size
            ball_colided_y = False
    elif not ball_colided_y and not ball_position.y >= (screen_height - ball_size):
        ball_position.y += ball_speed * delta_time
        if ball_position.y >= (screen_height - ball_size):
            ball_colided_y = (screen_height - ball_size)
            ball_colided_y = True

    # left pong deflect
    if (ball_position.x - ball_size) <= (left_pong_position.x + pong_size.x) and (ball_position.x - ball_size) >= left_pong_position.x:
        if (ball_position.y + ball_size) >= (left_pong_position.y - (pong_size.y / 2)) and (ball_position.y + ball_size) <= left_pong_position.y + (pong_size.y / 2):
            right_pong_move = True
            ball_colided_x = False

    # right pong deflect
    if (ball_position.x + ball_size) <= (right_pong_position.x + pong_size.x) and (ball_position.x + ball_size) >= right_pong_position.x:
        if (ball_position.y + ball_size) >= (right_pong_position.y - (pong_size.y / 2)) and (ball_position.y + ball_size) <= (right_pong_position.y + (pong_size.y / 2)):
            right_pong_move = False
            ball_colided_x = True

    # ======================================================
    # ================== left pong script ==================

    if keys[pygame.K_w] and left_pong_position.y >= (pong_size.y / 2):
        left_pong_position.y -= (pong_speed * delta_time)
    elif keys[pygame.K_s] and left_pong_position.y <= (screen_height - (pong_size.y / 2)):
        left_pong_position.y += (pong_speed * delta_time)

    # ======================================================
    # ================= right pong script ==================

    if right_pong_move and (pong_size.y / 2) <= right_pong_position.y >= ball_position.y:
        right_pong_position.y -= pong_speed * delta_time
    elif right_pong_move and (screen_height - (pong_size.y / 2)) >= right_pong_position.y <= ball_position.y:
        right_pong_position.y += pong_speed * delta_time

    # ======================================================
    # ================== screen appear =====================

    pygame.display.set_caption(f"Pong: FPS: {current_FPS}")
    current_FPS = int(clock.get_fps())
    pygame.display.flip()

    # ======================================================

pygame.quit()