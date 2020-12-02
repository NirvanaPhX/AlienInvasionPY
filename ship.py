import pygame

class Ship:
    """A class to manage the ship"""
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()


        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Initialize starting position
        self.rect.midbottom = self.screen_rect.midbottom # rect.attributes is the attributes determine the starting position

        self.x = float(self.rect.x)

        # Set up movement flag
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Function to manage the ship action"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """Draw ship to the screen"""
        self.screen.blit(self.image, self.rect)