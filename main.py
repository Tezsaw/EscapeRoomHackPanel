import pygame

pygame.init()

# constants
SIZE_INFO = pygame.display.Info()
FONT = pygame.font.Font("assets/RobotoMonoFont.ttf", 20)

# setup
screen = pygame.display.set_mode((SIZE_INFO.current_w, SIZE_INFO.current_h), pygame.FULLSCREEN)
all_sprites = pygame.sprite.Group()

camera_position = pygame.Vector2(0, 0)


class ExitButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)

        self.image = pygame.Surface((50, 30))
        self.image.fill((255, 128, 128))

        self.image.blit(FONT.render("Exit", True, (0, 0, 0)), (0, 0))

        self.rect = self.image.get_rect()
        self.rect.x = SIZE_INFO.current_w - self.image.get_width()
        self.rect.y = 0

    def update(self):
        global running

        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    running = False
                break


exit_button = ExitButton()


class NetworkNode(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__(all_sprites)

        self.pos = pygame.Vector2(x, y)

        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        self.image.blit(image, (0, 0))

        self.rect = self.image.get_rect()


# game loop
running = True
while running:
    events = pygame.event.get()
    for e_ in events:
        if e_.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
