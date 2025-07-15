import pygame


class Score(pygame.sprite.Sprite):
    def __init__(self, x, y,):
        super().__init__()
        self.font = pygame.font.SysFont('Arial', 30)
        self.x = x
        self.y = y
        self.image = None
        self.rect = None
        self.start_time = pygame.time.get_ticks()
        self.current_time_score = 0
        self.update_display()

    def update_display(self):
        self.image = self.font.render(f"Time: {self.current_time_score}", True, (255, 0, 0)) # Red text!
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        

    def update(self):
        elapsed_seconds = (pygame.time.get_ticks() - self.start_time) / 1000
        self.current_time_score = int(elapsed_seconds)
        self.update_display()

    def draw(self, screen):
        screen.blit(self.image, self.rect)