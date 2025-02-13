import pygame
my_list = [100, 100, 200]  # Список (List)
my_tuple = (100, 100, 200)  # Кортеж (Tuple)
main_screen = pygame.display.set_mode((500, 500))

actor_surf = pygame.Surface((50, 100))
actor_rect = actor_surf.get_rect()

button_skill_1 = pygame.Rect(100, 400, 50, 50)

delta = 0
while True:
    pygame.time.delay(60)
    main_screen.fill((0, 0, 255))
    main_screen.blit(actor_surf, actor_rect)
    actor_surf.fill((0, 255, 0))
    pygame.draw.rect(main_screen, color=(255, 0, 0), rect=button_skill_1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                delta = 20
            elif event.key == pygame.K_LEFT:
                delta = -20

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                delta = 0
            elif event.key == pygame.K_LEFT:
                delta = 0

    actor_rect.x += delta
    pygame.display.update()
